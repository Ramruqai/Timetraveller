def legal(positionX, positionY):
#legal for x =1
    if positionX == 1 and positionY == 1:
        legal_moves = "(N)orth"
    if positionX == 1 and positionY == 2:
        legal_moves = "(N)orth or (S)outh or (E)ast"
    if positionX == 1 and positionY == 3:
        legal_moves = "(S)outh or (E)ast"
#legal for x = 2
    if positionX == 2 and positionY == 1:
        legal_moves = "(S)outh or (W)est"
    if positionX == 2 and positionY == 2:
        legal_moves = "(N)orth or (S)outh or (E)ast"
    if positionX == 2 and positionY == 3:
        legal_moves = "(W)est or (E)ast"
#legal for x = 3
    if positionX == 3 and positionY == 1:
        legal_moves = "(N)orth"
    if positionX == 3 and positionY == 2:
        legal_moves = "(N)orth or (S)outh"
    if positionX == 3 and positionY == 3:
        legal_moves = "(W)est or (S)outh"
    return legal_moves

def check(position):
    MIN = 1
    MAX = 3
    if position < MIN:
        position = MIN
        print("Not a valid direction!")
    if position > MAX:
        position = MAX
        print("Not a valid direction!")
    return position

def check_error(position):
    MIN = 1
    MAX = 3
    if position < MIN:
        position = MIN
        return True
    elif position > MAX:
        position = MAX
        return True
    return False



positionX = 1
positionY = 1
legal_moves = ""

error = False


while True:
    if positionX == 3 and positionY == 1:
        break
    


    if error == False:
        print("You can travel:", end=" ")
        legal_moves = legal(positionX, positionY)
        print(legal_moves)
    
   
    move = input("Direction: ")
    move = move.lower()


    if move == "n":
        positionY += 1
        error = check_error(positionY)
        if error == True:
            positionY += 1
            positionY = check(positionY)
    elif move == "s":
        positionY -= 1
        error = check_error(positionY)
        if error == True:
            positionY -= 1
            positionY = check(positionY)

    elif move == "e":
        positionY += 1
        error = check_error(positionX)
        if error == True:
            positionX += 1
            positionX = check(positionX)

    elif move == "w":
        positionY -= 1
        error = check_error(positionX)
        if error == True:
            positionX -=1
            positionX = check(positionX)



print("Victory!")
