# 🚀 DevOps Python Automation

A hands-on collection of **Python scripts and labs for DevOps automation**, focusing on infrastructure, system administration tasks, and cloud automation using AWS.

This repository documents my journey learning **Python for DevOps engineering**, including automation scripts, cloud infrastructure provisioning, and system-level scripting.

---

# 📖 Overview

This repository contains multiple Python scripts used to understand and implement DevOps automation concepts.

Topics covered include:

* Python fundamentals for automation
* OS and file system automation
* Exception handling in scripts
* Infrastructure automation
* AWS cloud automation using **Boto3**
* Remote server automation using **Fabric**

The goal is to build practical DevOps skills through scripting and real-world infrastructure automation.

---

# 📂 Repository Structure

## Python Fundamentals

These scripts cover the core Python concepts required for automation.

```bash
00-QuotesAndComments.py
01-variables.py
02-printing.py
03-Datatypes.py
04-slicing.py
05-operators.py
06-Conditions.py
07-Loops.py
08-Break & Continue.py
09-Built-in-Methods.py
10-Functions.py
11-call-my_module.py
14-Exception_Handling.py
```

Concepts covered:

* Variables
* Data types
* Conditional logic
* Loops
* Functions
* Python built-in methods

---

## ⚙️ OS Automation Scripts

These scripts demonstrate automation tasks performed on the operating system.

```bash
12-check-file.py
13-OS-tasks.py
```

Examples include:

* Checking file existence
* Running system commands
* Automating OS tasks
* Handling runtime errors

---

## Fabric Automation

Remote automation using Fabric.

```bash
fabfile.py
```

Example use cases:

* Running commands on remote servers
* Automating deployments
* Managing remote systems

---

## ☁ AWS Cloud Automation

Cloud infrastructure automation scripts located in:

```bash
awscloud/
```

Examples include automation for:

* EC2 instance provisioning
* Security group creation
* S3 bucket operations
* Application Load Balancer creation
* Infrastructure deployment using Python and Boto3

These scripts simulate real DevOps automation workflows.

---

## 🛠️ Infrastructure Development Tools

```bash
Vagrantfile
```

Used to create reproducible development environments for learning and testing automation scripts.

---

# 🛠 Technologies Used

* Python
* AWS
* Boto3
* Fabric
* Vagrant
* Git & GitHub

---

# ☁ Cloud Automation

This repository includes automation examples using:

* AWS EC2
* AWS S3
* Application Load Balancer
* Security Groups

All automated using **Python + Boto3 SDK**.

Example workflow automated in the project:

1. Create Key Pair
2. Create Security Groups
3. Launch EC2 Instance
4. Deploy Website using User Data
5. Create Target Group
6. Create Application Load Balancer
7. Register Instance to Load Balancer

---

# ⚡ Getting Started

Clone the repository:

```bash
git clone https://github.com/yourusername/DevOps_Python.git
```

Navigate into the repository:

```bash
cd DevOps_Python
```

Create virtual environment:

```bash
python -m venv devops
```

Activate environment:

Linux / Mac

```bash
source devops/bin/activate
```

Windows

```bash
devops\Scripts\activate
```

Install dependencies:

```bash
pip install boto3 fabric requests
```

---

# 🔮 Future Improvements

Planned additions to this repository:

* Terraform automation examples
* CI/CD pipelines
* Docker automation scripts
* Kubernetes automation
* Ansible integration
* Advanced AWS automation

---

# ⭐ If you find this repository useful

Feel free to star ⭐ the project.

---
