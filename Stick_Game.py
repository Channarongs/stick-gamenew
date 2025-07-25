#Input data and import function
name = input("Enter your name = ")
stick = int(input("How many stick in the pile = "))
time = 0
n = []
ai_pull = (1,2)
import numpy as np
random_turn = np.random.randint(1,3)


#Determine Function
def pull_AI():

    #AI pull stick in the pile by smart AI
    global stick
    if stick in n or stick - ai_pull[0] in n :
        stick = stick - ai_pull[0]
        ai_pullstick = print("I pull",ai_pull[0],"sticks. There are ",stick," sticks in the pile.")
    else :
        stick = stick - ai_pull[1]
        ai_pullstick = print("I pull",ai_pull[1],"sticks. There are ",stick," sticks in the pile.")


    #Checking stick in he pile
    if stick == 1 :
        print("Not bad",name,". Now you lose.")

    #return data
    return stick,ai_pullstick

#Player pull stick
def f(Pile_stick,Pick_stick,t_time) :
    #Pull stick and Calculate how many time you spent
    global stick
    global time
    stick = Pile_stick - Pick_stick
    time = t_time + 1
    f = print("There are ",stick," sticks in the pile.")
    
    #Checking stick in the pile
    if  stick == 1 :
        print("Good job",name,". Now I'm lose.")
    elif stick == 0 :
        print("Not bad",name,". Now you lose.")
    else :
        pull_AI()
    return stick,time,f


#Checking number that posible to pick and lose
for l_stick in range(1,stick,3) :
        n.append(l_stick)

#random turn
if random_turn == 1 :
    pull_AI()

#Checking condition for sticks in the pile
while stick > 1 :
    no_stick = int(input("How many stick do you want to pick? (1 or 2) = "))

    #How many sticks do you want to pick 1 or 2
    if 0 < no_stick <= 2 :
        if no_stick == 1 and stick > 0 :
            f(stick,no_stick,time)
        elif no_stick == 2 and stick > 1 :
            f(stick,no_stick,time)
        else :
            print("There are no enough sticks to pick.")

    #Checking Wrong condition
    elif no_stick <= 0 :
        print("You can't pick less than 1 stick.")
    else :
        print("You can't pick more than 2 sticks.")

#When stick in the pile has left
print("OK",name, "You spent", time , "time to take stick.")