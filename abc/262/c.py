"""
ai = i と aj = j
→indexとlist[index]が同じってこと
ai = j と aj = i
→index と list[index] が同じ（ただしindexの位置が違う）

この2つの内容を理解してい進めていくべきだった…。

1. ai = i と aj = j が成り立つ組の総数は ak = k であるようなkの個数をnとした場合 n(n-1)/2となる
1. ai = j と aj = i が成り立つ組数は試さないとわからないのでここを全探索
1. これでO(N)で対応することができる

"""

import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = list(map(lambda x: int(x)-1, input().split()))

    same = 0
    for idx, value in enumerate(li):
        if idx == value:
            same += 1
    
    ans = same * (same - 1) // 2
    for idx, value in enumerate(li):
        if idx < value and li[value] == idx:
            ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
