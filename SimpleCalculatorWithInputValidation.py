#This is my first ever python project (Simple Calculator)
Num1=float(input("Enter the first number"))
Num2=float(input("Enter the second number"))

flag=1
while flag==1:     #Input validation
    choice=int(input("Enter 1 to add, 2 to subtract, 3 to multiply and 4 to divide"))
    if choice==1 or choice==2 or choice==3 or choice==4:
        flag=0
    else:
        print("That was not a valid choice! Please try again")

if choice==1:
    result=Num1+Num2
elif choice==2:
    result=Num1-Num2
elif choice==3:
    result=Num1*Num2
else:
    result=Num1/Num2

print("The answer is:",result)
