from sys import stdin

n = int(stdin.readline().rstrip())
a = [int(x) for x in stdin.readline().rstrip().split()]

ans = 0
exist_odd = False

while(True):
    # 偶数判定
    for i in range(n):
        if(a[i] % 2 != 0):
            exist_odd = True
    # 奇数があれば抜ける
    if (exist_odd):
        break 
    # 全部偶数にする
    for j in range(n):
        a[j] /= 2
    # 操作回数を更新する
    ans += 1

print(ans)
    
    