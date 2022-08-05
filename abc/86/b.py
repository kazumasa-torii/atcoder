import sys
input = sys.stdin.readline
from math import sqrt
def main():
    a, b = input().split()
    ans = sqrt(int(a + b))
    print('Yes' if ans.is_integer() else 'No')
    return

if __name__ == '__main__':
    main()
