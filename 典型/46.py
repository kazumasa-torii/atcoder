"""
同じ意味のものをまとめて考える

1. 数字は46より大きい数は使わないのでその都度modで割っておく
1. 各数字をlistに落とし込んでindexに突っ込んでおく
1. これを全探索させる
1. 各listを46回まわして組み合わせが存在する個数を掛け算してそれをansに突っ込む
1. 最後にansを答えたらおわり

肝は、計算量を言い換えで減らしたこと
これは、どの内容でも必要なので今後活用する
"""

import sys
input = sys.stdin.readline
sys.setrecursionlimit(3000)

def main():
    n: int = int(input())
    mod = 46
    limit = mod+1
    A = list(map(lambda x: int(x)%mod, input().split()))
    B = list(map(lambda x: int(x)%mod, input().split()))
    C = list(map(lambda x: int(x)%mod, input().split()))
    am = [0] * limit
    bm = [0] * limit
    cm = [0] * limit
    for i in range(n):
        am[A[i]] += 1
        bm[B[i]] += 1
        cm[C[i]] += 1

    ans = 0
    for i in range(limit):
        for j in range(limit):
            for k in range(limit):
                if (i + j + k) % mod == 0:
                    ans += (am[i] * bm[j] * cm[k])
    print(ans)

if __name__ == "__main__":
    main()
