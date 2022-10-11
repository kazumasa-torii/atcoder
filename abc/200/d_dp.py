"""
sortして愚直に全探索できるか考える
その後に難しそうであれば下記アルゴリズムを考える

共通
全探索,二部探索,累積和,いもす法,順列全探索,区間スケジューリング,貪欲法

グラフ関係
DFS,BFS,ダイクストラ法,ワーシャルフロイド法,トポロジカルソート

DP
区間,bit,ナップサック,桁

数学
約数,素数判定法,mod,組み合わせ,幾何

その他
クラスカル法,木,Union-find
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
5
180 186 189 191 218

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def create_new_dp():
        # dequeには、[1, 2, 4]や[2, 3]といったリストが入ります
        # appendで末尾に要素を追加して、3つ以上数列が入ることになる、勝手にpopleft()して先頭から1個消してくれます
        return [deque(maxlen=2) for _ in range(200)]

    def solve():
        dp_prev = create_new_dp()
        dp_cur = create_new_dp()

        for i in range(1, N + 1):
            dp_cur = create_new_dp()
            dp_cur[A[i]].append([i])
            for j in range(200):
                for prev in dp_prev[j]:
                    dp_cur[j].append(prev) # A[i] を使わない場合（そのまま）
                    dp_cur[(A[i] + j) % 200].append(prev + [i]) # A[i] を使う場合
            dp_prev = dp_cur
        return dp_cur

    def print_answer(dp_final):
        for i in range(200):
            if len(dp_final[i]) == 2:
                B = dp_final[i][0]
                C = dp_final[i][1]
                B_out = [len(B)] + B
                C_out = [len(C)] + C
                print("Yes")
                print(*B_out)
                print(*C_out)
                return
        print("No")
        return

    from collections import deque
    N = int(input())
    _A = [-1] + list(map(int, input().split()))  # 1-indexedに合わせます
    A = [x % 200 for x in _A]  # 200で割った余りにしておきます

    dp_final = solve()
    print_answer(dp_final)


if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
