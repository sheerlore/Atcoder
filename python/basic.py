# 基本的な入出力

from sys import stdin
from copy import deepcopy
import string

# a = stdin.readline().rstrip()
# print(a.upper())

# インタラクティブな問題の場合、出力時にflushする必要があるが、print関数のオプションで指定できる
# print('spam', flush=True)

# 入力値の簡単なデータ操作
# 数値への変換
# n = int(stdin.readline().rstrip())

# 空白で分割
# リストで返る
# l = stdin.readline().rstrip().split()
# アンバック代入（それぞれの変数に入力される
# A, B, C = stdin.readline().rstrip().split()
# print(l)
# print(A, B, C)

# 空白で分割しつつ数値に変換
# 上の二つの合わせ方「リスト内包表記」を使うと１行でかける
# A, B, C = [int(x) for x in stdin.readline().rstrip().split()]
# print(A + B - C)

# リスト内包表記
# 特定の条件のデータを数える
# リスト内からある条件を満たす要素の個数をカウントする時もリスト内表記が使える。
# data = range(1, 10)
# count = len([x for x in data if x % 3 == 0])
# print(count)

# 複数行をまとめて読み込む
# n = int(stdin.readline().rstrip())
# data = [stdin.readline().rstrip().split() for _ in range(n)]
# print(data) # 一行
# print(*data, sep='\n') # マトリクスをそのまま表示
# リストのオブジェクトに * をつけて引数に渡すと分解されるのを利用している。
# seqオプションに改行文字を指定することで、分割して渡したデータを改行しながら表示する

# 二重のリストの行列を入れ替える
# マトリクス状のデータを横方向（行）だけでなく縦方向（列）にも操作したいときは、行列の転置を行うと操作しやすい
# zip を使ってリスト内包表記を使って解決する
# data = [[1,2,3], [4,5,6], [7,8,9]]
# print(data)

# transpose = [x for x in zip(*data)]
# print(transpose)
# 列ごとの和を求めたい時はこうする
# print([sum(x) for x in zip(*data)])

# 二重のリストをフラットにする
# マトリクス状のデータを１行の単純なリストに平坦化する時もリスト内包表記が使える
# data = [[1,2,3], [4,5,6], [7,8,9]]
# print(data)
# flat = [flatten for inner in data for flatten in inner]
# print(flat)
# sum()を使ってフラットなリストを作ることもできる
# print(sum(data, []))

# リストの操作
# 連結と繰り返し
# a = [1, 2, 3] + [4, 5]
# print(a)
# b = [1, 2, 3] * 3
# print(b)

# 要素の存在確認
# a = [1, 2, 3, 4, 5]
# print(1 in a)
# print(6 in a)

# 削除
# a = [1, 2, 3, 4, 5]
# del a[1]
# print(a)

# b = [1, 2, 3, 4, 5]
# del b[1:3]
# print(b)

# c = [1, 2, 3, 4, 5]
# x = c.pop(1)
# print(c, x)

# d = [1, 2, 3, 4, 5]
# d.remove(3)
# print(d)

# ソート
# もとのリスト自体を書き換えて破壊的にソートするsort()メソッドと
# ソートした結果のリストを別途生成して返すsorted()関数がある

# a = [2, 5, 1, 4, 3]
# b = sorted(a)
# print(a)
# print(b)

# a.sort()
# print(a, b)

# 降順にソートしたい場合
# c = sorted(a, reverse=True)
# print(c)

# keyオプションによって比較を行う前にリストの各要素に対して呼び出される関数を指定することで
# 柔軟なソートが可能になる
# a = ['e', 'B', 'd', 'C', 'a']
# print(sorted(a)) #大文字と小文字それぞれでソートされる
# print(sorted(a, key=lambda x: x.upper()))  #比較時に大文字にするので、大文字小文字併せてソートされる

# 多重キーでのソート
# 内部のタプルの1要素目（アルファベット）、2要素目（数字）、0要素目（数値）の順に比較してソートを行う
# a = [(1, 'One', '1'), (1, 'One', '01'),
#      (2, 'Two', '2'), (2, 'Two', '02'),
#      (3, 'Three', '3'), (3, 'Three', '03')]
# print(sorted(a, key=lambda x: (x[1], x[2], x[0])))

# マイナス値のインデックス
# インデックスを指定してアクセスするときにマイナス値を使うことができる
# マイナスを使うと末尾から数えられ、-1が末尾になる
# a = [1, 2, 3, 4, 5]
# print(a[len(a) - 1])
# print(a[-1])
# print(a[-2])

# 部分リストの取り出し（スライス）
# [始点:終点]
# 取得できるのは「始点以上終点未満」
# 始点と終点は省略可能
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a[3:7])
# print(a[3:])
# print(a[:7])
# ステップを指定することも可能
# print(a[2:8:2])
# print(a[6:1:-2])

