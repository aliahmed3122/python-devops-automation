#!/usr/bin/python3
import os

userlist = ["alpha", "beta", "gamma"]

print("Adding Users to System")
print("-----------------------------------------")

# Loop to add user from userlist.
for user in userlist:
    exitcode = os.system("id {}".format(user))
    if exitcode != 0:
        print("User {} doesn't exist, Adding it.".format(user))
        print("----------------------------------------------")
        print()
        os.system("useradd {}".format(user))
    else:
        print("User {} already exist, skipping it.".format(user))
        print("----------------------------------------------")
        print()


# Condition to check if group exists or not, add if not exist.
exitcode = os.system("grep science /etc/group")

if exitcode != 0:
    print("Group science doesn't exist, Adding it.")
    print("----------------------------------------------")
    print()
    os.system("groupadd science")
else:
    print("Group science already exist, skipping it.")
    print("----------------------------------------------")
    print()

# Adding Users from userlist to the science group.
for user in userlist:
    print("Adding User {} in the science group.".format(user))
    print("----------------------------------------------")
    print()
    os.system("usermod -G science {}".format(user))

# Adding directory
print("Adding directory")
print("----------------------------------------------")
print()

directory = "/opt/science_dir"

if os.path.isdir(directory):
    print("Directory already exists, skipping it")
else:
    os.mkdir(directory)

print("Assigning permission and ownership to the directory.")
print("----------------------------------------------")
print()

os.system("chown :science /opt/science_dir")

os.system("chmod 770 /opt/science_dir")