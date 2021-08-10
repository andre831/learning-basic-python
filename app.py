# -*- coding: utf-8 -*-
#imports
from time import sleep

#
print("Hi, welcome to Uber")

print(' ' * 20)

#Persons
car = ["driver"]
you = {'Name': 'Pedro', 'wallet': 100} 


print('Currently in our car we have:',  car  , 'do you want to come in?')

# enter in car
option = 0

#run car
contage= 0 #kilocimetro
km = 0     #km rodado
wallet = 100
finalPoint = 30

def finishRun():
    wallet = 100
    finalPoint = 30
    moneyBack = wallet - finalPoint
    print('Value:', finalPoint)
    print('Money back:', moneyBack)

while option <= 1:
    print(' ' * 20)
    print("[1] no or [2]yes")
    option = int(input("Uber: - You?"))

    if option == 1:
        print("Okay! Bye.")
        break
    elif option == 2:
        print("YOU ARE IN THE CAR")
        car.append(you)
        print(' ' * 20) 
        print(car)
        print("Let's go")
        sleep(2) 
        
        #in car and run car
        while option == 2:
            contage += 2
            km += 0.5
            sleep(.20)
            print("km:", km)
            print("aceleration:", contage)
            if contage == 80: #high speed
                contage -= 20
                print("desacelaration:", contage)
            if km == 25:
                print(' ' * 20)
                print("okay, your point is here!")
                print(' ' * 20)
                finishRun()
                break