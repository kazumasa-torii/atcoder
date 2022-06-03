import sys
input = sys.stdin.readline
N = int(input())
if N % 100 == 0:
    print(N // 100)
else:
    print(N // 100 + 1)
