# try → except → else → finally
# ------------------------------

# try block:
# Code that might raise an exception (an error) is placed here.
# Python will attempt to execute this block first.
try:
    Number = int(input("Enter a Number : "))
    result = 10 / Number

# except block (specific exception):
# This block runs if a ValueError occurs inside the try block.
# ValueError happens when the input cannot be converted to an integer.
except ValueError:
    print("Invalid input! Please enter a valid number.")

# except block (another specific exception):
# This block handles the case when the user enters 0,
# which causes a division by zero error.
except ZeroDivisionError:
    print("Can't divide a number by zero.")

# except block (generic exception handler):
# This catches any unexpected exception that was not handled above.
# The error object is stored in the variable 'exception'.
except Exception as exception:
    print(f"An Unexpected error occurred: {exception}")

# else block:
# This block runs only if the try block executes successfully
# and no exceptions were raised.
else:
    print(f"The Result is : {result}")

# finally block:
# This block always runs regardless of whether an exception occurred or not.
# It is commonly used for cleanup actions (closing files, releasing resources, etc.).
finally:
    print("This Program ends here.")
    print("Happy Coding.")





















