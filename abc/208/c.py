import sys
from collections import defaultdict
from copy import deepcopy
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    hand = k // n
    amari = k % n
    a = list(map(int, input().split()))
    b = deepcopy(a)
    b.sort()
    num = defaultdict(int)
    for i in b:
        num[i] = hand
    while amari > 0:
        for _, i in enumerate(num):
            if amari == 0:
                break
            num[i] += 1
            amari -= 1
    for i in range(n):
        print(num[a[i]])
    return

if __name__ == '__main__':
    main()
