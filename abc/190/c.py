"""
まずはsortして解決できないか考える
その上でDPまたはDFS、BFSが必要ならば使う
二分探索木もあるよ
"""
import sys
input = sys.stdin.readline
from itertools import product
from collections import Counter
 
 
def calc(bit):
    counter = Counter()
    for i in range(K):
        choice = choices[i][bit >> i & 1]  # bit >> i & 1と書くと、i桁目が0か1かそのまま得られます
        counter[choice] += 1
 
    # 満たされている条件の数を、問題文通りに数えます
    ret = 0
    for a, b in cond:
        if counter[a] > 0 and counter[b] > 0:
            ret += 1
    return ret
 
 
N, M = map(int, input().split())
 
cond = []
for _ in range(M):
    a, b = map(int, input().split())
    cond.append((a, b))
 
K = int(input())
choices = []
for _ in range(K):
    c, d = map(int, input().split())
    choices.append((c, d))
 
ans = 0
for bit in range(1 << K):
    ans = max(ans, calc(bit))
print(ans)
