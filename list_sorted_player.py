lim = int(input())
count = 0
numbers = list(map(int,input().split(" ")))
for i in range(0,len(numbers)):
    if i != len(numbers)-1:
        if numbers[i] >= numbers[i+1]:
            count=count+1
            print("no");
            break;
if count == 0:
    print("yes")
