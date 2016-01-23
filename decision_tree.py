from math import log
import operator

def calcShannonEntropy(dataSet):
    numEntries = len(dataSet)
    labelCounts = {}
    for featureVector in dataSet:
        currentLabel = featureVector[-1]
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel] = 0
        labelCounts[currentLabel] += 1

    shannonEnt = 0.0

    for key in labelCounts:
        prob = float(labelCounts[key])/numEntries
        shannonEnt -= prob * log(prob,2)

    return shannonEnt

def createDataSet():
    dataSet = [ [1, 1, 'yes'],
                [1, 1, 'yes'],
                [1, 0, 'no'],
                [0, 1, 'no'],
                [0, 1, 'no']]
    labels = ['no surfacing', 'fliipers']
    return dataSet, labels

def splitDataSet(dataSet, axis, value):
    """
    Split dataSet by using the condition axis == value
    >>> myDat
    [[1, 1, 'yes'], [1, 1, 'yes'], [1, 0, 'no'], [0, 1, 'no'], [0, 1, 'no']]
    >>> trees.splitDataSet(myDat,0,1)
    [[1, 'yes'], [1, 'yes'], [0, 'no']]
    >>> trees.splitDataSet(myDat,0,0)
    [[1, 'no'], [1, 'no']]
    """
    returnDataSet = []
    for featureVector in dataSet:
        if featureVector[axis] == value:
            reducedFeatureVector = featureVector[:axis]
            reducedFeatureVector.extend(featureVector[axis+1:])
            returnDataSet.append(reducedFeatureVector)
    return returnDataSet

def chooseBestFeatureToSplit(dataSet):
    numFeatures = len(dataSet[0]) - 1
    baseEntropy = calcShannonEntropy(dataSet)
    bestInfoGain = 0.0
    bestFeature = -1

    for i in xrange(numFeatures):
        # Access the i-th column in each row in dataSet
        featureList = [example[i] for example in dataSet]
        uniqueVals = set(featureList)
        newEntropy = 0.0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet, i, value)
            prob = len(subDataSet)/float(len(dataSet))
            newEntropy += prob * calcShannonEntropy(subDataSet)
        infoGain = baseEntropy - newEntropy
        if( infoGain > bestInfoGain ):
            bestInfoGain = infoGain
            bestFeature = i
    
    return bestFeature

def majorityCount(classList):
    classCount = {}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote] = 0
        classCount[vote] += 1
    sortedClassCount = sorted(classCount.iteritems(),\
        key = operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree(dataSet, labels):
    classList = [example[-1] for example in dataSet]
    if classList.count(classList[0]) == len(classList):
        return classList[0]
    if len(dataSet[0]) == 1:
        return majorityCount(classList)
    bestFeature = chooseBestFeatureToSplit(dataSet)
    bestFeatureLabel = label[bestFeature]
    myTree = {bestFeatureLabel:{}}
    del(labels[bestFeature])
    featureValues = [example[bestFeature] for example in dataSet]
    uniqueValues = set(featureValues)

    for value in uniqueValues:
        subLabels = labels[:]
        myTree




if __name__ == "__main__":
    reload(decision_tree.py)
    myDat,labels = trees.createDataSet()
    print myDat