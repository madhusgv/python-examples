import random
import rpsconst

print("Welcome  to rock, paper, scissors Game!")

#Write your code below this line 👇
while(1):

    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors or 3 for exit. : "))
    if user_input == 3:
        break
    
    print("Your choice is: ")
    if user_input == rpsconst.ROCK:
        print(rpsconst.rock)
    elif user_input == rpsconst.PAPER:
        print(rpsconst.paper)
    elif user_input == rpsconst.SCISSORS:
        print(rpsconst.scissors)

    computer_choice = random.randint(0,2)

    print("Computer choice is: ")
    if computer_choice == rpsconst.ROCK:
        print(rpsconst.rock)
    elif computer_choice == rpsconst.PAPER:
        print(rpsconst.paper)
    elif computer_choice == rpsconst.SCISSORS:
        print(rpsconst.scissors)


    if (user_input  ==  rpsconst.ROCK):
        if computer_choice == rpsconst.ROCK:
            print("It\'s a draw")
        elif computer_choice == rpsconst.PAPER:
            print("Ohh! Computer Wins!")
        else:
            print("Very Nice! You Win!")

    elif (user_input  ==  rpsconst.PAPER):
        if computer_choice == rpsconst.ROCK:
            print("Very Nice! You Win!")
        elif computer_choice == rpsconst.PAPER:
            print("It\'s a draw")
        else:
            print("Ohh! Computer Wins!")

    elif (user_input  ==  rpsconst.SCISSORS):
        if computer_choice == rpsconst.ROCK:
            print("Ohh! Computer Wins!")
            
        elif computer_choice == rpsconst.PAPER:
            print("Very Nice! You Win!")
            
        else:
            print("It\'s a draw")
    else:
        print("Try Again!")
