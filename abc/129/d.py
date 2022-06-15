"""
縦方向と横方向でどのくらいのマスが光に照らされているのかを収集する
そして答えを 縦方向 + 横方向 -1を行い大きさを比べていく
-1は自分のマスを抜いた数ということ

ただ実装イメージがついていないので再度やる

"""
from typing import List
from sys import  stdin
input = stdin.readline
def main():
    # H, W = map(int, input().split())
    # atlas: List[str] = [str(input().rstrip('\n')) for _ in range(H)]

    H, W = 4, 6
    atlas: List[str] = ['#..#..', '.....#', '....#.', '#.#...']


    return

main()
