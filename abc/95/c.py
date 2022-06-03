import sys
input = sys.stdin.readline
ans = 0
A, B, C, X, Y = map(int, input().split())
Z = min(X, Y)*2
if A+B >= C*2:
    max_x = max(X-Y, 0)
    max_y = max(Y-X, 0)
    ans = min(C*Z + A*(max_x) + B*(max_y), C*max(X,Y)*2)
else:
    ans = A*X + B*Y
print(ans)
