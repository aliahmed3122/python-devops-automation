from fabric.api import *

# First Command
def greetings(msg):
    print(f"Good {msg}")


# Second Command
def system_info():

    print("Disk Space.")
    print("--------------")
#    local("df -h") # for Linux
    local("wmic logicaldisk get size,freespace,caption")
    print("----------------------------------------------")

    print("Memory info.")
    print("--------------")
#    local("free -m") # for Linux
    print("----------------------------------------------")


    print("System Uptime.")
#    local("uptime") # for Linux
    local("systeminfo")
    print("----------------------------------------------")

# Third Command
def remote_exec():

    print("Host Name.")
    print("--------------")
    run("hostname")
    print("----------------------------------------------")

    print("Disk Space.")
    print("--------------")
    run("df -h")
    print("----------------------------------------------")


    print("Memory info.")
    print("--------------")
    run("free -m")
    print("----------------------------------------------")


    print("System Uptime.")
    print("--------------")
    run("uptime")
    print("----------------------------------------------")


# Fourth Command
def web_setup(WEBURL, DIRNAME):
   print("-----------------------------------------------------------------------------------")
   local("apt install zip unzip -y")

   print("-----------------------------------------------------------------------------------")
   print("Installing dependencies")
   print("-----------------------------------------------------------------------------------")
   sudo("yum install httpd wget unzip -y")

   print("-----------------------------------------------------------------------------------")
   print("Start & enable service.")
   print("-----------------------------------------------------------------------------------")
   sudo("systemctl start httpd")
   sudo("systemctl enable httpd")

   print("-----------------------------------------------------------------------------------")
   print("Downloading and pushing website to webservers.")
   print("-----------------------------------------------------------------------------------")
   local(("wget -O website.zip %s") % WEBURL)
   local("unzip -o website.zip")

   print("-----------------------------------------------------------------------------------")
   with lcd(DIRNAME):
       local("zip -r tooplate.zip * ")
       put("tooplate.zip", "/var/www/html/", use_sudo=True)

   with cd("/var/www/html/"):
      sudo("unzip -o tooplate.zip")

   sudo("systemctl restart httpd")

   print("Website setup is done.")

