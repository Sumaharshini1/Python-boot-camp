my_list=list(map(int,input().split()))
n=(int(input("enter n")))
k=(int(int(input("enter k")))
if(len(my_list)<k+n):
    print("error")
else:
    for i in range(0,len(my_list)):
        print(my_list[k+n])
        break