# シャローコピーとディープコピー
# copyモジュールが使用できるがスライスを使って簡単に書くことができる
# a = [1, 2, 3, 4, 5]
# b = a[:]
# b[0] *= 10  # bはaのコピーなのでaには影響はない
# print(a)
# print(b)

# 多重リストをこの方法でコピーすると、単純なシャローコピーになるので思わぬ副作用が出る
# a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# b = a[:]
# b[0].append(0)
# print(a)
# print(b)
# 防ぐにはcopy.deepcopyを使ってディープコピーをする
# c = deepcopy(a)
# c[0].append(0)
# print(a)
# print(c)

# 和集合と積集合
# 二つのリストで少なくとも片方に含まれているものを集めたものが和集合、
# 両方とも入っているものを集めたものが積集合
# リストとセットの変換はlist()とset()を使って行う
# a = [2, 4, 6, 8]
# b = [3, 6, 9]

# print(list(set(a) | set(b)))
# print(list(set(a) & set(b)))

# 文字列操作
# リストと同じ操作
# a = 'ABC' + 'DEF'
# print(a)
# b = 'ABC' * 3
# print(b)
# c = 'ABCDEF'
# print('A' in c)
# print('a' in c)

# 置換
# a = 'abc(de)fg'
# print(a.replace('(', '[').replace(')', ']'))

# b = 'aBCdEfg'
# print(b.upper())
# print(b.lower())

# 文字列の反転
# s = 'ABCDEFG'
# print(s[::-1])

# 文字列定数
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)
# print(string.ascii_letters)
# print(string.digits)
# print(string.hexdigits)

# 正規表現
# import re
# text = '<h1 style="width: 100px; height: 200px;">'
# result = re.search(r'width: (\d*)px; height: (\d*)px;', text)
# print(result)

# if result:
#     print(result.group(0))
#     print(result.group(1))
#     print(result.group(2))
#     print(result.groups())
# else:
#     print('no match')

# 累積和 accumulate
from itertools import accumulate
# a = list(range(1, 11))
# # itertoolsの戻り値はイテレータとなっているので必要に応じてlist化する
# b = list(accumulate(a))
# print(a)
# print(b)

from itertools import dropwhile, takewhile
# a = [3, 6, 1, 7, 2, 5]

# # 1が出るまでを除外する
# b = dropwhile(lambda x: x != 1, a)
# print(list(b))

# # 1が出るまでを繰り返す
# c = takewhile(lambda x: x != 1, a)
# print(list(c))


from itertools import groupby
# a = [1, 1, 2, 3, 3, 3, 1, 2, 2]

# print(list(groupby(a)))
# for key, value in groupby(a):
#     print(key, list(value))

# b = [1, 3, 2, 4, 3, 1, 1, 2, 4]
# for key, value in groupby(b, key=lambda x: x % 2):
#     print(key, list(value))

# c = [1, 1, 2, 3, 3, 3, 1, 2, 2]
# d = sorted(c)
# for key, value in groupby(d):
#     print(key, list(value))


from collections import Counter
# a = [1, 1, 2, 3, 3, 3, 1, 2, 2]
# counter = Counter(a)

# for key, value in counter.items():
#     print(key, value)

# for文のelse
# for i in range(5):
#     if i == 5:
#         break;
# else:
#     print('@@@')

# for i in range(10):
#     if i == 5:
#         break;
# else:
#     print("$$$")

# 2進数や16進数
# print(bin(255)) # 10 -> 2
# print(hex(255)) # 10 -> 16
# print(int('0b11111111', 2)) # 2 -> 10
# print(int('0xff', 16)) # 16 -> 10

# 順列数と組み合わせ数
# from math import factorial

# def permutations_count(n, r):
#     # 順列
#     return factorial(n) // factorial(n - r)

# def combinations_count(n, r):
#     # 組み合わせ
#     return factorial(n) // (factorial(n - r) * factorial(r))

# print(permutations_count(5, 3))
# print(combinations_count(5, 2))

# メモ化
# from functools import lru_cache

# @lru_cache(maxsize=None)
# def fibo(n):
#     if n <= 0:
#         return 0
#     elif n == 1:
#         return 1
#     else:
#         return fibo(n - 1) + fibo(n - 2)

# print(fibo(35))

# stdinをファイルに置き換える
'''
入力データをファイルに保存しておいてリダイレクトでstdinにデータを流し込む
ファイルをopenした場戻り値でstdinを上書きすることで解決する
'''
from sys import stdin
stdin = open('sample.txt')
print(stdin.readline().rstrip())