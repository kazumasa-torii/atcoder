"""
気持ちは二分探索
ただ場合分けのやり方がうまかった

先頭がaである可能性はa+bCa-1で求まる
それ以上ならば先頭はbである
これを文字数分繰り返していけば正答の文字列を回答できるって内容
"""
import sys
import time
from io import StringIO
from typing import List
# input = sys.stdin.readline
# import pypyjit
# pypyjit.set_param('max_unroll_recursion=-1')

_INPUT = """\
30 30 1

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

def main():
    A, B, K = map(int, input().split())
    pascal = [[1]]
    for i in range(1,A+B+1):
        tmp = [1]
        if i > 1:
            for j in range(1,i):
                tmp.append(pascal[i-1][j-1]+pascal[i-1][j])
        tmp.append(1)
        pascal.append(tmp)
    ans = str()
    print(pascal[A+B-1][A-1], A+B-1, A-1)
    # while A+B > 0:
    #     x = 0
    #     if A >= 1: x = pascal[A+B-1][A-1]
    #     if K <= x:
    #         ans += 'a'
    #         A -= 1
    #     else:
    #         ans += 'b'
    #         B -= 1
    #         K -=x
    # print(ans)

    return

main()
print(f'[Sec] {str(time.time() - StartTime)}')
"""
7までのパスカルの三角形
[
0    [1],
1    [1, 1],
2    [1, 2, 1],
3    [1, 3, 3, 1],
4    [1, 4, 6, 4, 1],
5    [1, 5, 10, 10, 5, 1],
6    [1, 6, 15, 20, 15, 6, 1],
7    [1, 7, 21, 35, 35, 21, 7, 1]
]

118264581564861424
118264581564861424
"""
