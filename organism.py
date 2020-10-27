import random
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

organisms = []
foods = []
NUMSTEP = 100
NUMGEN = 100

class organism:
    def __init__(self, xposition, yposition, energy=100):
        self.xposition = xposition
        self.yposition = yposition
        self.energy = energy

    def update(xposition, yposition, xdelta, ydelta):
        self.xposition = xposition
        self.yposition = yposition
        self.xdelta = xdelta
        self.ydelta = ydelta

class food:
    def __init__(self, xposition, yposition):
        self.xposition = xposition
        self.yposition = yposition

class world:
    def __init__(self, sizex=100, sizey=100):
        self.sizex = sizex
        self.sizey = sizey

    

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

def plotlo(sizex, sizey):
    fig, ax = plt.subplots()
    plt.xlim(0, sizex)
    plt.ylim(0, sizey)
    plt.title("Test")
    for org in organisms:
        orgcircle = Circle([org.xposition,org.yposition], 2, edgecolor = 'darkslateblue', facecolor = 'mediumslateblue', zorder=5)
        ax.add_artist(orgcircle)
        pass
    """
    circle = Circle([20,20], 2, edgecolor = 'darkslateblue', facecolor = 'mediumslateblue', zorder=5)
    circle2 = Circle([80,80], 2, edgecolor = 'darkslateblue', facecolor = 'mediumslateblue', zorder=5)
    circle3 = Circle([50,50], 25, edgecolor = 'darkslateblue', facecolor = 'mediumslateblue', zorder=5)
    
    ax.add_artist(circle)
    ax.add_artist(circle2)
    ax.add_artist(circle3)
    ax.set_aspect('equal')
    """
    plt.show()



#### 
def run(sizex, sizey, organismnum, foodnum):
    initsim(sizex, sizey, organismnum, foodnum)
    plotlo(sizex, sizey)
###run 


run(200, 200, 10, 10)
print("ORGANISMS position x, position y, energy",[(o.xposition, o.yposition, o.energy) for o in organisms])
print("FOOD position x, position y",[(f.xposition, f.yposition) for f in foods])
