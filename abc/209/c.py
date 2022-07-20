"""
順列の考え方

1. 順番は関係ないのでsortする（制約で順番大事そうだけど結局数字が異なればOKなので無視）
1. あとは順列なので各数字の組み合わせを考える
1 3 4 6
1 1 1 1
  2 2 2
  3 3 3
    4 4
      5
      6
になるので
1 2 2 3 通りずつ使えるので予め計算する
1. あとはansにすべて掛けていくだけ(modは忘れないようにする)
"""
import sys
input = sys.stdin.readline
def main():
    mod = 10 ** 9 + 7
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    maina = 0
    for i in range(n):
        c[i] -= maina
        maina += 1
    ans = c[0]
    for i in range(1, n):
        ans *= c[i]
        ans %= mod
    print(ans)
    return

if __name__ == '__main__':
    main()
