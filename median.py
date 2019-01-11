import statistics
med = 0
number = int(input())
set = list(map(int,input().split(" ")))
set.sort()
med = statistics.median(set)
print(med)
