import random
import math
import statistics
import scipy.stats as st
#zScore function start


def zScore(data):
    #z = (x - mean)/standard deviation
    zScores = st.zscore(data)
    return zScores
#zScore function end

test = [1,8,6,5,5,4,5,10]


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
    
    SDPopulation = st.tstd(data)
    
    scores = zScore(data)
    
    #Margin Of Error (moe)
    moe = []
    
    for score in scores:
        MarginOfError =  score * SDPopulation / math.sqrt(len(data))
        moe.append(MarginOfError)
    
    return moe
#Margin of Error function end

#Cochrans Sample Size formula function start
def cochSample(data):
    e = marginOfError(data)
    Z = zScore(data)
    ps = st.norm.cdf(Z)
    result = []
    
    for p in range(len(ps)):
        
        if ps[p] == 'nan':
            continue
        else:
    
            result.append(Z[p]**2 * ps[p]*(1-ps[p])/e[p]**2)
            
    return result

#Cochrans Sample Size formula function end

#def unknownPopSD(data):
    

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
print(marginOfError(test))