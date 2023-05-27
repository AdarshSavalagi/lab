import zipfile
import os

def create_zip(folder_path, zip_file_name):
    with zipfile.ZipFile(zip_file_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                zipf.write(file_path, os.path.relpath(file_path, folder_path))


folder_path = input("Enter the folder path: ")
zip_file_name = input("Enter the ZIP file name: ")

create_zip(folder_path, zip_file_name)
print("ZIP file created successfully.")
