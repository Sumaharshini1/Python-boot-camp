num1=int(input("Enter  number 1\n"))
num2=int(input("Enter number 2\n"))
a=num1+num2
b=num1-num2
c=num1*num2
print(a,b,c)

age=int(input("Enter the age\n"))
if(age>=18 and age<24):
    print("only two wheeler")
elif(age>=24 and age<45):
    print("two and four wheeler")
else:
    print("All")
