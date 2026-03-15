import random

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


def time_activity(*args, **kwargs):
    # print(args)
    # print(kwargs)
    mini = sum(args) + random.randint(0, 60)  # Simulating some random time for the activities
    # print(min)
    choice = random.choice(list(kwargs.keys()))
    # print(choice)
    print(f"You have to spend  {mini} for {kwargs[choice]}")
    print("---------------------------------------------")