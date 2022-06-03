"""
dictの拡張機能版
データがなくてもInsertできたり、lambdaで初期値を設定できたりする
※lambdaの場合は処理時間が多分遅くなる
"""
from collections import defaultdict
a = defaultdict(int) # 他の型も入る
a[1] = 1
print(a) # defaultdict(None, {1: 1})

b = defaultdict(lambda: 2)
for i in range(2):
    b[i] += 0
print(b) # defaultdict(<function <lambda> at 0x0000022D8248E160>, {0: 2, 1: 2})
