import sys
from typing import List
input = sys.stdin.readline

def main():
    N = int(input())
    li = [list(map(int, input().split())) for _ in range(N)]
    li = sorted(li, key = lambda x:x[1])
    time = 0
    for i in range(N):
        time += li[i][0]
        if time > li[i][1]:
            print('No')
            return
    print('Yes')
    return

main()
