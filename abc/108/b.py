"""
意味がわからん
"""
import sys
input = sys.stdin.readline
def main():
    a, b, c, d = map(int, input().split())
    x, y = c - a, d - b
    print(c-y, d + x, a - y, b + x)
    return

if __name__ == '__main__':
    main()
