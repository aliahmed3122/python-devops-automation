"""
# String Buils in Methods/Functions
message = "corona vaccine is ready to use, most of them are more than 90% effective."

# Some built-in methods for string manipulation
print(message)
print(message.capitalize())
print(message.upper())
print(message.lower())
print(message.title())
print(message.strip())    
print(message.replace("corona", "COVID-19"))
print(message.split(","))
print(message.islower())
print(message.isupper())
print(message.isalpha())           # Checks if all characters in the string are alphabetic (letters only, no spaces or punctuation)
print(message.find("ready"))       # Returns the index of the first occurrence of the substring "ready"
print(message.find("not"))         # Returns -1 if the substring is not found
print(message.count("e"))          # Counts the number of occurrences of the letter "e" in the string
print(message.startswith("corona"))
print(message.endswith("effective."))
# ---------------------------------------------
"""

"""
print("----------------------------------------------------------------")
print(dir(message))  # List all attributes and methods of the string object
print(dir([]))       
print(dir({}))
print(dir(()))
print(dir(""))    
print("----------------------------------------------------------------")
# ---------------------------------------------
"""


"""
print("----------------------------------------------------------------")
# 1. capitalize() - Converts the first character of a string to uppercase and the rest to lowercase.
text = "hello world"
capitalized_text = text.capitalize()
print(capitalized_text)  # Output: "Hello world"

# 2. upper() - Converts all characters in a string to uppercase.
text = "hello world"
upper_text = text.upper()
print(upper_text)  # Output: "HELLO WORLD"

# 3. lower() - Converts all characters in a string to lowercase.
text = "HELLO WORLD"
lower_text = text.lower()
print(lower_text)  # Output: "hello world"

# 4. title() - Converts the first character of each word to uppercase and the rest to lowercase.
text = "hello world"
title_text = text.title()
print(title_text)  # Output: "Hello World"

# 5. strip() - Removes leading and trailing whitespace from a string.
text = "   hello world   "
stripped_text = text.strip()
print(stripped_text)  # Output: "hello world"

# 6. replace() - Replaces occurrences of a specified substring with another substring.
text = "hello world"
replaced_text = text.replace("world", "Python")
print(replaced_text)  # Output: "hello Python"

# 7. split() - Splits a string into a list of substrings based on a specified delimiter.
text = "hello,world,python"
split_text = text.split(",")
print(split_text)  # Output: ["hello", "world", "python"]

# 8. islower() - Checks if all characters in a string are lowercase.
text = "hello world"
print(text.islower())  # Output: True

# 9. isupper() - Checks if all characters in a string are uppercase.
text = "HELLO WORLD"
print(text.isupper())  # Output: True

# 10. isalpha() - Checks if all characters in a string are alphabetic (letters only, no spaces or punctuation).
text = "hello"
print(text.isalpha())  # Output: True
text = "hello world"
print(text.isalpha())  # Output: False

# 11. find() - Returns the index of the first occurrence of a specified substring in a string. If the substring is not found, it returns -1.
text = "hello world"
index = text.find("world")
print(index)  # Output: 6
index = text.find("python")
print(index)  # Output: -1

# 12. count() - Counts the number of occurrences of a specified substring in a string.
text = "hello world"
count = text.count("o")
print(count)  # Output: 2

# 13. startswith() - Checks if a string starts with a specified substring.
text = "hello world"
print(text.startswith("hello"))  # Output: True
print(text.startswith("world"))  # Output: False

# 14. endswith() - Checks if a string ends with a specified substring.
text = "hello world"
print(text.endswith("world"))  # Output: True
print(text.endswith("hello"))  # Output: False

print("----------------------------------------------------------------")
# ---------------------------------------------
"""


""" 
# Joining a sequence of strings with a specified separator
seq1 = ("192", "168", "40", "90")

print(".".join(seq1))   # Output: 192.168.40.90
print("/".join(seq1))   # Output: 192/168/40/90
print("-".join(seq1))   # Output: 192-168-40-90

# ---------------------------------------------

"""

"""
DevOps = ["Docker", "Kubernetes", "CI/CD", "Monitoring"]
print(DevOps)

DevOps.append("Terraform")           # Adds "Terraform" to the end of the list
print(DevOps)

DevOps.insert(2, "Ansible")          # Inserts "Ansible" at index 2 (before "CI/CD")
print(DevOps)

DevOps.extend(["Git", "Jenkins"])    # Extends the list by adding elements from another list ["Git", "Jenkins"]
print(DevOps)

DevOps.sort()                        # Sorts the list in alphabetical order
print(DevOps)

DevOps.remove("Monitoring")          # Removes the first occurrence of "Monitoring" from the list
print(DevOps)

DevOps.pop()                         # Removes and returns the last item in the list (in this case, "Jenkins")
print(DevOps)

DevOps.pop(4)                      # Removes and returns the item at index 1 (in this case, "Ansible")
print(DevOps)

DevOps.clear()                       # Removes all items from the list, leaving it empty
print(DevOps)

# ---------------------------------------------

"""

cntr_emp1 = {"Name": "Santa", "Skill": "Blockchain", "Code": 1024}
print(cntr_emp1.keys())                      # Output: dict_keys(['Name', 'Skill', 'Code']
print(cntr_emp1.values())                    # Output: dict_values(['Santa', 'Blockchain', 1024])

print(cntr_emp1.get("Name"))                 # Output: "Santa"
print(cntr_emp1.get("Age", "Not Found"))     # Output: "Not Found" (since "Age" key does not exist)

print(cntr_emp1.items())                     # Output: dict_items([('Name', 'Santa'), ('Skill', 'Blockchain'), ('Code', 1024)])
print(cntr_emp1.pop("Skill"))                # Output: "Blockchain" (removes the "Skill" key-value pair from the dictionary)
print(cntr_emp1)                             # Output: {'Name': 'Santa', 'Code': 1024} (after popping "Skill")

print(cntr_emp1.popitem())                   # Output: ('Code', 1024) (removes and returns the last key-value pair from the dictionary)
print(cntr_emp1)                             # Output: {'Name': 'Santa'} (after

cntr_emp1.clear()                            # Removes all key-value pairs from the dictionary, leaving it empty
print(cntr_emp1)                             # Output: {} (after clearing the dictionary)

