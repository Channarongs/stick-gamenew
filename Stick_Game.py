#Input data and import function
name = input("Enter your name = ")
stick = int(input("How many stick in the pile = "))
time = 0
import numpy as np


#Determine Function
def pull_AI():
    #AI pull stick in the pile by random
    global stick
    random_stick = np.random.randint(1,3)
    stick = stick - random_stick
    ai_pullstick = print(" I pull",random_stick,"sticks. There are ",stick," sticks in the pile.")

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
