import random


def robot_choice():
    
    #random number 
    random_number = random.randint(1,3)

    # dictornary with 3 values
    option = { 1: "rock", 2: "paper", 3:"scissors"}

    # get corresponding pick
    # 1 = rock, 2 = paper , 3 = scissors
    
    computer_choice = option[random_number]

    return computer_choice


def user_choice(user_choice):
    
    user_choice = input("Enter rock/paper/scissors: ")

    # lowering the string in small size

    user_choice = user_choice.lower()

    return user_choice

def win_or_loss(choice_robo , choice_user):

    if choice_robo == choice_user:
        return 'DRAW'
    
    # only for computer condition

    elif choice_robo == 'rock' and choice_user == 'scissors':
        return 'computer WINS'
    elif choice_robo == 'scissors' and choice_user == 'paper':
        return 'computer WINS'
    elif choice_robo == 'paper' and choice_user == 'rock':
        return 'computer WINS'
    
    # only for user 

    else:
        return 'User WINS'
    

def main():
    
    #until user gives correct input

    while True:
        choice_user = user_choice(user_choice)
        if choice_user in ['rock','paper', 'scissors']:
            print(f" You choose: {choice_user}")
            break


    choice_robo = robot_choice()
    print(f"Computer choose: {choice_robo}")


    decision = win_or_loss(choice_robo, choice_user)
    print(decision)



result  = main()
print(result)

