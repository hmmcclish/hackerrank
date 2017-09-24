n = int(raw_input().strip())
calories = map(int, raw_input().split())
calories.sort()
miles = 0
for x in range(n):
    miles += calories[-x-1] * 2**x
print miles
