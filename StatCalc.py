import random
import math
import statistics
import scipy.stats as st

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

    def __init__(self):
        pass

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

# Z SCORE
def zScore(data):
    # z = (x - mean)/standard deviation
    zScores = st.zscore(data)
    return zScores


# SIMPLE RANDOM SAMPLE
def simpleRandomSample(data):
    sample = []

    iterator = random.randint(1, len(data) - 1)

    for x in range(len(data)):
        if x == 0:
            continue
        if x % iterator == 0:
            sample.append(x)
    print("Iterator " + str(iterator))
    return sample

# MARGIN OF ERROR
def marginOfError(data):
    scores = zScore(data)

    # Margin Of Error (moe)
    moe = []

    for score in scores:
        MarginOfError = score * standard_deviation(data) / math.sqrt(len(data))
        moe.append(MarginOfError)

    return moe

# COCHRANS SAMPLE SIZE
def cochSample(data):
    e = marginOfError(data)
    Z = zScore(data)
    ps = st.norm.cdf(Z)
    result = []

    for p in range(len(ps)):

        if ps[p] == 'nan':
            continue
        else:

            result.append(Z[p] ** 2 * ps[p] * (1 - ps[p]) / e[p] ** 2)

    return result

# CONFIDENCE INTERVAL
def confInterval(data):
    xPlus = 0
    xMinus = 0
    confidence = []
    zScores = zScore(data)
    for z_Score in zScores:
        xPlus = mean(data) + z_Score * standard_deviation(data) / math.sqrt(len(data))
        xMinus = mean(data) - z_Score * standard_deviation(data) / math.sqrt(len(data))
        confidence.append([xPlus, xMinus])

    return confidence

# MEAN
def mean(data):
    mean_value = statistics.mean(data)
    return mean_value

# MEDIAN
def median(data):
    median_value = statistics.median(data)
    return median_value

# MODE
def mode(data):
    mode_value = statistics.mode(data)
    return mode_value

# POPULATION STANDARD DEVIATION
def standard_deviation(data):
    sd_value = statistics.pstdev(data)
    return sd_value

# POPULATION VARIANCE
def variance(data):
    var_value = statistics.pvariance(data)
    return var_value