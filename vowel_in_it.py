string = input()
count = 0
for i in string:
    if(i=='a' or i=='e' or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='U' or i=='O'):
        count = count + 1
if count > 0:
    print("yes")
else:
    print("no")
