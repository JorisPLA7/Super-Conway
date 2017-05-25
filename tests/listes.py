xLen = 6
yLen = 6



global draw
draw = []
def reverse(val):
    if val == True : return False
    if val == False : return True
    else : return '?'
def refresh(x,y,draw):
    S = 0
    for nearx in range(0,3):
        for neary in range(0,3):
            if not nearx == neary == 1:
                try:
                    S += draw1[x-1+nearx][y-1+neary]
                except:
                    pass
    print(S)
    return S
    #return reverse(draw1[x][y])



draw1 = [[True, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False], [False, False, False, False, False, False]]
#draw1 = [ [False for y in range(yLen)] for x in range(xLen)]
draw2 = [ [refresh(x,y,1) for y in range(yLen)] for x in range(xLen)]



print(draw1)
print('')
print(draw2)
