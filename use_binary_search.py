"""
1.left は常に条件を満たさない
1.right は常に条件を満たす
1.right - left = 1 になるまで範囲を狭める
        (最後は right が条件を満たす最小)

math.ceil(left + (right - left) / 2)
...これの意味は、まずright - leftでこの2つの距離を取得する
...次に2つの間の真ん中を取得するために / 2 を行う
...最後にleft分を足してleft と right の中間を取得できる

出力する際は、常にrightが真なのでwhileを抜けた時には、rightを返す
"""
import math

def isOK(index: int, key:int) -> bool:
    if a[index] >= key: return True
    else: return False

# 汎用的な二分探索のテンプレ
def binary_search(key: int) -> int:
    left: int = -1
    right: int = len(a)
    while right - left > 1:
        mid: int = math.ceil(left + (right - left) / 2)
        if isOK(mid, key): right = mid
        else: left = mid
    return right

a = [1, 14, 32, 51, 51, 51, 243, 419, 750, 910]

print(binary_search(419))
