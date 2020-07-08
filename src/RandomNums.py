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

    # Randomized number
    random_num = 0

    # Randomly selected number
    random_selected = 0

    # Random subset
    randomly_subset = []

    # List of random numbers
    data = []

    # List of random number(s) with seeding
    for num in range(0, len(data) + 1):
        random.seed(5)
        data.append(random_number(round(random.uniform(0.00, 102.00), 2)))

    # Generates random number without seeding
    def generate_num(self):
        self.random_num = random_number(round(random.uniform(0.00, 102.00), 2))
        return self.random_num

    # Generates random number with seeding
    def generate_num_seed(self):
        random.seed(5)
        self.random_num = random_number(round(random.uniform(0.00, 102.00), 2))
        return self.random_num

    # Returns random value without seeding
    def randomly_selected(self):
        self.random_selected = random_select(self.data)
        return self.random_selected

    # Returns same random value with seeding
    def randomly_selected_seed(self):
        random.seed(5)
        self.random_selected = random_select(self.data)
        return self.random_selected

    # Returns randomized subset from list without seeding
    def randomly_subset(self):
        self.randomly_subset.append(random_subset(self.data))
        return self.randomly_subset

    # Returns randomized subset from list with seeding
    def randomly_subset_seed(self):
        random.seed(5)
        self.randomly_subset.append(random_subset_seeding(self.data))
        return self.randomly_subset
