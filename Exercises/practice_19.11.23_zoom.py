
# רשימה אפשר לשנות ולדרוס
#my_list = [1, 3, 8]

#מרייך א"א לשנות (לדרוס כן)
#my_tuple = (1, 3, 8)

#my_tuple_1 = ("mmmm")

#print(my_tuple_1)

def go(str1, str2):
    return sorted(list(str1)) == sorted(list(str2))

print(go("mendy", "yndme"))
