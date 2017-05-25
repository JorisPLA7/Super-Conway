xLen = 6
yLen = 6



global draw
draw = []
def reverse(val):
    if val == 1 : return 0
    if val == 0 : return 1
    else : return '?'
def refresh(x,y,i):
    S = 0
    for nearx in range(0,3):
        for neary in range(0,3):
            if not nearx == neary == 1:
                try:
                    S += draw[i][x-1+nearx][y-1+neary]
                except:
                    pass
    

    rep = 0
    if draw[i][x][y]:
        if S == 2:
            rep = 1
    elif S == 3:
        rep = 1
    if S <2:
        rep = 0
    if S >3:
        rep = 0
    return rep

    #return reverse(draw1[x][y])



draw.append([[0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 1, 1, 1, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0]])
#draw1 = [ [0 for y in range(yLen)] for x in range(xLen)]
for n in range(0,xLen):
    print(draw[0][n])
print("")
steps = 3
#steps = input("Nombre d'itérations: ")
for i in range(1,int(steps)+1):
    draw.append([ [refresh(x,y,i-1) for y in range(yLen)] for x in range(xLen)])
    for n in range(0,xLen):
        print(draw[i][n])
    print("")
