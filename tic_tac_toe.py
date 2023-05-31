

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
            compMove()
            printBoard()
        else:
            print("Congrats you won!")
            break

    if isBoardFull(board):
        print("Tie game!")