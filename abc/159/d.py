"""
遷移の仕方を理解してその差分を対応する
遷移の仕方は考えていたけど
差分の引き方というか求め方が悪かった
最初に全体の通り数を数えておいて
そこから一つ数字がなくなったときの遷移を考えていなかった
都度都度じゃなくて最初にまとめてやるようにする
"""

import sys
input = sys.stdin.readline
def main():
    def choose(n):
        return n * (n-1) // 2

    n = int(input())
    a = list(map(lambda x: int(x) - 1, input().split()))
    
    cnt = [0] * n
    for i in range(n): cnt[a[i]] += 1
    tot = 0
    for i in range(n): tot += choose(cnt[i])
    for i in range(n):
        ans = tot
        ans -= choose(cnt[a[i]])
        ans += choose(cnt[a[i]] - 1)
        print(ans)
    return

if __name__ == '__main__':
    main()