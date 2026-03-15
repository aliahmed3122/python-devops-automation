from my_module import time_activity
from my_module import *
import my_module
print(dir(my_module))
print("------------------------------------------")

# Calling the function directly without module name use 'from my_module import time_activity'.
time_activity(10, 20, 30, Activity_1="Coding", Activity_2="Testing", Activity_3="Debugging")

# Calling the function with module name use '*' .
vac_feedback("Covaxin", 78)

# Calling the function with module name use 'import my_module'.
my_module.order_food_with_extras("Burger", "Fries", "Coke", Souce="Ketchup", Size="Large")



