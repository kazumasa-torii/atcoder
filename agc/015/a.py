import sys
input = sys.stdin.readline

from itertools import combinations_with_replacement
def main():
    n, a, b = map(int, input().split())
    if n == 1 and a == b: exit(print(1))
    elif n == 1 and a != b: exit(print(0))
    elif a > b: exit(print(0))
    print((b-a)*(n-2) + 1)
    return

if __name__ == '__main__':
    main()