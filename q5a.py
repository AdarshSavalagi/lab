# without using regular pattern (re module)
# def isphonenumber(phone_number):
#     if len(phone_number) != 12:
#         return False
#     for i in range(0, 3):
#         if not phone_number[i].isdecimal():
#             return False
#     if phone_number[3] != '-':
#         return False
#     for i in range(4, 7):
#         if not phone_number[i].isdecimal():
#             return False
#     if phone_number[7] != '-':
#         return False
#     for i in range(8, 12):
#         if not phone_number[i].isdecimal():
#             return False
#     return True

# with using regular pattern (re module)
import re

def isphonenumber(phone_number):
    pattern = r'^\d{3}-\d{3}-\d{4}$'
    if re.match(pattern, phone_number):
        return True
    else:
        return False

number = input("Enter a phone number: ")
if isphonenumber(number):
    print("Valid phone number")
else:
    print("Invalid phone number")
