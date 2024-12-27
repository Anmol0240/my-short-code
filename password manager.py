
def add():
    name=(input("enter your name: "))
    pwd=input("enter the passsword: ")
    with open('password.txt', 'a') as g:
        g.write("name: "+name+"\n"+"password: "+pwd+"\n")

def view():
    
    with open('password.txt', 'r') as g:
        print("\nSaved passwords:")
        print(g.read())


mode=input("do you want to add a new password or view it or quit the process[add/view/q]").lower()
    
    
if mode=="add":
        add()
    
elif mode=="view":
        view()
    
    
elif mode=="q":
    exit(0)
else: 
    print("invalide operator")
    mode=input("do you want to add a new password or view it or quit the process[add/view/q]").lower()

    