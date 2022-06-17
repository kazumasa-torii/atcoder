import sys
from typing import List
input = sys.stdin.readline

def main():
    """
    L+i-1 りんごの味
    """
    N, L = map(int, input().split())
    ap =[]
    for i in range(1, N+1):
        num = L+i-1
        ap.append(num)
    ap_sum = sum(ap)
    tmp = 10 ** 10
    index = int()
    for i in range(N):
        if abs((ap_sum - ap[i]) - ap_sum) < tmp:
            index = i
            tmp = abs((ap_sum - ap[i]) - ap_sum)
    print(ap_sum - ap[index])

    return

main()
