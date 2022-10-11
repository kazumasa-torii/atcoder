"""
片方を固定してもう片方を求めるってやり方
これで計算量を落とすことができる

また個数を予めカウントしておきo(1)で個数を求めるようにしておくのもポイント
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
3
1 2 2
3 1 2
2 3 2

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from collections import defaultdict
def main():
    N = int(input())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))
    C = list(map(lambda x: int(x) - 1, input().split()))
    a_dict = defaultdict(int)
    for i in range(10 ** 5):
        a_dict[i] = 0
    for i in A:
        a_dict[i] += 1
    ans = 0
    for i in C:
        if a_dict[B[i]]:
            ans += a_dict[B[i]]
    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
