"""
周期性
当初は、4735まわせば同じ数になるようになっていたのでそれを省いた最低限回す形で答えを取得していたが間違いっぽい
最終的には、(K-mod) % 周期 + modにすれば問題なかった。
ここらへんの周期がちょっとよくわからなかったので再度考える
"""
import sys
import time
from io import StringIO
from typing import List


_INPUT = """\
99999 1000000000000000000

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)
mod = 10 ** 5

#桁の和
def digit_sum(x):
    return (x + sum(map(int, list(str(x))))) % mod

def main():
    N, K = map(int, input().split())
    done = [-1] * mod

    index = 0
    now = N

    # ここで周期性を確認する
    while True:
        # ぐるぐる回して数字が入っているものに出逢えばブレイク
        # 周期で数字が入っているのですでにこの数字は出現しているので
        # この先は、同じような数字が出てくるだけになる
        if done[now] != -1:
            loop = index - done[now]
            break
        done[now] = index
        now = digit_sum(now)
        index += 1

    if K > mod:
        # Kからmod分引いてさらに周期分とmodを足したものあまりを算出
        K = (K-mod) % loop + mod

    # 最後に問題文通り答えを出す
    # このときには、すでに10 ** 5程度になっているので問題無い
    for _ in range(K):
        N = digit_sum(N)
    
    print(N)
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
