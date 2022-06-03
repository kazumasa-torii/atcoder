import sys
import copy
input = sys.stdin.readline
A, B, C, D, E, F, X = map(int, input().split())
one_X = copy.deepcopy(X)
two_X = copy.deepcopy(X)
ans_A = 0
ans_B = 0
while one_X > 0:
    if one_X - A >= 0:
        one_X -= (A + C)
        ans_A += (B * A)
    elif one_X < 0:
        break
    else:
        ans_A += (B * one_X)
        break

while two_X > 0:
    if two_X - A >= 0:
        two_X -= (D + F)
        ans_B += (E * D)
    elif two_X < 0:
        break
    else:
        ans_B += (E * two_X)
        break
ans = str()
if ans_A > ans_B:
    ans = 'Takahashi'
elif ans_A < ans_B:
    ans = 'Aoki'
else:
    ans = 'Draw'

print(ans)
