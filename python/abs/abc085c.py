n, y = map(int, input().split())
# n = a + b + c 
# c = n - a - b
# y = 10*a + 5*b + c 
y //= 1000
for a in range(n + 1):
    for b in range(n + 1):
        c = n - a - b
        if c < 0: break
        if (10*a+5*b+c) == y:
            print(a, b, c)
            exit()

print(-1, -1, -1)
