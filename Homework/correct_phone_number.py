import re

def correct_phone_num():
    phon_num = input("Enter a phon number: ")
    phon_lst = []
    while not re.search("^05[0-9]-[0-9]{7}$", phon_num):
        phon_lst.append(phon_num)
        phon_num = input("Enter a phon number: ")
    for i in phon_lst:
        print(f"{i} is not a correct phon number!")
    print(f"\n{phon_num} is a correct phon number!")

correct_phone_num()