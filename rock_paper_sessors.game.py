import random
choices= ('r', 's', 'p') 
def get_user_choice(user_choices, computer):
    while True:
        user_choices= input("rock, paper, scissors? (r/p/s)")
        if user_choices not in choices:
            return user_choices
        else:
            print("invalid choice")

def display(user_choices, computer):
     while True:
        print(f"you chose {user_choices}")
        print(f"computer chose {computer}")

def case(user_choices, computer):
    while True:
            
        if (
            (user_choices=='r' and computer=='p')or
            (user_choices=='p' and computer=='s') or
            (user_choices=='s' and computer=='r')):
            print(f"you chose {user_choices}")
            print(f"computer chose {computer}")
            print("you lose")
        elif ((user_choices=='r' and computer=='s') or
            (user_choices=='p' and computer=='r')or 
            (user_choices=='s' and computer=='p')):
                print(f"you chose {user_choices}")
                print(f"computer chose {computer}")
                print("you lose")  
        elif user_choices==choices:
                print("tie")    
def play_game(user_choices, computer):
    while True:
         user_choices= get_user_choices()
         computer=random.choice(choices)
         display(user_choices, computer)
         case(user_choices, computer)
  

play_game()
        
