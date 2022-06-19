import sys
from typing import List
input = sys.stdin.readline

def main():
    N = int(input())
    li = []
    for _ in range(N):
        li.append(list(map(int,input().split())))

    li = sorted(li, key = lambda x:x[0])
    L = li[0][0]
    R = li[0][1]
    ans = []
    index = 1
    while True:
        if index >= N:
            ans.append([L, R])
            break
        if li[index][0] > R:
            ans.append([L, R])
            L = li[index][0]
            R = li[index][1]
            index += 1
            continue
        if li[index][1] > R:
            R = li[index][1]

        index += 1
    for i in ans:
        print(i[0], i[1])
    return

main()
