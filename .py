import random

def determineWinner(choiceOfPlayer, choiceOfComputer):
    if choiceOfPlayer == choiceOfComputer:
        return "It's a tie!"
    elif choiceOfPlayer == 'rock' and choiceOfComputer == 'scissors':
        return "You win!"
    elif choiceOfPlayer == 'paper' and choiceOfComputer == 'rock':
        return "You win!"
    elif choiceOfPlayer == 'scissors' and choiceOfComputer == 'paper':
        return "You win!"
    else:
        return "Computer wins!"

def playGame():
    print("Welcome to Rock, Paper, Scissors Game!")
    
    choices = ['rock', 'paper', 'scissors']

    while True:
        choiceOfPlayer = input("Enter your choice (rock, paper, scissors) or 'q' to quit: ").lower()
        
        if choiceOfPlayer == 'q':
            print("Thanks for playing")
            break
        
        if choiceOfPlayer not in choices:
            print("Invalid choice! Please enter rock, paper, or scissors.")
            continue

        choiceOfComputer = random.choice(choices)
        print("Computer's choice:", choiceOfComputer)
        
        result = determineWinner(choiceOfPlayer, choiceOfComputer)
        print(result)
    
        

playGame()
