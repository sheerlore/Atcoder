N, M = map(int, input().split())

ac = [0]*N
wa = [0]*N
cnt = 0
for i in range(M):
    n, s = input().split()
    n = int(n) - 1
    if ac[n] > 0:
        continue
    else:
        if s == "AC":
            ac[n] += 1
            cnt += wa[n]
        else:
            wa[n] += 1
            
print(sum(ac), cnt)
