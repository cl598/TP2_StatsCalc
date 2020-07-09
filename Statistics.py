import random

# Random number
def random_number(a):
    return a

# Select a random value from the list
def random_select(data):
    a = random.choice(data)
    return a

# Select n number(s) of values from the list without seeding
def random_subset(data):
    a = random.randint(0, len(data)+1)
    subset = random.choices(data, k=a)
    return subset

# Select n number(s) of values from the list with seeding
def random_subset_seeding(data):
    random.seed(5)
    a = random.randint(0,len(data)+1)
    subset = random.choices(data, k=a)
    return subset

class RandomNums:

    # List of random numbers
    data = []

    def __init__(self):
        pass

    # List of random number(s) with seeding
    for num in range(0, len(data)+1):
        random.seed(5)
        data.append(random_number(round(random.uniform(0.00,102.00), 2)))

    # Generates random number without seeding
    generate_num = random_number(random_number(round(random.uniform(0.00,102.00), 2)))

    # Generates random number with seeding
    random.seed(5)
    generate_number = random_number(random_number(round(random.uniform(0.00, 102.00), 2)))

    # Returns random value without seeding
    randomly_select = random_select(data)

    # Returns same random value with seeding
    random.seed(5)
    randomly_selected = random_select(data)