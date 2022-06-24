"""
公式解説は文字列をsortして対応していたけどいまいちやり方できなかったので方針変更

当初考えていた内容を実際に実装しているコードがあったので真似て対応

1. 文字が同じ数だけ出ている場合はアナグラムであると仮定
1. 各文字を数え上げて対応させてdictで管理する
1. その答えをコンビネーションで同じ文字列をnとおく nC2 を計算
1. それのsumして答え

str型もdict行けたのね…。
前に失敗したので行けないものだと思っていた…。
"""
from collections import defaultdict
def main():
    n = int(input())
    li = [input() for _ in range(n)]

    dic = defaultdict(int)

    for s in li:
        s = ''.join(sorted(list(s)))
        dic[s] += 1
    ans = 0

    for val in dic.values():
        ans += val*(val-1) // 2
    print(ans)
    return

main()
