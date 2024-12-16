import random
user_wins=0
computer_wins=0
options=["rock","paper","scissors"]

while True:
    user_pick=input("enter rock\paper\scissor or Q to quit:  ").lower()
    if user_pick=="q":
        break
    if user_pick not in options:
        print("enter the correct options")
        continue
    random_number=random.randint(0,2)
    computer_pick=options[random_number]
    
    print("computer picked",computer_pick+".")
    if user_pick=="rock" and computer_pick=="scissors":
        print("you won!!")
        user_wins+=1
        
    elif user_pick=="paper" and computer_pick=="rock":
        print("you won!!")
        user_wins+=1
        
    elif user_pick=="scissors" and computer_pick=="paper":
        print("you won!!")
        user_wins+=1

    elif user_pick==computer_pick:
        print("nice try!! it was a draw")

    else:
        print("you lost")
        computer_wins+=1

print('good bye!!')
print("computer won",computer_wins,"times.")
print("you won",user_wins,"times.")

user_total=(user_wins+computer_wins)
print("win rate is",str(user_wins/(user_total)*100),"percent")

