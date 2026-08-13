import random

number = random.randint(1, 100)
guess = int(input("Guess the number: "))

attemts = 1
while(True):
    
 if(guess>number):
    guess = int(input("Guess another number. this one is too big"))
    attemts +=1
 elif(guess<number):
    guess = int(input("Guess another number,this one is too less"))
    attemts +=1
 else:
    print(f"yeah thats the number! you guessed it right in {attemts} attems")
    break

































