import sys
input = sys.stdin.readline
def main():
    a, b = map(int, input().split())
    print('Even' if (a*b)%2 == 0 else 'Odd')
    return

if __name__ == '__main__':
    main()
