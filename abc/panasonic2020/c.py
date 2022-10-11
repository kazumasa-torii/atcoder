"""
式変形が必要でこれはわからん
"""
import sys
input = sys.stdin.readline
def main():
    a, b, c = map(int, input().split())
    d = c - a - b
    if d > 0 and d * d > 4 * a * b: print('Yes')
    else: print('No')
    return

if __name__ == '__main__':
    main()