import sys
import time
from io import StringIO

_INPUT = """\
15 9
dnsusrayukuaiia
dujrunuma

"""
StartTime = time.time()
sys.stdin = StringIO(_INPUT)

from math import gcd
def main():
    def lcm(a, b):
        return  a * b // gcd(a, b)
    n, m = map(int, input().split())
    s = input()
    t = input()

    g = gcd(n,m)
    if s[0::n//g] == t[0::m//g]:print(lcm(n,m))
    else:print(-1)
    return

if __name__ == '__main__':
    main()
    print(f'[Sec] {str(time.time() - StartTime)}')
