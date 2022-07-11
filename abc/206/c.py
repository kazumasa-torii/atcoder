"""
肝は、dictを変動させていくのがポイント
今までは、前処理で使うことが多かったがdictをforの中で使用するのは初めて
確かにこの動きなら使いやすいかも
"""

import sys
from collections import defaultdict
input = sys.stdin.readline

def main():
    N = int(input())
    A = list(map(int, input().split()))
    li = defaultdict(int)
    idx = 0
    ans = 0
    for i in A:
        idx += 1
        li[i] += 1
        ans += idx - li[i]
    print(ans)
    return

if __name__ == '__main__':
    main()
