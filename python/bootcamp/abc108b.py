import math

x1, y1, x2, y2 = map(int, input().split())

x, y = x2 - x1, y2 - y1
x4 = x*math.cos(math.pi / 2) - y*math.sin(math.pi / 2)
y4 = x*math.sin(math.pi / 2) + y*math.cos(math.pi / 2)

x3 = round(x2 + x4)
y3 = round(y2 + y4)
x4 = round(x1 + x4)
y4 = round(y1 + y4)

print(x3, y3, x4, y4)