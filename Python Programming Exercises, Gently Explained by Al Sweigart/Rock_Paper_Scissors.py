"""
Rock, paper, scissors is a popular hand game for two players.
The two players simultaneously choose one of the three possible moves and determine the winner of the game: rock beats scissors, paper beats rock, and scissors beats paper.
This exercise involves determining a game’s outcome given the moves of the two players.
"""

def rpsWinner(player1,player2):
    if player1 == player2:
        return "tie"
    elif player1 == "rock":
        if player2 == "scissors":
            return "player one"
        else:
            return "player two"
    elif player1 == "paper":
        if player2 == "rock":
            return "player one"
        else:
            return "player two"
    elif player1 == "scissors":
        if player2 == "paper":
            return "player one"
        else:
            return "player two"
    

assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'