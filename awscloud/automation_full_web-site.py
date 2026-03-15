import boto3
import requests
import time

region = "us-east-1"
template_name = "health"

ec2 = boto3.client("ec2", region_name=region)
elbv2 = boto3.client("elbv2", region_name=region)

# -----------------------------
# 1. Get My Public IP
# -----------------------------
my_ip = requests.get("https://checkip.amazonaws.com").text.strip()
cidr_my_ip = f"{my_ip}/32"

# -----------------------------
# 2. Create Key Pair
# -----------------------------
key_name = f"{template_name}-key"

key = ec2.create_key_pair(KeyName=key_name)

with open(f"{key_name}.pem", "w") as f:
    f.write(key["KeyMaterial"])

print("Key pair created:", key_name)

# -----------------------------
# 3. Get VPC and Subnets
# -----------------------------
vpcs = ec2.describe_vpcs()
vpc_id = vpcs["Vpcs"][0]["VpcId"]

subnets = ec2.describe_subnets(
    Filters=[{"Name": "vpc-id", "Values": [vpc_id]}]
)

subnet_ids = [s["SubnetId"] for s in subnets["Subnets"]]
subnet_id = subnet_ids[0]

print("Using subnet:", subnet_id)

# -----------------------------
# 4. Create Security Groups
# -----------------------------
sg_ec2 = ec2.create_security_group(
    GroupName=f"{template_name}-ec2-sg",
    Description="EC2 SG",
    VpcId=vpc_id
)

sg_ec2_id = sg_ec2["GroupId"]

ec2.authorize_security_group_ingress(
    GroupId=sg_ec2_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 22,
            "ToPort": 22,
            "IpRanges": [{"CidrIp": cidr_my_ip}]
        },
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }
    ]
)

print("EC2 Security group created:", sg_ec2_id)

sg_alb = ec2.create_security_group(
    GroupName=f"{template_name}-alb-sg",
    Description="ALB SG",
    VpcId=vpc_id
)

sg_alb_id = sg_alb["GroupId"]

ec2.authorize_security_group_ingress(
    GroupId=sg_alb_id,
    IpPermissions=[
        {
            "IpProtocol": "tcp",
            "FromPort": 80,
            "ToPort": 80,
            "IpRanges": [{"CidrIp": "0.0.0.0/0"}]
        }
    ]
)

print("ALB Security group created:", sg_alb_id)

# -----------------------------
# 5. User Data Script
# -----------------------------
user_data = """#!/bin/bash
yum update -y
yum install httpd wget unzip -y
systemctl start httpd
systemctl enable httpd
cd /tmp
wget https://www.tooplate.com/zip-templates/2098_health.zip
unzip 2098_health.zip
cp -r 2098_health/* /var/www/html/
systemctl restart httpd
"""

# -----------------------------
# 6. Amazon Linux 2023 AMI
# -----------------------------

ami_id = "ami-02dfbd4ff395f2a1b"

print("Using AMI:", ami_id)

# -----------------------------
# 7. Launch EC2 Instance
# -----------------------------
instance = ec2.run_instances(
    ImageId=ami_id,
    InstanceType="t2.micro",
    KeyName=key_name,
    SecurityGroupIds=[sg_ec2_id],
    SubnetId=subnet_id,
    MinCount=1,
    MaxCount=1,
    UserData=user_data,
    TagSpecifications=[
        {
            "ResourceType": "instance",
            "Tags": [{"Key": "Name", "Value": f"{template_name}-server"}]
        }
    ]
)

instance_id = instance["Instances"][0]["InstanceId"]

print("Instance launching:", instance_id)

print("Waiting for instance to be running...")
waiter = ec2.get_waiter("instance_running")
waiter.wait(InstanceIds=[instance_id])

# Give time for user-data script
print("Waiting for web server setup...")
time.sleep(60)

# -----------------------------
# 8. Create Target Group
# -----------------------------
tg = elbv2.create_target_group(
    Name=f"{template_name}-tg",
    Protocol="HTTP",
    Port=80,
    VpcId=vpc_id,
    TargetType="instance",
    HealthCheckProtocol="HTTP",
    HealthCheckPath="/"
)

tg_arn = tg["TargetGroups"][0]["TargetGroupArn"]

# register instance
elbv2.register_targets(
    TargetGroupArn=tg_arn,
    Targets=[{"Id": instance_id}]
)

print("Instance registered to target group")

# -----------------------------
# 9. Create ALB
# -----------------------------
alb = elbv2.create_load_balancer(
    Name=f"{template_name}-alb",
    Subnets=subnet_ids,
    SecurityGroups=[sg_alb_id],
    Scheme="internet-facing",
    Type="application"
)

alb_arn = alb["LoadBalancers"][0]["LoadBalancerArn"]
alb_dns = alb["LoadBalancers"][0]["DNSName"]

print("ALB created:", alb_dns)

# -----------------------------
# 10. Create Listener
# -----------------------------
elbv2.create_listener(
    LoadBalancerArn=alb_arn,
    Protocol="HTTP",
    Port=80,
    DefaultActions=[
        {
            "Type": "forward",
            "TargetGroupArn": tg_arn
        }
    ]
)
time.sleep(60)  # Wait for ALB to be fully ready

print("\nApplication Load Balancer ready")
print(f"\nOpen the website at:\nhttp://{alb_dns}")