string = input()
str1 = string.lower()
list1 = []
c = 0
for i in str1:
    if i.isalpha():
        if i in list1:
            c = 1
        list1.append(i)
if c == 1:
    print("No")
else:
    print("Yes")
