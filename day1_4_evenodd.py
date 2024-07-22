n=int(input("Enter a number\n"))
if(n>=0 and n%2==0):
    print("n is positive and even")
elif(n<=0 and n%2==0):
    print("n is negative and even")
elif(n>=0 and n%2==1):
    print("n is positive and odd")
else:
    print("negative and odd")
