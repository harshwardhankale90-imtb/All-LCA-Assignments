
import re

# Accept string from user
s = input("Enter a string: ")

# Check whether string contains only alphabets and digits
if re.fullmatch(r'[a-zA-Z0-9]+', s):
    print("String contains only alphabets and digits")
else:
    print("String contains other characters")
