import re

email = input("What's your email? ").strip()

if re.search("^[a-zA-Z0-9_]+@[^@]+\.edu$",email,re.IGNORECASE):
    print("Valid")
else:
    print("Invalid")