#Input data
name = input("Enter your name = ")
stick = int(input("How many stick in the pile = "))
time = 0
value = [stick,time]


#Determine Function
def f(stick,no_stick,time) :
    value[0] = stick - no_stick
    value[1] = time + 1
    f = print("There are ",value[0]," sticks in the pile")
    return value[0],value[1],f


#Checking condition for sticks in the pile
while value[0] > 0:
    no_stick = int(input("How many stick do you want to pick? (1 or 2) = "))


    #How many sticks do you want to pick 1 or 2
    if 0 < no_stick <= 2 :
        if no_stick == 1 and value[0] > 0 :
            f(value[0],no_stick,value[1])
        elif no_stick == 2 and value[0] > 1 :
            f(value[0],no_stick,value[1])
        else :
            print("There are no enough sticks to pick.")

    #Checking Wrong condition
    elif no_stick <= 0 :
        print("You can't pick less than 1 stick.")
    else :
        print("You can't pick more than 2 sticks.")


#When stick in the pile has left
print("OK",name,", There is no stick left in the pile.", "You spent", value[1] ,
"time")
