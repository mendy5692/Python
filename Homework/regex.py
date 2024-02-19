import re

def check_file_name():
    file_name = input("Enter the file name: ")
    if re.search("^[\w]*[\w_()-]*\.(jpg|jpeg|png|gif)$", file_name):
        return True
    else:
        return False

while True:
    print(check_file_name())