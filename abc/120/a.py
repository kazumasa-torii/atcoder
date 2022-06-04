import sys
input = sys.stdin.readline
a, b, c = map(int, input().split())
print(c if b//a > c else b//a)
