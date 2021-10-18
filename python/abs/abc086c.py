from sys import stdin
n = int(stdin.readline().rstrip())
dt, dx, dy = 0, 0, 0
for i in range(n):
    t, x, y = map(int, stdin.readline().split())
    dist = abs(dx - x) + abs(dy - y)
    if t - dt < dist or ((x + y) % 2) != (t % 2):
        print("No")
        exit()
    dt, dx, dy = t, x, y

print("Yes")