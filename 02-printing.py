#LINK - https://www.w3schools.com/python/python_ref_string.asp
# ------------------------------------------------------------
name    = "sars_cov_2"
disease = "COVID-19"

# format num_1
print("The name of virus is ",name)
print("The disease caused by virus is ",disease)

# format num_2
print("The name of virus is {}.".format(name))
print("{} is the name of virus.".format(name))
print("The name of virus is {} and it causes {}.".format(name,disease))

# format num_3
print(f"The name of virus is {name} and it causes {disease}.")   # Best


# --------------------------------------------
# Concatenation
print("The name of virus is" + " " + name)

