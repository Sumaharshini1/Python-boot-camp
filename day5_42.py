#skipping 4 alphabets after selected alphabet and print the next element in capital letters
t=input()
n=int(input())
for i in t:
    print(chr(ord(i)+n))