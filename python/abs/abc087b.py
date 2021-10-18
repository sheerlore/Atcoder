from sys import stdin

a = int(stdin.readline().rstrip())
b = int(stdin.readline().rstrip())
c = int(stdin.readline().rstrip())
x = int(stdin.readline().rstrip())

res = 0
for a_i in range(a + 1):
    for b_i in range(b + 1):
        for c_i in range(c + 1):
            if ((500*a_i + 100*b_i + 50*c_i) == x):
                res += 1

print(res)