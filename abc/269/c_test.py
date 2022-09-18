"""
こっちがわかりやすい
ビットの各桁の調べてそれを出力に応用するみたいなやり方
ただ具体的なやり方はわかっていないので再度履修
"""
import sys
import time
from io import StringIO
from typing import List

_INPUT = """\
11

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)
def main():
    n = int(input())
    a = []
    for i in range(60):
        if n&(1<<i):a.append(i)
    
    k = len(a)
    res = []
    for i in range(1<<k):
        cur = 0
        for j in range(k):
            if i & (1 <<j): cur |= 1 << a[j]
        res.append(cur)
    for i in res:
        print(i)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
