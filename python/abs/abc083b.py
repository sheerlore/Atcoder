from sys import stdin

def findSumOfDigits(n):
    sum = 0
    while (n > 0):
        sum += n % 10
        n //= 10
    return sum

n, a, b = [int(x) for x in stdin.readline().rstrip().split()]
total = 0
for i in range(1, n + 1):
    temp_sum = findSumOfDigits(i)
    if (temp_sum >= a and temp_sum <= b):
        total += i

print(total)