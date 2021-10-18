from sys import stdin

a = int(stdin.readline().rstrip())
b, c = [int(x) for x in stdin.readline().rstrip().split()]
s = stdin.readline().rstrip()

print("{} {}".format(a + b + c, s))