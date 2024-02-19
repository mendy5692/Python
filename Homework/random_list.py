import random
import re
def get_list(lst):
    new_lst = []
    for i in lst:
        if i.isupper():
            new_lst.append(i)

    return ''.join(random.choices(new_lst, k = len(lst)))

def get_list_regex(lst):
    new_lst = re.findall('[A-Z]', lst)
    return ''.join(random.choices(new_lst, k=len(lst)))



lst = "aBCd@#Efg454"
print(f"normal: {get_list(lst)}")
print(f"regex: {get_list_regex(lst)}")