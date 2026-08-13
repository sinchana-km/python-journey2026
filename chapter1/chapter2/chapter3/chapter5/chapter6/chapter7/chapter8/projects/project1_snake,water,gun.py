import random
def swg(comp,mine):
    if(comp ==mine):
        return None
    if(comp =='snake' and mine=='gun'):
        return True
    elif(comp =='water' and mine =='snake'):
        return True
    elif(comp =='gun' and mine =='water'):
        return True
    else:
        return False
choice=('snake', 'water', 'gun')
comp = random.randint(0,2)
comp = choice[comp]
mine = input("choose either snake,water or gun: ")
    
win=swg(comp,mine)
print(f"you chose {mine} and the computer chose {comp} ")
if win is None:
    print("match drawn")
if win is True:
    print("you won")
else:
    print("you lose")
        
    