class Draw():
    def __init__(self,xLen,yLen):
        self.xLen = 6
        self.yLen = 6
        self.draw = []
        self.startBaton()

    def __refresh(self,x,y,i):
        S = 0
        for nearx in range(0,3):
            for neary in range(0,3):
                if not nearx == neary == 1:
                    try:
                        S += self.draw[i][x-1+nearx][y-1+neary]
                    except:
                        pass #si par exemple on est proche d'un bord, on évite le plantage lors de la lecture dans un index bidon
        rep = 0
        if self.draw[i][x][y]:
            if S == 2:
                rep = 1
        elif S == 3:
            rep = 1
        if S <2:
            rep = 0
        if S >3:
            rep = 0
        return rep

    def startBaton(self):
        self.draw.append([[0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 1, 1, 1], [0, 0, 1, 1, 1, 0], [0, 0, 0, 0, 0, 0]])
        #self.draw1 = [ [0 for y in range(self.yLen)] for x in range(self.xLen)]
        for n in range(0,self.xLen):
            print(self.draw[0][n])
        print("")
        self.i = 0

    def increment(self, increment):
        for i in range(self.i, self.i+ increment):
            self.draw.append([ [self.__refresh(x,y,self.i-1) for y in range(self.yLen)] for x in range(self.xLen)])
            for n in range(0,self.xLen):
                print(self.draw[i][n])
            print("")



MyDraw = Draw(6,6)
MyDraw.increment(10)
