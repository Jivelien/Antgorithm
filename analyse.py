from univers import univers
from matplotlib import pyplot as plt
import pandas as pd
import random as ran
import matplotlib.gridspec as gridspec 
import threading

global resultSet, universList, attributList
resultSet = pd.DataFrame()
universList = []

def createRandomUnivers():
    universY=100
    universX=int(universY*16/9)
    univParam = {'uniY' : universY, 
                 'uniX' : universX, 
                 'population' : ran.randrange(100,5000), 
                 'exhaust' : ran.randrange(1000,10000), 
                 'stepWeight' : ran.randrange(10,255), 
                 'weightLostByStep' : ran.randrange(1,10),
                 'lostEachEpoch' : ran.randrange(1,10),
                 'lostPower' : ran.randrange(1,10)}

    u = univers(**univParam)
    u.food.y = 25
    u.food.x = 45
    return u, univParam

def runTime(u : univers, epoch : int):
    for i in range(epoch):
        u.applyTime()

def getResult(u, univParam):
    attr = [getattr(u, att) for att in attributList]
    df = pd.DataFrame.from_records([attr], columns=attributList)
    df['univ']= u 
    return df
    
def iteration():
    global resultSet, universList
    u, univParam = createRandomUnivers()
    universList.append(u)
    print('Started')
    runTime(u, 25000)
    result = getResult(u, univParam)
    resultSet = resultSet.append(result)
    resultSet.to_csv('result.csv')
    print('Finish')

def launchUni():
    uni = 0
    for t in threading.enumerate():
        if "univers" in t.name:
            uni+=1
    if uni < 0:
        threading.Thread(target=iteration, name = 'univers'+str(len(universList))).start() 
            
def maxUni():
    while 1:
        launchUni()

            
threading.Thread(target=maxUni, name = 'univLauncher').start()


# -----------------------------------------------------------
fu,_ = createRandomUnivers()
attributList = [attr for attr in dir(fu) if not callable(getattr(fu, attr)) and not attr.startswith("__")]

threading.enumerate()
threading.active_count()

listAge=[] 
for u in universList:
    if u.age != 25000 : 
        listAge.append(u.age)
        print("age : " + str(u.age) + '\t - maxPop : ' +str(u.maxPop) + "   \t - score : " + str(u.score))
  


plt.figure(dpi = 150)
plt.figure(figsize = (9,12))
gs1 = gridspec.GridSpec(len(universList)//3 +1,3)
gs1.update(wspace=0, hspace=0)
for i in range(len(universList)):
    ax1 = plt.subplot(gs1[i])
    ax1.set_xticklabels([])
    ax1.set_yticklabels([])
    fig = plt.imshow(universList[i].path_from_food + universList[i].path_from_home)
 
    
resultSet = pd.DataFrame()
bypass = True
for u in universList:
    if u.age == 25000 or bypass == True: 
        attr = [getattr(u, att) for att in attributList]
        df = pd.DataFrame.from_records([attr], columns=attributList)
        df['univ']= u 
        resultSet = resultSet.append(df)

resultSet.to_csv('result.csv')
