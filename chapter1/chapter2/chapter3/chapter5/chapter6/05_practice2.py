m1= int(input("Enter the marks for sub 1:"))
m2= int(input("Enter the marks for sub 2:"))
m3= int(input("Enter the marks for sub 3:"))
m4= int(input("Enter the marks for sub 4:"))

overall = (m1+m2+m3+m4)/4


if(overall>=40):
    if(m1>=33 and m2>=33 and m3>=33 and m4>=33):
        print("you have passed the exam")
    else:
        print("You have passed the exam")
else:
    print("You have not passsed the exam")
