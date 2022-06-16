import sys
from typing import List
input = sys.stdin.readline

def main():
    N, X = map(int, input().split())
    li = list(map(int, input().split()))
    li_sum = (sum(li) + 1)
    acc = [0] * li_sum
    cnt = 1
    acc[0] = cnt
    tmp = li[0]
    index = 0
    for i in range(li_sum):
        if i == tmp:
            cnt += 1
            index += 1
            acc[i] = cnt
            if index <= len(li)-1:
                tmp = i + li[index]
        else:
            acc[i] = cnt

    print(acc[X])
    return

main()
