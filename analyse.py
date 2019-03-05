from univers import univers
from matplotlib import pyplot as plt
import pandas as pd
import random as ran

import threading

global resultSet
resultSet = pd.DataFrame()

def createRandomUnivers():
    universY=100
    universX=int(universY*16/9)
    univParam = {'uniY' : universY, 
                 'uniX' : universX, 
                 'population' : ran.randrange(1,5000), 
                 'exhaust' : ran.randrange(1000,10000), 
                 'stepWeight' : ran.randrange(10,255), 
                 'weightLostByStep' : ran.randrange(1,10),
                 'lostEachEpoch' : ran.randrange(1,10),
                 'lostPower' : ran.randrange(1,10)}

    return univers(**univParam), univParam

def runTime(u : univers, epoch : int):
    for i in range(epoch):
        u.applyTime()

def getResult(u, univParam):
    univParam['score'] = u.score
    univParam['univ'] = u
    row = pd.DataFrame(univParam, index=[0])
    return row
    
def iteration():
    global resultSet
    u, univParam = createRandomUnivers()
    runTime(u, 10000)
    result = getResult(u, univParam)
    resultSet = resultSet.append(result, sort=False)
    resultSet.to_csv('result.csv')
    print('finish')


for i in range(20):  
    threading.Thread(target=iteration).start() 
