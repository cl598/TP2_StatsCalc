import random

class RandomNums:

    list1 = []

    list2_range = range(10)
    list2 = []

    def __init__(self):
        pass

    # Without seeding
    for num in range(list1.length):
        random_value = random.random()
        list1.append(random_value)

    # With seeding
    for num2 in range(list2_range.length):

        random.seed(10)
        random_value2 = random.randint(0,10)
        list2.append(random_value2)
