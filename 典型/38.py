import sys
import math
input = sys.stdin.readline
one, two = map(int, input().split())
ans = (one * two) // math.gcd(one, two)
print(ans if ans <= 1000000000000000000 else 'Large')
