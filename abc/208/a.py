import sys
input = sys.stdin.readline
def main():
    a, b = map(int, input().split())
    max_si = 6*a
    min_si = 1*a
    print('Yes' if max_si >= b >= min_si else 'No')
    return

if __name__ == '__main__':
    main()
