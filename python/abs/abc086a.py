from sys import stdin

a, b = [int(x) for x in stdin.readline().rstrip().split()]

if ((a * b) % 2 == 0):
    print("Even")
else:
    print("Odd")