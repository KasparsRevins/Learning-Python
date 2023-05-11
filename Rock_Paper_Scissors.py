"""
Rock, paper, scissors is a popular hand game for two players.
The two players simultaneously choose one of the three possible moves and determine the winner of the game: rock beats scissors, paper beats rock, and scissors beats paper.
This exercise involves determining a game’s outcome given the moves of the two players.
"""

def rpsWinner(player1,player2):
    if player1 == player2:
        return "tie"
    
    if player1 == "rock" and player2 == "paper" or player1 == "paper" and player2 == "scissors" or player1 == "scissors" and player2 == "rock":
        return "player two"
    
    if player1 == "rock" and player2 == "scissors" or player2 == "paper" and player1 == "scissors" or player2 == "scissors" and player1 == "rock" or player2 == "rock" and player1 == "paper":
        return "player one"
    

assert rpsWinner('rock', 'paper') == 'player two'

assert rpsWinner('rock', 'scissors') == 'player one'

assert rpsWinner('paper', 'scissors') == 'player two'

assert rpsWinner('paper', 'rock') == 'player one'

assert rpsWinner('scissors', 'rock') == 'player two'

assert rpsWinner('scissors', 'paper') == 'player one'

assert rpsWinner('rock', 'rock') == 'tie'

assert rpsWinner('paper', 'paper') == 'tie'

assert rpsWinner('scissors', 'scissors') == 'tie'