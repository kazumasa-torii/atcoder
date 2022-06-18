from distutils.spawn import spawn
import sys
from typing import List
input = sys.stdin.readline

mod = 10 ** 9 * 7
limit = 4000
pa = [[1]]
for i in range(1,limit):
    tmp = [1]
    if i > 1:
        for j in range(1,i):
            tmp.append(pa[i-1][j-1]+pa[i-1][j])
    tmp.append(1)
    pa.append(tmp)

def comb(n: int, k: int):
    return pa[n][k]

def f2(n: int, k: int):
    return comb(n+k-1, k-1) % mod

def f(n: int, k: int):
    if n < k: return 0
    if n == 0 and k == 0: return 1
    if k < 1: return 0

    return f2(n-k, k) % mod

def main():
    N, K = map(int, input().split())

    for i in range(1, K+1):
        bule = f(K, i)
        red = 0

        red += f(N-K, i-1) % mod
        red += f(N-K, i) % mod
        red += f(N-K, i) % mod
        red += f(N-K, i+1) % mod

        ans = bule * red % mod
        print(ans)

    return

main()
