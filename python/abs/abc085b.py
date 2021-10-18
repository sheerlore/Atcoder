from sys import stdin

N = int(input())
value = [int(input()) for _ in range(N)]
print(len(set(value)))