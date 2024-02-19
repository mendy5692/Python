class IntNode():
    def __init__(self, value, next = None):
        self.value = value
        self.next = next
    def get_value(self):
        return self.value
    def get_next(self):
        return self.next
    def set_value(self, value):
        self.value = value
    def set_next(self, next):
        self.next = next
    def value_to_string(self):
        return str(self.value)
    def get_all_values(self, first):
        while first != None:
            print(first.get_value())
            first = first.get_next()
    def get_count(self, first):
        count = 0
        while first != None:
            count += 1
            first = first.get_next()
        return count
    def get_sum(self, first):
        sum = 0
        while first != None:
            sum += first.get_value()
            first = first.get_next()
        return sum
    def get_maximal(self, first):
        maximal = 0
        while first != None:
            if first.get_value() > maximal:
                maximal = first.get_value()
            first = first.get_next()
        return maximal

    def count_number(self, first, num):
        count_num = 0
        while first != None:
            if first.get_value() == num:
                count_num += 1
            first = first.get_next()
        return count_num

    def first_index_num(self, first, num):
        index_num = 0
        index_my_num = 0
        while first != None:
            if first.get_value() == num:
                index_my_num = index_num
                break
            index_num += 1
            first = first.get_next()
        return index_my_num

    def last_index(self, first, num):
        index_num = 0
        index_my_num = 0
        while first != None:
            if first.get_value() == num:
                index_my_num = index_num
            index_num += 1
            first = first.get_next()
        return index_my_num

    def avg(self, first):
        return first.get_sum(first) / first.get_count(first)

    def max_index(self, first):
        max_index = -1
        while first != None:
            max_index += 1
            first = first.get_next()
        return max_index

    def add_ten(self, first):
        while first != None:
            first.set_value(first.get_value() + 10)
            first = first.get_next()

    def add_val(self, first, value):
        while first != None:
            first.set_value(first.get_value() + value)
            first = first.get_next()

    def div_two(self, first):
        while first != None:
            first.set_value(first.get_value() / 2)
            first = first.get_next()

    def check_update_val(self, first, val):
        while first != None:
            if val <= first.get_value():
                first.set_value(first.get_value() * 2)
            else:
                first.set_value(first.get_value() / 2)
            first = first.get_next()

first = None
for i in range(1, 5):
    first = IntNode(i, first)
pass
for i in range(1, 5):
    first = IntNode(i, first)
pass
for i in range(1, 5):
    first = IntNode(i, first)
pass
#
# for i in range(8, 0, -2):
#     first = IntNode(i, first)
# pass
#
# for i in range(20, 60, 10):
#     first = IntNode(i, first)
# pass
#
# for i in range(40, 0, -10):
#     first = IntNode(i, first)
# pass





first.get_all_values(first)
print(f"the num of the interactions is '{first.get_count(first)}'.")
print(f"the sum of the all interactions is '{first.get_sum(first)}'.")
print(f"the maximal value from the objects is '{first.get_maximal(first)}'.")
print(f"'1' is '{first.count_number(first,1)}' times.")
print(f"the avarge of the all numbers is '{first.avg(first)}'")
print(f"the last index in the interactions is '{first.max_index(first)}'")
print(f"The first index that holds the number '3' is '{first.first_index_num(first,3)}'")
print(f"The last index that holds the number '3' is '{first.last_index(first,3)}'")
first.add_ten(first)
first.get_all_values(first)
print("--------------------------------")
first.add_val(first, 1)
first.get_all_values(first)
print("--------------------------------")
first.div_two(first)
first.get_all_values(first)
print("--------------------------------")
first.check_update_val(first, 6)
first.get_all_values(first)



