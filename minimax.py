import sys

arr = map(int, raw_input().strip().split(' '))
min_sum = sum(arr)
max_sum = 0
for x in range(len(arr)):
                max_sum = max((sum(arr) - arr[x]),max_sum)
                min_sum = min((sum(arr) - arr[x]),min_sum)

print min_sum, max_sum
                
