# IF Conditions

x = 10

if x < 30:
    print("x is less than 30")

print("-----------------------------") 
# If-Else

if x > 5:
    print("x is greater than 5")
else:
    print("x is less than or equal to 5")  
    
print("-----------------------------") 
# If-Elif-Else

if x < 5:
    print("x is less than 5")
elif x < 15:
    print("x is between 5 and 15")
else:
    print("x is greater than or equal to 15")                    
    

print("-----------------------------")
# Nested If

if x > 0:
    if x < 20:
        print("x is between 0 and 20")
    else:
        print("x is greater than or equal to 20")
elif x < 0:
    print("x is negative")
    
else:
    print("x is zero")


      
print("-----------------------------")


# Example

DevOps = ["Docker", "Kubernetes", "CI/CD", "Monitoring"]
Develpopment = ["Python", "JavaScript", "Java", "C++"]

cntr_emp1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 1024}
cntr_emp2 = {"Name": "Rudolf", "Skill": "AI", "Code": 1218}

usr_skill = input("Enter your desired skill: ")

# Check in the database if we have this skill

if usr_skill in DevOps:
    print(f"{usr_skill} in DevOps Team.")
elif usr_skill in Develpopment:
    print(f"{usr_skill} in Development Team.")
elif (usr_skill in cntr_emp1.values()) or (usr_skill in cntr_emp2.values()):
    print("We have contract employees with this skill.")
else:    
    print("Sorry, we don't have this skill in our database.")    
    
    
