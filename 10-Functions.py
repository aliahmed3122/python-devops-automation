import random

# -------------------------------------------------------------------
# Defining a function
print("----------------------------------------------------------------")
def __greet__(name):
    return f"Hello, {name}!"

# Calling the function

# name = input("Enter your name: ")
name = "Alice"
print(__greet__(name))  # Output: "Hello, Alice!"
print("----------------------------------------------------------------")

def add(arg1, arg2):
    total = arg1 + arg2
    return total

result = add(5, 3)
print(result)       # Output: 8
print(add(10, 20))  # Output: 30
print("----------------------------------------------------------------")

# -------------------------------------------------------------------
# whithout return statement, the function will return None by default.
def adder(arg1, arg2):
    total = arg1 + arg2
    print(total)
    
adder(2, 3)  # Output: 5
print("----------------------------------------------------------------")


# -------------------------------------------------------------------
# Examples

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))  # Output: 120
print("----------------------------------------------------------------")    

def sum(numbers):
    total = 0
    for num in numbers:
        total += num
    return total

print(sum([1, 20, 3, 4, 50]))            # Output: 78
print("----------------------------------------------------------------")    


# -------------------------------------------------------------------
# Default Arguments

def greet(MSG="Morning"):
    print (f"Good {MSG}!")
    print("Welcome to the function.")

greet()                 # Output: "Good Morning!"
greet("Evening")        # Output: "Good Evening!" 
print("----------------------------------------------------------------")


# -------------------------------------------------------------------
# Keyword Arguments

def vac_feedback(vac,efficacy):
    print(f"{vac} vaccine is having {efficacy} % efficacy.")
    if (efficacy > 50) and (efficacy <= 75):
        print("This is a good vaccine.")
    elif (efficacy > 75) and (efficacy <= 90):
        print("This is a very good vaccine.")
    elif (efficacy >= 90):
        print("This is an excellent vaccine.")
    else:
        print("This is a poor vaccine.")
    print("--------------------------")
        
vac_feedback("Covaxin", 78)                # Output: "Covaxin vaccine is having 78 % efficacy."
vac_feedback(efficacy=95, vac="Pfizer")    # Output: "Pfizer vaccine is having 95 % efficacy."

print("----------------------------------------------------------------")


# -------------------------------------------------------------------
# Variable-Length Arguments *args and **kwargs
# *args allows you to pass a variable number of non-keyword arguments to a function, classified as a tuple  <class 'tuple'>. 
# **kwargs allows you to pass a variable number of keyword arguments, classified as a dictionary <class 'dict'>.

# Example of *args in a function definition.
def order_food(min_order,*items):
    print(f"You have ordered: {min_order}.")
    for item in items:
        print(f"- {item}")
        
    print("Thank you for your order.")
    print("--------------------------")

# Example of *args and **kwargs in a function definition.
def order_food_with_extras(min_order, *items, **extras):
    print(f"You have ordered: {min_order}.")
    for item in items:
        print(f"- {item}")
    
    if extras:
        print("Extras:")
        for key, value in extras.items():
            print(f"  {key}: {value}")
    
    print("Thank you for your order.")
    print("--------------------------")
       
# Example of *args and **kwargs in a function definition and use of random module.         
def time_activity(*args, **kwargs):
    # print(args)
    # print(kwargs)
    mini = sum(args) + random.randint(0, 60)  # Simulating some random time for the activities
    # print(min)
    choice = random.choice(list(kwargs.keys()))
    # print(choice)
    print(f"You have to spend  {mini} for {kwargs[choice]}")
    print("---------------------------------------------")
   

# Calling the functions with variable-length arguments
order_food("Pizza", "Coke", "Fries") 
order_food_with_extras("Burger", "Fries", "Coke", Souce="Ketchup", Size="Large")      
time_activity(10, 20, 30, Activity_1="Coding", Activity_2="Testing", Activity_3="Debugging") 
   
   
# -------------------------------------------------------------------
   