

board = [" " for x in range (10)]

def insertLetter(letter, pos):
    board[pos] = letter

def spaceIsFree(pos):
    return board[pos] == " "

def printBoard(board):
    print("   |   |   ")
    print(" " + board[1] + " | " + board[2] + " | " + board[3])
    print("   |   |   ")
    print("-----------")
    print("   |   |   ")
    print(" " + board[4] + " | " + board[5] + " | " + board[6])
    print("-----------")
    print("   |   |   ")
    print(" " + board[7] + " | " + board[8] + " | " + board[9])
    print("   |   |   ")

def isWinner(bo, le):
    return ((bo [7] == le and bo[8] == le and bo[9] == le) or 
            (bo [4] == le and bo[5] == le and bo[6] == le) or 
            (bo [1] == le and bo[2] == le and bo[3] == le) or
            (bo [1] == le and bo[4] == le and bo[7] == le) or
            (bo [2] == le and bo[5] == le and bo[8] == le) or 
            (bo [3] == le and bo[6] == le and bo[9] == le)) 

def playerMove():
    run = True
    while run:
        move = input("Choose your move! (1-9)")
        try:
            move = int(move)
            if move > 0 and move < 10:
                if spaceIsFree(move):
                    run = False
                    insertLetter("X",move)
                else:
                    print("Space is already occupied!")
            else:
                print("Enter a valid move!")
        except:
            print("Please type a number!")

def compMove():
    possibleMoves = [x for x, letter in enumerate(board) if letter == " " and x != 0]
    move = 0

    for let in ["O", "X"]:
        for i in possibleMoves:
            boardCopy = board[:]
            boardCopy[i] = let
            if isWinner(boardCopy,let):
                move = i
                return move
            
    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append[i]

def selectRandom(board):
    pass

def isBoardFull(board):
    if board.count(" ") > 1:
        return True
    else:
        return False

def main():
    print("Tic Tac Toe game")
    printBoard()

    while not(isBoardFull(board)):
        if not(isWinner(board,"O")):
            playerMove()
            printBoard()
        else:
            print("AI wins this time!")
            break
        if not(isWinner(board,"X")):
            move = compMove()
            if move == 0:
                print("Tie game!")
            else:
                insertLetter("O", board)
                print("Computer placed an \" O\" in postition", move, ":")
                printBoard()
        else:
            print("Congrats you won!")
            break

    if isBoardFull(board):
        print("Tie game!")