import random

# Global variables
Game = ""
Score = 0
LastPlayerChoice = ""  

# Colors for the text
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

# Define the win conditions for both games
WIN_CONDITIONS = {
    'RPS': {
        'rock': ['scissors'],
        'paper': ['rock'],
        'scissors': ['paper']
    },
    'RPSLS': {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['paper', 'spock'],
        'spock': ['rock', 'scissors']
    }
}

# Game type selection
def Game_type_selection():
    global Game  
    print(f"{bcolors.HEADER}Enter the game type:{bcolors.ENDC} \n 1.RPS=(Rock, Paper, Scissors) \n 2.RPSLS=(Rock, Paper, Scissors, Lizard, Spock) \n 3.EXIT to exit the game")
    GameType = input()
    if GameType == "RPS" or GameType == "rps" or GameType == "1":
        Game = "RPS"
        CPU_version()
    elif GameType == "RPSLS" or GameType == "rpsls" or GameType == "2":
        Game = "RPSLS"
        CPU_version()
    elif GameType == "EXIT" or GameType == "exit" or GameType == "3":
        exit()
    else:
        print(f"{bcolors.WARNING}Invalid game type, Please enter a valid game type: 'RPS'=(Rock, Paper, Scissors) or 'RPSLS'(Rock, Paper, Scissors, Lizard, Spock) or 'EXIT' to exit the game{bcolors.ENDC}")
        Game_type_selection()

# CPU version selection
def CPU_version():
    print(f"\n{bcolors.HEADER}Choose the CPU version...{bcolors.ENDC}\n 1.Do you want the computer to randomly select the choice? Type '1' \n 2.Do you want the CPU to use your previous choice? Type '2' \n 3.EXIT to exit the game")
    computer_settings = input()
    if computer_settings == "1":
        print("Computer will randomly select the choice")
        player_choice(computer_settings)
    elif computer_settings == "2":
        print("Computer will use your previous choice")
        player_choice(computer_settings)
    elif computer_settings == "EXIT" or computer_settings == "exit" or computer_settings == "3":
        exit()
    else:
        print(f"{bcolors.WARNING}Invalid CPU version, Please enter a valid CPU version: \n'1'=(Computer randomly selects the choice) or \n'2'=(Computer uses your previous choice) or \n'EXIT' to exit the game{bcolors.ENDC}")
        CPU_version()

# Determine the outcome
def determine_winner(game_type, player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'draw'
    elif computer_choice in WIN_CONDITIONS[game_type][player_choice]:
        return 'win'
    else:
        return 'lose'

# Rock, Paper, Scissors version
def RPS_version(computer_settings):
    global LastPlayerChoice
    player_choice = input(f"\n{bcolors.HEADER}Enter your choice: {bcolors.ENDC}rock, paper, scissors: or 'EXIT' to exit the game\n")
    if player_choice == "EXIT" or player_choice == "exit":
        exit()
    elif player_choice not in WIN_CONDITIONS[Game]:
        print(f"{bcolors.WARNING}\nInvalid choice, Please enter a valid choice: rock, paper, scissors or 'EXIT' to exit the game\n")
        RPS_version(computer_settings)
    if computer_settings == "1":
        computer_choice = random.choice(list(WIN_CONDITIONS[Game].keys()))
    elif computer_settings == "2":
        if LastPlayerChoice == "":
            computer_choice = random.choice(list(WIN_CONDITIONS[Game].keys()))
        else:
            computer_choice = LastPlayerChoice
    
    LastPlayerChoice = player_choice  
    
    result = determine_winner(Game, player_choice, computer_choice)
    if result == "win":
        global Score
        Score += 1
    elif result == "lose":
        Score -= 1
    else:
        Score += 0.5
    print(f"{bcolors.OKBLUE}\nPlayer choice: {player_choice}, Computer choice: {computer_choice}, Result: {result} \nScore: {Score}\n{bcolors.ENDC}")
    RPS_version(computer_settings)

# Rock, Paper, Scissors, Lizard, Spock version
def RPSLS_version(computer_settings):
    global LastPlayerChoice
    player_choice = input(f"\n{bcolors.HEADER}Enter your choice: {bcolors.ENDC}rock, paper, scissors, lizard, spock: or 'EXIT' to exit the game\n")
    if player_choice == "EXIT" or player_choice == "exit":
        exit()
    elif player_choice not in WIN_CONDITIONS[Game]:
        print(f"{bcolors.WARNING}\nInvalid choice, Please enter a valid choice: rock, paper, scissors, lizard, spock or 'EXIT' to exit the game")
        RPSLS_version(computer_settings)
    if computer_settings == "1":
        computer_choice = random.choice(list(WIN_CONDITIONS[Game].keys()))
    elif computer_settings == "2":
        if LastPlayerChoice == "":
            computer_choice = random.choice(list(WIN_CONDITIONS[Game].keys()))
        else:
            computer_choice = LastPlayerChoice
    
    LastPlayerChoice = player_choice  
    
    result = determine_winner(Game, player_choice, computer_choice)
    if result == "win":
        global Score
        Score += 1
    elif result == "lose":
        Score -= 1
    else:
        Score += 0.5
    print(f"{bcolors.OKBLUE}\nPlayer choice: {player_choice}, Computer choice: {computer_choice}, Result: {result} \nScore: {Score}\n{bcolors.ENDC}")
    RPSLS_version(computer_settings)

# Player choice
def player_choice(computer_settings):
    global Game 
    if Game == "RPS":
        RPS_version(computer_settings)
    elif Game == "RPSLS":
        RPSLS_version(computer_settings)
    else:
        print(f"{bcolors.WARNING}Invalid game type, Please enter a valid game type: 'RPS'=(Rock, Paper, Scissors) or 'RPSLS'(Rock, Paper, Scissors, Lizard, Spock) or 'EXIT' to exit the game{bcolors.ENDC}")
        Game_type_selection()

# Main function starting with the game type selection
def main():
    Game_type_selection()

main()
