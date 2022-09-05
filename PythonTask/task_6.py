import random

def random_list(number_count):
    number = []
    for i in range(number_count):
        number.append(random.randint(0, 9))
    print(number)

list_length = int(input("write number: "))
random_list(list_length)
