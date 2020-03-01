# Rock Paper Scissors game

import random, sys, jsonpickle

# These variables keep track of number of wins, losses, and ties.
playerSelections = ('r', 'p', 's', 'q')
moves = {'r':'Rock', 'p': 'Paper', 's': 'Scissors'} 


class GameScore:
    def __init__(self, wins = 0, losses = 0, ties = 0, games = 0, lastWinner = ""):
        self.wins = wins
        self.losses = losses
        self.ties = ties
        self.games = games
        self.lastWinner = lastWinner
    
    def winner(self):
        self.wins += 1
        self.lastWinner = "Player!"
        self.games += 1
    def loser(self):
        self.losses += 1
        self.lastWinner = 'Computer'
        self.games += 1
    def stalemate(self):
        self.ties += 1
        self.lastWinner = 'Tie'
        self.games += 1
    

gs = GameScore()

def game_stats():
    with open('rps_results.json', 'w') as json_file:
        json_file.write(jsonpickle.encode(gs))


def winner():
    global wins
    wins += 1
    global lastWinner
    lastWinner = "Player!"
    global games
    games += 1

def loser():
    global losses
    losses += 1
    global lastWinner
    lastWinner = "Computer"
    global games
    games += 1
 
def stalemate():
    global ties 
    ties += 1
    global lastWinner
    lastWinner = "Tie"
    global games
    games += 1


print('---ROCK PAPER SCISSORS---')

while True: #The main game loop
    print(f"___Wins: {gs.wins} -- Losses: {gs.losses} -- Ties: {gs.ties} ___")
    print(f"___Last Winner: {gs.lastWinner} -- Games Played: {gs.games}___")

    
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            game_stats()
            sys.exit() # Quit the program
        
        # if playerMove != 'r' and playerMove != 'p' and playerMove != 's' and playerMove != 'q':
        if playerMove not in playerSelections: 
            print('Invalid selection! You lose 5 points!')
            gs.wins -= 5
            break
        if playerMove in playerSelections:
            break # Break out of the player input loop
        print('Type one of r, p, s, or q.')
        
    
    # Computer chosing a move
    randomNumber = random.randint(1,3)
    if randomNumber == 1: 
        computerMove = 'r'
        # print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        # print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        # print('SCISSORS')



    # Display what is being played by Player versus Computer
    print(f'Player chooses: {moves[playerMove]} while Computer choses:{moves[computerMove]}!')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print(f"It was a tie!")
        gs.stalemate()
    elif playerMove == 'r' and computerMove == 's':
        print('Rock beats scissors! You win!')
        gs.winner()
    elif playerMove == 'p' and computerMove == 'r':
        print('Paper beats rock! You win!')
        gs.winner()
    elif playerMove == 's' and computerMove == 'p':
        print('Scissors beats paper! You win!')
        gs.winner()
    elif playerMove == 'r' and computerMove == 'p':
        print('Paper beats rock! You lose!')
        gs.loser()
    elif playerMove == 'p' and computerMove == 's':
        print('Scissors cut paper! You lose!')
        gs.loser()
    elif playerMove == 's' and computerMove == 'r':
        print('Rock smashes Scissors! You lose so hard!')
        gs.loser()


