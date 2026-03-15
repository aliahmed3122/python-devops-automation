# -------------------------------------------------
# For Loop

PLANET = "Earth"

for letter in PLANET:
    print(letter)
print("-----------------------------")


VACCINES = ("Moderna", "Pfizer", "Sputnik V", "AstraZeneca", "Covaxin")

for vac in VACCINES:
    print(f"{vac} vaccine provides Immunization against Covid-19")


# Nested For Loop
for vac in VACCINES:
    print("")
    print("I Would like to take a shot of ")
    for i in vac:
        print(i)
    
print("-----------------------------")


# -------------------------------------------------
# While Loop

x = 0
while x <= 10:
    # code to execute
    print("Value of x:", x)
    x += 1
else:
    # code to execute when the loop condition is false
    print("Loop finished")
    
print("-----------------------------")    


import time

x = 2
while x < 2049:
    
    print("Value of x:", x)
    x *= 2
    time.sleep(1)
   
# -------------------------------------------------
    