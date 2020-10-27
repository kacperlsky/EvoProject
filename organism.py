import random

organisms = []
foods = []

class organism:
    def __init__(self, xposition, yposition, energy=100):
        self.xposition = xposition
        self.yposition = yposition
        self.energy = energy

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

###run 
initsim(100, 200, 2, 3)
print("ORGANISMS position x, position y, energy",[(o.xposition, o.yposition, o.energy) for o in organisms])
print("FOOD position x, position y",[(f.xposition, f.yposition) for f in foods])