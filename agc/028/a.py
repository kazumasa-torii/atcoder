"""
a = n/gcd(n,m)
b = m/gcd(n,m)
これの文字列が同じであればOKで最小公倍数を答えたらOK
これが同じじゃなければ答えは作れない

ただこれどうしてこうなっているのかがいまいち理解できていない
"""
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