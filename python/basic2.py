"""
abc
s = input()

---------------------------

10
s = int(input())

---------------------------

abc def ghi
a, b, c = input().split()
str_list = list(input().split())

---------------------------

1 2 3
a, b, c = map(int, input().split())
num_list = list(map(int, input().split()))

---------------------------

3
aa
a
aaa
n = int(input())
str_list = [input() for _ in range(n)]

---------------------------

4
2
3
4
5
n = int(input())
num_list = [int(input()) for _ in range(n)]

---------------------------

3
aaa b cc
d ee fff
gg hhh i
n = int(input())
str_list = []
for i in range(n):
    str_list.append(list(input().split()))

または
n = int(input())
str_list = [list(input().split()) for _ in range(n)]

---------------------------

3
2 1 3
3 1 2 3
2 3 2
n = int(input())
num_list = []
for i in range(n):
    num_list.append(list(map(int, input().split())))

または
n = int(input())
num_list = [list(map(int, input().split())) for _ in range(n)]

"""