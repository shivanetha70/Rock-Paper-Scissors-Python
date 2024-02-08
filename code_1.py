import random

choices=['Rock','Paper','Scissor']
x=1

while x:

    print()
    print("1.Rock")
    print("2.Paper")
    print("3.Scissor")
    print("Select Option: ",end="")
    player_input=int(input())

    comp_choice=random.choice(choices)

    print()
    
    print("Computers Choice:",comp_choice)
    print("Players Choice:",choices[player_input-1])

    if choices[player_input-1]==comp_choice:
        print("TIE..!!")
    elif player_input==1 and comp_choice=='Paper':
        print("Computer win!!")
    elif player_input==1 and comp_choice=='Scissor':
        print("User Win!!")
    elif player_input==2 and comp_choice=="Rock":
        print("User win!!")
    elif player_input==2 and comp_choice=="Scissor":
        print("Computer win!!")
    elif player_input==3 and comp_choice=='Rock':
        print("Computer wins!!")
    elif player_input==3 and comp_choice=='Paper':
        print("User wins!!")
    

    print("Enter [n] to stop else enter any key to continue :")
    inp=input()

    if inp=='n':
        x=0
    else:
        continue
    

print("GAME OVER!!!!!!!!!!")



