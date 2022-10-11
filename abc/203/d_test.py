"""
二分探索と累積和
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
3 2
1 7 0
5 8 11
10 4 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    def judge(acc):
        """
        midより大きい値が K ** 2 // 2 + 1 個未満である K * K の区域が存在するかどうか判定します
        midより大きい値の個数はmidが小さくなると、単調に減少しますから、二分探索が可能です
        00000
        0****
        0*+*-
        0*-*o

        oのところの累積和を求める場合は、
        -のところの値を引いて+のところを追加する

        -----
        00000
        0****
        0****
        -----
        0****

        |000|00
        |0**|**
        |0**|**
        |0**|**

        -のところを引く

        000|00
        0**|**
        0**|**
        ---
        0****
        だが同じところを引いてしまうのでこの四角の部分のところを足す
        """
        for row in range(K, N + 1):
            for col in range(K, N + 1):
                # 二次元累積和のテンプレです。最後に足しているのは、二重に引いている部分を足すためです。
                cnt = acc[row][col] - acc[row - K][col] - acc[row][col - K] + acc[row - K][col - K]
                if cnt < K ** 2 // 2 + 1:
                    return True
        return False

    def twoDimensionsAcc(mid):
        """
        ある区域の、midより大きい数の個数を高速で求めるために、二次元累積和を作ります
        処理の都合上、行と列のインデックスを1ずつずらして、(N+1)*(N+1)の二次元リストにします
        """

        acc = [[0] * (N + 1) for _ in range(N + 1)]

        """
        外枠に0の列を追加するイメージ
        00000
        0****
        0****
        0****
        この*の中に内容を入れる必要がある
        """
        for row in range(N):
            for col in range(N):
                if A[row][col] > mid:
                    acc[row + 1][col + 1] = 1

        # 横方向の累積和をとります
        for row in range(1, N + 1):
            for col in range(N):
                acc[row][col + 1] += acc[row][col]
        # さらに縦方向の累積和をとります
        for col in range(1, N + 1):
            for row in range(N):
                acc[row + 1][col] += acc[row][col]
        return acc

    N, K = map(int, input().split())
    A = [list(map(int, input().split())) for _ in range(N)]

    ok = 10 ** 10
    ng = -1

    while abs(ok - ng) > 1:
        mid = (ok + ng) // 2
        acc = twoDimensionsAcc(mid)

        if judge(acc):
            ok = mid
        else:
            ng = mid

    print(ok)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
