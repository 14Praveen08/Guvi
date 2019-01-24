c=0
check = int(input())
num1,num2 = map(int,input().split(" "))
while num1<=num2:
    if check == num1:
        print("yes")
        c=1
        break
    else:
            num1 = num1 + 1
if c==0:
    print("no")
