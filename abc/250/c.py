"""
1.数列を作る時に各indexの場所を記したlistも作成する
1.場所が左端かどうなのか判断させて入れ替えさせる
1.indexの場所も入れ替える

肝はすべて同じListで行わないようにすること
"""
import sys
input = sys.stdin.readline

def main():
    N, Q = map(int, input().split())
    A = list(range(N+1))
    idx = list(range(N+1))

    for _ in range(Q):
        x = int(input())
        fi = idx[x]
        si = fi + 1 if fi != N else fi - 1
        y = A[si]
        A[fi], A[si] = A[si], A[fi]

        idx[x] = si
        idx[y] = fi
    print(*A[1:])

main()
