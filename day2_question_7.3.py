my_list=list(map(int,input().split()))
even=0
odd=0
for i in range(0,len(my_list)):
    if(my_list[i]%2==0):
        even+=1
        print("even")
    else:
        odd+=1 
        print("odd")