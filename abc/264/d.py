"""
転倒数の個数を調べるためにバブルソートする
このバブルソートした数を答えに出力
"""

import sys
input = sys.stdin.readline
from collections import defaultdict
def main():
    t = 'atcoder'
    s = input().strip()
    n = len(t)
    dic = defaultdict()
    for i in range(n): dic[t[i]] = i
    a = []
    for i in range(n): a.append(dic[s[i]])
    ans = 0
    for i in range(n):
        for j in range(i):
            if a[j] > a[i]: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
