"""
日付を後ろから進めて行き制約をかけながら一番大きい数字を取得していく
肝は、複数の制約があった時には一つずつ制約を倒していくようにしていく
言い換え大事

1. 報酬0の仕事を日付ごとに作成する
1. 仕事リストをかかる日付
1. listを回して同じ日付のものを優先度キューにマイナスで突っ込む
1. 日付が変わったら優先度キューから一番大きい給与を取得
1. そこから同じように進めて合計値を答える
"""
import sys
import heapq
from operator import itemgetter
from typing import List
input = sys.stdin.readline

def main():
    n, m = map(int, input().split())
    li = [list(map(int, input().split())) for _ in range(n)]

    li2=[[i, 0] for i in range(1, m + 2)] #すべてのAi=1 to Mについて報酬0の仕事を追加する
    li.extend(li2)
    li=sorted(li, key=itemgetter(0)) #Aiの小さい順にソート
    q = []
    ans = 0
    pos = 0
    while 1:
        a, b = li[pos]
        if a > m: #AiがMより大きければその仕事を請ける意味はない
            break
        if a == li[pos + 1][0]: #Aiの値が等しいとき、その仕事を優先度付きキューに追加する
            heapq.heappush(q,-b)
        else:
            heapq.heappush(q,-b)
            ans -= heapq.heappop(q) #Aiの値が変化したとき、そのAiまででの仕事の報酬の最大値を答えに加える
        pos += 1
    print(ans)

    return

main()
