from audioop import reverse

before = [[1 ,2], [2 ,2], [3 ,2, 4], [100 ,2, 11]]
# 多次元配列でsortする lambda x: x[1] で多次元配列のiの1番目のindexでsortさせる
after = sorted(before, key=lambda x: x[1])

# 複数の引数でsortする
after = sorted(before, key=lambda x: (x[0], x[1]))

# sortを逆順にする 単次元
ld = sorted(before, reverse=True)

# 無限
# inf = float('inf')

# 改行の削除
# list(input().strip())

# 内容をコピーする（deepcopy）
import copy
l1 = [4, 5, 6]
l2 = copy.copy(l1) # 一次元のみ対応
l3 = [[1, 2, 3], [4, 5, 6]]
l4 = copy.deepcopy(l3) # 多次元配列の場合は深いコピー
