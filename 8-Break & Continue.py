import random

# -------------------------------------------------
# Break Statement
"""
for i in "DevOps":
    print(i)
    if i == "O":
        print("Found my target letter.")
        break
    
print("Outside the loop")

# -------------------------------------------------
# Continue Statement
for i in "DevOps":
    if i == "O":
        print("Found my target letter.")
        continue
    print(f"Current letter: {i}")
print("Outside the loop")

"""
# -------------------------------------------------
# Examples

VACCINES = ["Moderna", "Pfizer", "Sputnik V", "AstraZeneca"]


random.shuffle(VACCINES)
print(VACCINES)

Lucky = random.choice(VACCINES)
print(Lucky)

for vac in VACCINES:
    print(f"******TESTING VACCINE {vac}")
    if vac == Lucky:
        print("############################")
        print(f"{Lucky} Vaccine, Test Successful.")
        print("############################")
        print()
        break

    print("XXXXXXXXXX")
    print("Test Failed.")
    print("XXXXXXXXXX")
    print()

# -------------------------------------------------
