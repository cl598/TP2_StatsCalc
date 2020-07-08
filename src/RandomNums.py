import random

# Random number
def random_number(a):
    return a

class RandomNums:

    def __init__(self):
        pass

    # Randomized number
    random_num = 0

    # Generates random number without seeding
    def generate_num(self):
        self.random_num = random_number(round(random.uniform(0.00, 102.00), 2))
        return self.random_num

    # Generates random number with seeding
    def generate_num_seed(self):
        random.seed(5)
        self.random_num = random_number(round(random.uniform(0.00, 102.00), 2))
        return self.random_num
