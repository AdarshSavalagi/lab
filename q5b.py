import re

def search_contacts(file_name):
    phone_pattern = r'\+\d{1,3}\d{10}'
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'

    with open(file_name, 'r') as file:
        content = file.read()

        phone_numbers = re.findall(phone_pattern, content)
        email_addresses = re.findall(email_pattern, content)

        return phone_numbers, email_addresses

# Test the function
file_name = input("Enter the file name: ")
phone_numbers, email_addresses = search_contacts(file_name)

print("Phone numbers:")
for phone_number in phone_numbers:
    print(phone_number)

print("Email addresses:")
for email_address in email_addresses:
    print(email_address)
