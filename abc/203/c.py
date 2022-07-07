"""
答えの出し方が微妙だった
最初にKをansに足しておいてそこから比べて行くべきだった
要素を少なくしてシンプルに考える実装例
"""
import sys
from operator import itemgetter
def main():
    input = sys.stdin.readline
    ans = 0
    N, K = map(int, input().split())
    li = []
    for _ in range(N):
        x, y = map(int, input().split())
        li.append([x, y])
    li.sort(key=itemgetter(0))
    ans += K
    j = 0
    while j < N and li[j][0] <= ans:
        ans += li[j][1]
        j += 1
    print(ans)

    return

main()
