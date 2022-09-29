import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
from math import gcd
def main():
    n, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.insert(0, x)
    gcdList = []
    for i in range(1, n+1):
        gcdList.append(abs(a[i] - a[i-1]))
    ans = gcdList[0]
    for i in range(1, len(gcdList)):
        ans = gcd(ans, gcdList[i])
    print(ans)
    return

if __name__ == '__main__':
    main()