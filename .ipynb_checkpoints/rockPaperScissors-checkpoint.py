# Rock Paper Scissors game

import random, sys

# These variables keep track of number of wins, losses, and ties.
playerSelections = ('r', 'p', 's', 'q')

wins = 0
losses = 0
ties = 0
games = 0
lastWinner = ""
moves = {'r':'Rock', 'p': 'Paper', 's': 'Scissors'} 

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
    print(f"___Wins: {wins} -- Losses: {losses} -- Ties: {ties} ___")
    print(f"___Last Winner: {lastWinner} -- Games Played: {games}___")

    
    while True: # The player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit() # Quit the program
        
        # if playerMove != 'r' and playerMove != 'p' and playerMove != 's' and playerMove != 'q':
        if playerMove not in playerSelections: 
            print('Invalid selection! You lose 10 points!')
            wins -= 5
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


    # Display what the player chose:
    #if playerMove == 'r':   
    #    print('Rock versus...')
    #elif playerMove == 'p':
    #    print('PAPER versus...')
    #elif playerMove == 's':
    #    print('SCISSORS versus...')

    # Display what is being played by Player versus Computer
    print(f'Player chooses: {moves[playerMove]} while Computer choses:{moves[computerMove]}!')

    # Display and record the win/loss/tie:
    if playerMove == computerMove:
        print(f"It was a tie!")
        stalemate()

    elif playerMove == 'r' and computerMove == 's':
        print('Rock beats scissors! You win!')
        winner()
    elif playerMove == 'p' and computerMove == 'r':
        print('Paper beats rock! You win!')
        winner()
    elif playerMove == 's' and computerMove == 'p':
        print('Scissors beats paper! You win!')
        winner()
    elif playerMove == 'r' and computerMove == 'p':
        print('Paper beats rock! You lose!')
        loser()
    elif playerMove == 'p' and computerMove == 's':
        print('Scissors cut paper! You lose!')
        loser()
    elif playerMove == 's' and computerMove == 'r':
        print('Rock smashes Scissors! You lose so hard!')
        loser()

