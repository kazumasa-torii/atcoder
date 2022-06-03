"""
優先度付きキュー
"""
import heapq

a = [1, 2, 3, -3,-2, 47]
heapq.heapify(a) # リストから優先度付きキューへ変換
print(a)

print(heapq.heappop(a)) # 最小値の取り出し

a = list(map(lambda x: x*(-1), a))  # 各要素を-1倍
print(a) # 最大値を取得する際には、-をつけて保存させるのが良い

heapq.heappush(a, 11) # 要素の挿入
print(a)
