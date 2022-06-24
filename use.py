"""
処理速度はlambdaよりitemgetterのほうが早い
"""
from operator import itemgetter

before = [[1 ,2], [2 ,2], [3 ,2, 4], [100 ,2, 11]]
dic = {1:10, 11:1, 12:3, 33:4, 14:55, 17:0}

# dictに関しては、items()にしてからkeyを指定する
print(sorted(dic.items(), key=itemgetter(1)))

# 多次元配列でsortする lambda x: x[1] で多次元配列のiの1番目のindexでsortさせる
before.sort(key=itemgetter(1))

# 複数の引数でsortする
before.sort(key=itemgetter(0, 1))

# sortを逆順にする 単次元
before.sort(key=itemgetter(1), reverse=True)

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
