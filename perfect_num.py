import sys

def is_perfect(n):
    
    return sum ([i for i in range (2, n/2 + 1) if n % i == 0]) + 1 == n

for i in range(1, len(sys.argv)):
    print is_perfect (int(sys.argv[i]))

