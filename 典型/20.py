import sys
input = sys.stdin.readline
one, two, three = map(int, input().split())
print('Yes' if one < pow(three, two) else 'No')
