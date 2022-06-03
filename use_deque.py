from collections import deque

d = deque([1, 2, 3, 4, 5])

# 「appendleft」メソッドを使用します。
# Listでは「insert」メソッドを使用する。
d.append('b')
d.appendleft('c')

d.insert(2, 5)
print(d)
# -> deque([1, 2, 5, 3, 4, 5])

# deque内の引数に等しい値の数を数える。
print(d.count(5))
# -> 2

# deque内の引数に等しい値の位置を返す。
print(d.index(2))
# -> 1
print(d.index(5))
# -> 2
print(d.index(5, 4, 6))
# -> 5

# pop:dequeの右側の要素を削除して返す。
print(d.pop())
# -> 5
print(d)
# -> deque([1, 2, 5, 3, 4])

# popleft:dequeの左側の要素を削除して返す。
print(d.popleft())
# -> 1
print(d)
# -> deque([2, 5, 3, 4])

# deque内の引数に等しい最初の値を削除する。
d.remove(5)
print(d)
# -> deque([2, 3, 4])

# deque内の要素の並びを反転させる。
d.reverse()
print(d)
# -> deque([4, 3, 2])

# インテラブルな要素を右側に追加する。
li = [6,7,8,9]
d.extend(li)
print(d)
# -> deque([1, 2, 3, 4, 5, 6, 7, 8, 9])

# インテラブルな要素を左側に追加する。
d.extendleft(li)
print(d)
# -> deque([9, 8, 7, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9])

# 引数の値だけ要素を右に移動する。
# 末端を超える要素は先頭に移動する。
d.rotate(1)
print(d)
# -> deque([9, 9, 8, 7, 6, 1, 2, 3, 4, 5, 6, 7, 8])

# 負の数を指定すると左に移動する。
d.rotate(-1)
print(d)
# -> deque([9, 8, 7, 6, 1, 2, 3, 4, 5, 6, 7, 8, 9])

d.clear()
print(d)
# -> deque([])
