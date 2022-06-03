"""
今回の肝は全探索できるレベルの処理しかなかったということがわかれば
全探索が使える
そして概ね全探索ではbit全探索で答えが出せることが多いので習得必要
"""
import sys
input = sys.stdin.readline
N = int(input())
ans = []
# bit探索させる
for i in range(1 << N):
    tmp = ''
    count = 0
    """
    1010101010
    と
    10
    のand演算させて
    0000000010
    となる
    その結果をifで分岐
    """
    for j in range(N):
        if i & (1 << j):
            tmp += '('
            count += 1
        else:
            tmp += ')'
            count -= 1

        if count < 0:
            break
    if count == 0:
        ans.append(tmp)

ans.sort()
for i in ans:
    print(i)
