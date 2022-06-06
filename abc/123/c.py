"""
ボトルネックの存在

一旦シュミレーションした上で遷移がどのようになるかを理解する
ここらへんは絵で書いたほうがわかるのでシュミレーションを書き起こしてみる
"""
import sys
import math
input = sys.stdin.readline

def main():
    N = int(input())
    li = [int(input()) for _ in range(5)]
    min_num = min(li)
    print(math.ceil(N/min_num) + 4)

main()
