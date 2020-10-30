import random
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

organisms = []
foods = []
NUMSTEP = 100
NUMGEN = 100

def distancecalc(x1, y1, x2, y2):
    result = sqrt((x2-x1)**2 + (y2-y1)**2)
    return result

class organism:
    def __init__(self, xposition, yposition, energy=100, food = None, xdelta = 0, ydelta = 0):
        self.xposition = xposition
        self.yposition = yposition
        self.energy = energy
        self.food = food
        self.xdelta = xdelta
        self.ydelta = ydelta

    """
    def updateorganism(xposition, yposition, xdelta, ydelta):
        self.xposition = xposition
        self.yposition = yposition
        self.xdelta = xdelta
        self.ydelta = ydelta
    """
    def updatexy(self, newx, newy):
        self.xposition = newx
        self.yposition = newy
    
    def updatedeltaxy(self, newdeltax, newdeltay):
        
        self.xdelta = newdeltax
        self.ydelta = newdeltay

    def updatefood(self, newfood):
        self.food = newfood
    
    def eat(self):
        self.energy = self.energy + 10

    def move(self):
        self.energy = self.energy - 1

class food:
    def __init__(self, xposition, yposition):
        self.xposition = xposition
        self.yposition = yposition

class world:
    def __init__(self, sizex=100, sizey=100):
        self.sizex = sizex
        self.sizey = sizey

    
def closeorfood(organism, foods):
    minx = 0
    miny = 0
    mindist = float('inf')
    minlist = []
    currentdist = 0
    for food in foods:
        currentdist = distancecalc(organism.xposition, organism.yposition, food.xposition, food.yposition)
        if mindist > currentdist:
            mindist = currentdist
            minx = food.xposition
            miny = food.yposition
    minlist.append(minx)
    minlist.append(miny)
    minlist.append(mindist)
    return minlist
#### init function
def initsim(sizex, sizey, organismnum, foodnum):
    for i in range(organismnum):
        org = organism(random.randint(0,sizex), random.randint(0,sizey), 100)
        organisms.append(org)
        i = i + 1
    for i in range(foodnum):
        fd = food(random.randint(0, sizex), random.randint(0, sizey))
        foods.append(fd)
        i = i + 1

def updateorg(organisms, xdelta, ydelta):
    for org in organisms:
        org.xposition = org.xposition + xdelta
        org.yposition = org.yposition + ydelta

def plotlo(sizex, sizey, i):
    fig, ax = plt.subplots()
    plt.xlim(0, sizex)
    plt.ylim(0, sizey)
    plt.title("Test")
    for org in organisms:
        orgcircle = Circle([org.xposition,org.yposition], 4, facecolor = 'darkgreen', zorder=10)
        ax.add_artist(orgcircle)
        orgedge = Circle([org.xposition,org.yposition], 8, facecolor='lightgreen', zorder=8)
        ax.add_artist(orgedge)
        pass
    ax.set_aspect('equal')
    for fdpoint in foods:
        fdcircle = Circle([fdpoint.xposition,fdpoint.yposition], 4, facecolor = 'blue', zorder=10)
        ax.add_artist(fdcircle)
    
    plt.savefig('img/'+str(i)+'DAY2.png', dpi=100)
    #plt.show() - useful but a bit annoying in the same time



#### 
def run(sizex, sizey, organismnum, foodnum, numgen = 10):
    initsim(sizex, sizey, organismnum, foodnum)
    """
    for i in range(numgen):
        plotlo(sizex, sizey, i)
        updateorg(organisms, 10, 5)
    """
    for orq in organisms:
        print(closeorfood(orq, foods))
###run 


run(1000, 1000, 10, 10)
print("FOOD position x, position y",[(f.xposition, f.yposition) for f in foods])
#print("ORGANISMS position x, position y, energy",[(o.xposition, o.yposition, o.energy) for o in organisms])
#print("FOOD position x, position y",[(f.xposition, f.yposition) for f in foods])
#or1 = organism(1,1)
#print(or1.xposition)
#or1.updatexy(555, 555)
#print("X:",or1.xposition)
#print("Y:",or1.yposition)
#print("Energy:", or1.energy)
#or1.move()
#print("Energy:", or1.energy)