import sys
input = sys.stdin.readline

def main():
    a, b, c = map(int, input().split())
    tmp = a
    for i in range(100):
        tmp += a
        if tmp % b == c: exit(print('YES'))
    print('NO')
    return

if __name__ == '__main__':
    main()