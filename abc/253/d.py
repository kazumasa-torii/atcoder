import sys
import math
input = sys.stdin.readline

"""
最小公倍数
(x * y) // 最大公約数
"""
def lcm(x, y):
    return (x * y) // math.gcd(x, y)

"""
等差数列の和
n:項数
a:初項
d:公差

例
初項 3
公差 2
項数 10の等差数列
[3, 5, 7, 9, 11, 13, 15, 17, 19, 21]

足し算は順序に関係なく一定なので，(1)の式は(2)ともかけます。
S10 = 3 + 5 + 7 + 9 + 11 + 13 + 15 + 17 + 19 + 21…(1)
S10 = 21 + 19 + 17 + 15 + 13 + 11 + 9 + 7 + 5 + 3…(2)

なので両方を足すと(3)となります。
2S10 = 24 + 24 + 24 + 24 + 24 + 24 + 24 + 24 + 24 + 24…(3)

これを2で割れば等差数列の和が求まります。
"""
def AP(n, a, d):
    return n*(2*a+(n-1)*d)//2


N, A, B = map(int, input().split())
ans = AP(N,1,1)
one = AP(N//A, A, A)
two = AP(N//B, B, B)
ab_lcm = lcm(A,B)
LCM = AP(N//ab_lcm, ab_lcm, ab_lcm)
ans = ans - one - two + LCM
print(ans)
