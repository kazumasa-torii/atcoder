"""
プライオリティーキューのことです(Pythonだとヒープキューっていうらしい)。プライオリティーキューとは
- 計算量O(logN)O(log⁡N)で要素を挿入
- 計算量O(logN)O(log⁡N)で最小値を取り出す
ができるデータ構造です。最短経路を求めるダイクストラ法でお世話になります。
"""
from heapq import heappop,heappush
L=[3,0,2,5,7,2]
H=[]
for l in L: #ここはH=heapq.heapify(L)でもいいです。
    heappush(H,l) 
print(H) #[0, 3, 2, 5, 7, 2]
print(heappop(H)) #0
print(heappop(H)) #2
print(heappop(H)) #2
