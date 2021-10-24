N, K, Q = map(int, input().split())
x = [0]*N

for i in range(Q):
    a = int(input())
    x[a - 1] += 1

cond = Q - K
for i in range(N):
    if x[i] > cond:
        print("Yes")
    else:
        print("No")





