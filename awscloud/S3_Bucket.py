import boto3

# Create S3 client
s3 = boto3.client("s3", region_name="us-east-1")

bucket_name = "devops-boto3-test-s3-153718962451-us-east-1-an"               # must be globally unique
file_name   = input("Enter the Path to the file you want to upload : ")      # File to upload (should be in the same directory as this script or provide full path)
object_name = file_name                                                      # The name of the file in the S3 bucket (can be different from file_name)

# Create bucket
# s3.create_bucket(Bucket=bucket_name)

# Upload file to bucket
try:
    s3.upload_file(file_name, bucket_name, object_name)
except Exception as exception:
    print(f"Error uploading file: {exception}")
else:
    print(f"File '{file_name}' uploaded to bucket '{bucket_name}' as '{object_name}'.")
    
