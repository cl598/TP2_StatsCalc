import random
import math
import statistics

#zScore function start


def zScore(data):
    #z = (x - mean)/standard deviation
    
    meanData = statistics.mean(data)
    SDPopulation = statistics.pstdev(data)
    
    zScores = []

    for x in data:
        zScore = (x - meanData)/ SDPopulation
        zScores.append(zScore)
        
    
    
    return zScores
#zScore function end

test = [12,46,23,87,43,91,74,88]


#Simple Random Sample function start
def simpleRandomSample(data):
    
    sample = []
    
    iterator = random.randint(1,len(data)-1)
    
    for x in range(len(data)):
        if x == 0:
            continue
        if x % iterator == 0:
            sample.append(x)
    print("Iterator " + str(iterator))
    return sample
#Simple Random Sample function end

#Margin of Error function start
def marginOfError(data):
    
    SDPopulation = statistics.pstdev(data)
    
    scores = zScore(data)
    
    #Margin Of Error (moe)
    moe = []
    
    for score in scores:
        MarginOfError =  score * SDPopulation / len(data)
        moe.append(MarginOfError)
    
    return moe
#Margin of Error function end

#Cochrans Sample Size formula function start

#Cochrans Sample Size formula function end

# Confidence interval for a sample start

def confInterval(data):
    xPlus = 0
    xMinus = 0
    confidence = []
    meanData = statistics.mean(data)
    SDPopulation = statistics.pstdev(data)
    zScores = zScore(data)
    for z_Score in zScores:
        xPlus = meanData + z_Score * SDPopulation/math.sqrt(len(data))
        xMinus = meanData - z_Score * SDPopulation/math.sqrt(len(data))
        confidence.append([xPlus,xMinus])
    
    
    return confidence
# Confidence interval for a sample start

