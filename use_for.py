
"""
range(stop)
range(start, stop[, step])
"""
# 最終値のみを指定（初期値は0、増分値は1）
for num in range(3):
    print(num)  # 0、1、2

# 初期値と最終値を指定（増分値は1）
for num in range(2, 5):
    print(num)  # 2、3、4

# 初期値と最終値と増分値を指定
for num in range(2, 8, 2):
    print(num)  # 2、4、6

# 増分値に負値を指定
for num in range(5, 2, -1):
    print(num)  # 5、4、3


"""
enumerate
"""
iterable = [chr(num+ord('A')) for num in range(3)]

# (インデックス, 要素)を個別のループ変数に代入
for index, item in enumerate(iterable):
    print(index, ':', item)  # '0 : A'、'1 : B'、'2 : C'

# (インデックス, 要素）を単一のループ変数に代入
for t in enumerate(iterable):
    print(t[0], ':', t[1])  # '0 : A'、'1 : B'、'2 : C'

# インデックスの初期値を1にする
for index, item in enumerate(iterable, 1):
    print(index, ':', item)  # '1 : A'、'2 : B'、'3 : B'


"""
zip
"""
x = list(range(5))  # [0, 1, 2, 3, 4]
y = list(range(1, 6))  # [1, 2, 3, 4, 5]

# タプルを単一のループ変数に受け取る例
for coord in zip(x, y):
    print(coord)  # (0, 1)、(1, 2)、(2, 3)、(3, 4)、(4, 5)

# タプルの要素を個別のループ変数に受け取る例
for xp, yp in zip(x, y):
    print(f'({xp}, {yp})')  # (0, 1)、(1, 2)、(2, 3)、(3, 4)、(4, 5)

# タプルの内容を基に辞書を作り、それらを要素とするリストを作る
xy_list = []  # 空のリスト
for xp, yp in zip(x, y):
    xy_list.append({'x': xp, 'y': yp})
