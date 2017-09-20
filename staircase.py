import sys
n = int(raw_input().strip())
print '\n'.join((' ' * (n - i -1))+('#' * (i+1)) for i in range(n))
