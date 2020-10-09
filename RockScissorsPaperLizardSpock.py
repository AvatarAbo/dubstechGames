import random

# Define a set of variables to hold the valid moves
rock     = "Rock"
paper    = "Paper"
scissors = "Scissors"
lizard   = "Lizard"
spock    = "Spock"
cheat    = "Cheat"

# Default number of rounds
NUM_OF_RESPONSES = 3

# Now store the moves in a list
moves = [rock, paper, scissors, lizard, spock]
#moves2 = [rock, paper, scissors, lizard, spock, cheat] # uncomment to toggle Cheat
winmoves = {scissors:[paper,lizard], paper:[rock,spock], rock:[lizard,scissors], lizard:[spock,paper], spock:[scissors,rock], cheat:moves}

def main():
    user_input = input("Enter the number of rounds you want to play: ")
    print()
    play_times = NUM_OF_RESPONSES

    if user_input.isdigit() and int(user_input) < 100:
        # if the input was appropriate, override play_times
        play_times = int(user_input)
    else:
        # otherwise the play_times remains default
        print("Bad input. You will play", NUM_OF_RESPONSES, "times as default.")
        
    while play_times > 0:
        playermove = input("Enter your choice: "+", ".join(moves)+": ") # change to moves2 to use Cheat
        computermove = random.choice(moves)
        while playermove not in moves: # change to moves2 to use Cheat
            playermove = input("Bad input. Enter your choice: "+", ".join(moves)+": ") # change to moves2 to use Cheat
        print(findwinner(playermove,computermove))
        print()
        play_times -= 1
    
    print()
    print("Thanks for playing.")

def findwinner(playermove, computermove):
    print("You chose", playermove,", Computer chose", computermove, ".")
    
    if playermove == computermove:
        return "Draw!"
    elif computermove in winmoves[playermove]:
        return "Player wins!"
    return "Computer wins!"

main()
    