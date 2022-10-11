"""
鳩の巣原理！！
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
    def solve():
        L = [[] for _ in range(200)]

        N = int(input())
        A = list(map(int, input().split()))

        if N > 8:
            A = A[:8]  # 2 ** 8 - 1 = 255通りの選び方があれば、必ず答えが存在します
        M = len(A)

        for bit in range(1, 1 << M):
            s = 0  # 和
            I = []  # 選び方
            for i in range(M):
                if (bit >> i) & 1:
                    s += A[i]
                    I.append(i + 1)  # 出力は i + 1 です
            remainder = s % 200  # 余り
            L[remainder].append(I)
        return L

    def print_answer(L):
        # 総和の余りがiの数列が、2つ以上あるか探します
        for i in range(200):
            if len(L[i]) >= 2:
                B = L[i][0]
                C = L[i][1]
                B_out = [len(B)] + B
                C_out = [len(C)] + C
                print("Yes")
                print(*B_out)
                print(*C_out)
                return
        print("No")
        return

    L = solve()
    print_answer(L)

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
