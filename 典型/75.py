"""
因数に分解する感じはなんとなくやっていたが結局どうやって答えを求めるかわからなかった
最小は因数の数を半分に割って切り上げすることにより
因数の要素を把握できる（計算は必要としていないので因数分のみ）
後はそれを繰り返してカウントしていけば最小の数を求めることができる
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
48

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    n = int(input())
    cnt = 0
    # 素因数分解を行い数を因数の数を数える
    d = 2
    while d*d <= n:
        while n % d== 0:
            cnt += 1
            n //= d
        d += 1
    
    if n > 1:
        cnt += 1

    ans = 0
    # 因数の数を半分に割り切り捨ててあまりをプラスする
    # 要するに切り上げするって感じ
    while cnt > 1:
        ans += 1
        cnt = cnt // 2 + cnt % 2

    print(ans)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
