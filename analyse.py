from univers import univers

from matplotlib import pyplot as plt
import pandas as pd
import random as ran
import matplotlib.gridspec as gridspec 
import threading
import time

global resultSet, universList, attributList, listAge, t
resultSet = pd.DataFrame()
universList = []
listAge=[] 
t=time.time()

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

    
def iteration():
    global resultSet, universList, attributList
    u, univParam = createRandomUnivers()
    universList.append(u)
    print('Started')
    runTime(u, 25000)
    
    attr = [getattr(u, att) for att in attributList]
    df = pd.DataFrame.from_records([attr], columns=attributList)
    df['univ']= u 
    
    resultSet = resultSet.append(df)
    resultSet.to_csv('result6.csv')
    
    print('Finish')

def launchUni():
    uni = 0
    for t in threading.enumerate():
        if "univers" in t.name:
            uni+=1
    if uni < 1:
        threading.Thread(target=iteration, name = 'univers'+str(len(universList))).start() 
    time.sleep(60)
     
def maxUni():
    while 1:
        launchUni()

def showInfo():
    global t, listAge
    listAgePast = listAge
    listAge     = [] 
    i           = 0
    t1          = t
    t           = time.time()
    tim         = t-t1
    print('Time since last check: {} min'.format(int(tim/60)))
    for u in universList:
        #if u.age != 25000 : 
        listAge.append(u.age)
        try:
            iterPerMin = (u.age-listAgePast[i])/tim*60
            timeRemain = (25000-u.age)/iterPerMin
        except:
            iterPerMin = 0
            timeRemain = 0
        msg = "age : {}".format(u.age) 
        msg += "\tmaxPop : {}".format(u.maxPop) 
        msg += "  \tscore : {}".format(u.score)
        msg += "\ttime remain : {} min".format(int(timeRemain))
        print(msg)
        i+=1

def graph(figsize = (9,4)):    
    plt.figure(dpi = 150)
    plt.figure(figsize = figsize)
    gs1 = gridspec.GridSpec(len(universList)//3 +1,3)
    gs1.update(wspace=0, hspace=0)
    for i in range(len(universList)):
        ax1 = plt.subplot(gs1[i])
        ax1.set_xticklabels([])
        ax1.set_yticklabels([])
        plt.imshow(universList[i].path_from_food + universList[i].path_from_home)
        plt.text(5, 10, "Score : " + str(universList[i].score), color = 'white')
        plt.text(5, 95, "Age : " + str(universList[i].age), color = 'white')

         
threading.Thread(target=maxUni, name = 'univLauncher').start()
fu,_ = createRandomUnivers()
attributList = [attr for attr in dir(fu) if not callable(getattr(fu, attr)) and not attr.startswith("__")]


# -----------------------------------------------------------
threading.enumerate()

showInfo()

graph((9,6))

resultSet = pd.DataFrame()
bypass = False
for u in universList:
    if u.age == 25000 or bypass == True: 
        attr = [getattr(u, att) for att in attributList]
        df = pd.DataFrame.from_records([attr], columns=attributList)
        df['univ']= u 
        resultSet = resultSet.append(df)
resultSet.to_csv('result6.csv')


df = pd.read_csv('result5.csv')
concat = pd.read_csv('resultConcat.csv')
