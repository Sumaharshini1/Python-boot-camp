my_list=list(map(str,input().split(",")))
choice=int(input())
print("enter the choice 1.append\n 2.pop\n 3.sort\n 4.length\n")
if(choice==1):
    my_list.append(9)
    print(my_list)
elif(choice==2):
    my_list.pop(2)
    print(my_list)
elif(choice==3):
    my_list.sort()
    print(my_list)
else:
    print(my_list)

