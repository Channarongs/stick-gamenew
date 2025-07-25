#Input data and import function
import numpy as np
name = input("Enter your name = ")
stick = int(input("How many stick in the pile = "))
max_stick = int(input("How many stick can take in 1 time ? : "))
time = 0
lose_number = []
can_take = []
random_turn = np.random.randint(1,3)
ai_pull = 1


#Determine Function
def pull_AI():
    #AI pull stick in the pile by smart AI
    global stick

    #Checking the number
    for i in can_take :
        if stick - i in lose_number and i >= 1:
            ai_pull = i
    stick = stick - ai_pull
    ai_pullstick = print("I pull",ai_pull,"sticks. There are ",stick," sticks in the pile.")

    #Checking stick in he pile
    if stick == 1 :
        print("Not bad",name,". Now you lose.")

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

#Number of stick that can pick
for i in range(1,max_stick+1):
    can_take.append(i)

#Checking number that posible to pick and lose
for l_stick in range(1,stick,max_stick+1) :
        lose_number.append(l_stick)

#random turn
if random_turn == 1 :
    pull_AI()

#Checking condition for sticks in the pile
while stick > 1 :
    no_stick = int(input("How many stick do you want to pick? : "))

    #How many sticks do you want to pick 1 or 2
    if  no_stick in can_take :
        if no_stick in can_take and stick - no_stick > 0 :
            f(stick,no_stick,time)
        else :
            print("There are no enough sticks to pick.")

    #Checking Wrong condition
    elif no_stick < can_take[0] :
        print("You can't pick less than 1 stick.")
    else :
        print("You can't pick more than",max_stick,"sticks.")

#When stick in the pile has left
print("OK",name, ",nice try. You spent", time , "times to take sticks.")