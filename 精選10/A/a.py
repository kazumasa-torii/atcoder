import sys
input = sys.stdin.readline
def main():
    a = int(input())
    b, c = map(int, input().split())
    s = input().strip()

    print(f'{a+b+c} {s}')
    return

if __name__ == '__main__':
    main()
