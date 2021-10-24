N = int(input().rstrip())
h = list(map(int, input().split()))

r = 0
i = 0
c = 0
while i < N - 1:
    if h[i] >= h[i + 1]: c += 1
    else: c = 0
    i += 1
    r = max(c, r)

print(r)
