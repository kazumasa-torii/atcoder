import sys
input = sys.stdin.readline
def main():
    a, b = map(int, input().split())
    mcnt = 0
    if a < 0 and b > 0:exit(print('Zero'))
    for i in range(a, b + 1):
        if i < 0: mcnt += 1
    print('Positive' if mcnt % 2 == 0 else 'Negative')
    return

if __name__ == '__main__':
    main()
