N, M = map(int, input().split())
left = 1
right = N

for i in range(M):
    a, b = map(int, input().split())
    left = max(left, a)
    right = min(right, b)

print(max(right - left + 1, 0))