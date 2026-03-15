planet1 = "closet of the sun"
print(planet1)
print(len(planet1))  # 17

# print from start
print(planet1[0])  # c
print(planet1[1])  # l  
print(planet1[2])  # o

# print from last
print(planet1[-1])  # n
print(planet1[-2])  # u
print(planet1[-3])  # s


# Slicing a string, get a substring from the string
print(planet1[1:4])  # los
print(planet1[:])    # closet of the sun
print(planet1[0:])   # closet of the sun
print(planet1[:7])   # closet
print(planet1[15:])  # un

# --------------------------------------------
# Slicing Tuple

devops = ("Linux", "Docker", "Kubernetes", "Ansible", "Terraform", "Git", "Jenkins")

print(devops[0])
print(devops[4]) 
print(devops[-1])

print(devops[2:5])              # Kubernetes, Ansible, Terraform
print(devops[2:5][0])           # Kubernetes

print(devops[2:5][0][5:8])      # net

print(devops[2:5][0][5:8][-1])  # t


# --------------------------------------------
# Slicing List

devops = ["Linux", "Docker", "Kubernetes", "Ansible", "Terraform", "Git", "Jenkins"]

print(devops[0])
print(devops[4]) 
print(devops[-1])

print(devops[2:5])              # Kubernetes, Ansible, Terraform
print(devops[2:5][0])           # Kubernetes

print(devops[2:5][0][5:8])      # net

print(devops[2:5][0][5:8][-1])  # t


# --------------------------------------------
# Dictionary Example

skills = {"Programming": ("Python", "Java", "C++"), "DevOps": ["Docker", "Kubernetes", "Ansible"]}

print(skills)
print(skills["Programming"])  # ('Python', 'Java', 'C++')
print(skills["DevOps"])       # ['Docker', 'Kubernetes', 'Ansible']

print(skills["Programming"][0])   # Python
print(skills["DevOps"][-1])       # Kubernetes
print(skills["DevOps"][-1][:4])   # ock
