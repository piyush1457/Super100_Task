import re

def is_valid_email(email):
    pattern = r'^\S+@\S+\.\S+$'
    return re.match(pattern, email) is not None

print(is_valid_email("user@example.com"))  
print(is_valid_email("invalid@com"))       
print(is_valid_email("bad email@.com"))
