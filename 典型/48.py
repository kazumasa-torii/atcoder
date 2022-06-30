"""
問題を2分かけて満点の場合と1分かけた場合の時間という問題を両方1分にすることで問題を単純にした
これが一番の肝
言い換え大事

1. listを作成してそれに1分ごとの解ける問題の点数を追加する
1. sortしてlistのk番目まで見てsumする
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')
_INPUT = """\
4 3
4 3
9 5
15 8
8 6

"""
sys.stdin = StringIO(_INPUT)
StartTime = time.time()

def main():
    n, k = map(int, input().split())
    li = []
    for i in range(n):
        a, b = map(int, input().split())
        li.append(a-b)
        li.append(b)
    li.sort(reverse=True)
    print(sum(li[:k]))
    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
