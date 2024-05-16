import random
print("welome to anmol's gamming app")
top_of_range=input("enter the range:   ")
if top_of_range.isdigit():
    top_of_range=int(top_of_range)
    if top_of_range<=0:
        print("enter the higher value number next time")
        quit()
else:
    print("enter the number next time")
    quit()
random_num=random.randint(0,top_of_range)
guess=0

while True:
    guess+=1
    user_input=input('enter the guess:   ')
    if user_input.isdigit():
        user_input=int(user_input)
    else:
        print('enter a number nxt time')
        continue
    if user_input==random_num:
        print('yeah!! you got it')
        break
    elif user_input<random_num:
        print('try a number with higher value')
        
    else:
        print('try a number with lower value')
        
print("you got in " ,guess, "guess")
        
       
