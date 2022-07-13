"""
LとRの値のみ注目
T L R
1 2 3
2 4 5
3 1 2
4 4 9
みたいにあったらTの区間わけを取っ払う
全部開区間にしてしまって詳細な場合分けをなくしてしまうのが肝
あとはLとRの関係を全部見ていく
L[i] R[j] の関係が > ならばL[i] とR[j] は区間が離れているのでバツ
L[j] R[i] の関係が > ならばL[i] とR[j] は区間が離れているのでバツ
全部がくっついているか、包括されているのかを判断させる

また閉区間は未満なので小数点を足したり引いたりしたら開区間にできるが小数点を扱いたくないので
全部の値を二倍したらすべて整数で判断できるようになる
"""

import sys
input = sys.stdin.readline

def main():
    N = int(input())
    I = []
    L = []
    R = []
    for i in range(N):
        t, l, r = map(int, input().split())
        l *= 2
        r *= 2
        if t%2 == 0:
            r -= 1
        if t >= 3:
            l += 1
        L.append(l)
        R.append(r)
    ans = 0
    for i in range(N):
        for j in range(i+1, N):
            if L[i] > R[j]: continue
            if L[j] > R[i]: continue
            ans += 1
    print(ans)

    return

if __name__ == '__main__':
    main()
