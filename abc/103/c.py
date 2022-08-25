import sys
input = sys.stdin.readline
from math import gcd
def main():
    def lcm(a, b):
        return a * b // gcd (a, b)
    n = int(input())
    a = list(map(int, input().split()))
    tmp = lcm(a[0], a[1])
    for i in range(2, n):
        tmp = lcm(tmp, a[i])
    ans = 0
    tmp -= 1
    for i in a:
        ans = ans + (tmp%i)
    print(ans)
    return

if __name__ == '__main__':
    main()
