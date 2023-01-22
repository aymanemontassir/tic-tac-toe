
def RowsWin(matrix,char):
    for i in range(0,3,1):
        winChar = 0
        for j in range(0,3,1):
            if matrix[i][j] == char:
                winChar += 1
                if winChar == 3:
                        return char + " wins"
    return "hfzffrzf"      
            
            
            

def columnsWin(matrix,char):
    for i in range(0,3,1):
        winChar = 0
        for j in range(0,3,1):
            if matrix[j][i] == char:
                winChar += 1
                if winChar == 3:
                    return char + " wins"
            
    return "hel" 

def diagonalWin(matrix,char):
    winChar = 0
    for i in range(0,3,1):
        if matrix[i][i] == char:
            winChar += 1
            if winChar == 3:
                return char + "wins"
    return "fr" 
    
def diagonalReverseWin(matrix, char):
    mid = len(matrix) // 2
    if matrix[0][ len(matrix)-1 ] == matrix[mid][mid] == matrix[ len(matrix)-1 ][0] == char:
        return char + " wins"
    return "hzfozzf"        
    
def isWinX(matrix):
    if RowsWin(matrix,'X') == "X wins" or diagonalReverseWin(matrix,'X') == "X wins" or diagonalWin(matrix,'X') == "X wins" or columnsWin(matrix,'X') == "X wins":
        return "X wins"
        
def isWinO(matrix):
    if RowsWin(matrix,'O') == "O wins" or diagonalReverseWin(matrix,'O') == "O wins" or diagonalWin(matrix,'O') == "O wins" or  columnsWin(matrix,'O') == "O wins":
        return "O wins"
        
def isWin(matrix):
    if (isWinX(matrix) == "X wins"  and isWinO(matrix) == "O wins"):
        return "Impossible"
    elif RowsWin(matrix,'X') == "X wins" or diagonalReverseWin(matrix,'X') == "X wins" or diagonalWin(matrix,'X') == "X wins" or columnsWin(matrix,'X') == "X wins":
        return "X wins"
    elif RowsWin(matrix,'O') == "O wins" or diagonalReverseWin(matrix,'O') == "O wins" or diagonalWin(matrix,'O') == "O wins" or  columnsWin(matrix,'O') == "O wins":
        return "O wins"    


            
def count(matrix, char):
    count = 0
    for array in matrix:
        for element in array:
            count += element.count(char)
    return count   
    
def isImpossible(matrix):
    if  (abs( count(matrix, 'X') - count(matrix, 'O') ) >= 2 ) or  (isWin(matrix) == "Impossible"):
        return "Impossible"
    return "hre"      
    
                
def isGameNotFinished(matrix):
    if count(matrix,'_') >= 1 and (isWin(matrix) != "X wins" and  isWin(matrix) != "O wins"):
        return "Game not finished"
    return "jfjzjfzp"       
            
    

def checkForDraw(matrix):
    count = 0
    for i in range(3):
        for j in range(3):
            if matrix[i][j] != " ":
                count += 1
    if count == 9 and isWin(matrix) != "X wins" and isWin(matrix) != "O wins":
        return "Draw"
        
def stateAnalyse(matrix):
    if isImpossible(matrix) != "Impossible":
        if isGameNotFinished(matrix) != "Game not finished":
            if isWin(matrix) == "X wins":
                return "X wins"
            elif isWin(matrix) == "Impossible":
                return "Impossible"
            elif isWin(matrix) == "O wins":
                return "O wins"
            else:
                if checkForDraw(matrix) == "Draw":
                    return "Draw"
        else:
            return "Game not finished"
    else:
        return "Impossible"    
    return None  
#print(isWinO(matrix))







            


  
 
 


             





def GetEmptyMatrix():
    matrix = [[" "]*3 for i in range(3)]
    return matrix 

matrix = GetEmptyMatrix()

def GetMatrix():
    xo_input = input()
    matrix = [[]*3 for i in range(3)]

    xo_combinaison = list(xo_input)
    s=0
# fill the matrix 
    for i in range(0,3,1):
        for j in range(0,3,1):
            matrix[i][j] = xo_combinaison[s]
            s = s + 1
    return matrix 


def printMatrix(matrix):

    print("---------")
    for i in range(0,3,1):
        print("| ",end='')
        for j in range(0,3,1):
            print(matrix[i][j] + " ",end='')
        print("|")
    print("---------")

def checkingCell(matrix,x,y):
    for i in range(0,3,1):
        for j in range(0,3,1):
            if matrix[x-1][y-1] == 'X' or matrix[x-1][y-1] == 'O':
                return "This cell is occupied! Choose another one!"
            
def moveX(matrix,x,y):
    matrix[x-1][y-1] = 'X'            

def checkingInput(input):

    if (len(input) > 3 and len(input) < 0):
        return "You should enter numbers!"
    
def checkingCoordinatesOutside(x,y):
    if (x < 1 or y < 1 ) or (x > 3 or y > 3): 
        return "Coordinates should be from 1 to 3!"



def check(matrix):

    while True:
        moveString = input()
        listString =  list(moveString.replace(' ',''))  # string to chars
        
        
        if checkingInput(listString) != "You should enter numbers!": # if it's correct
            try:
                intString = [int(ele) for ele in listString]
            except ValueError:
                print("You should enter numbers!")
                continue
            x = intString[0]
            y = intString[len(intString)-1]
            if checkingCoordinatesOutside(x,y) != "Coordinates should be from 1 to 3!":
                if  checkingCell(matrix,x,y) != "This cell is occupied! Choose another one!":
                    return [True,x,y]
                else:
                    print("This cell is occupied! Choose another one!")
            else:
                print("Coordinates should be from 1 to 3!")

        else:
            print("You should enter numbers!")

def move(matrix,x,y,c):
    matrix[x-1][y-1] = c
    
    
def switchRole(c):
    if c == 'X':
        return "O"
    else:
        return "X" 


def run(matrix):
    c = 'X'
    printMatrix(matrix)

    while True:
        outcome = stateAnalyse(matrix)
        if outcome == "X wins":
                print("X wins")
                break
        elif outcome == "O wins":
                print("O wins")
                break
        elif outcome == "Draw":
                print("Draw")
                break
        result = check(matrix)
        x = result[1]
        y = result[2]
        if result[0] == True:
            outcome = stateAnalyse(matrix)
            if outcome == "X wins":
                print("X wins")
                break
            elif outcome == "O wins":
                print("O wins")
                break
            elif outcome == "Draw":
                print("Draw")
                break
            else:
                move(matrix,x,y,c)
                c = switchRole(c) 
                printMatrix(matrix)

           




run(matrix)         








   



    


 
   

