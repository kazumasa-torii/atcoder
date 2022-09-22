import sys
input = sys.stdin.readline
def main():
    a = [list(map(int, input().split())) for i in range(3)]
    x = [0] * 3
    y = [0] * 3
    for i in range(3): y[i] = a[0][i] - x[0]
    for i in range(3): x[i] = a[i][0] - y[0]
    good = True
    for i in range(3):
        for j in range(3):
            if x[i] + y[j] != a[i][j]: good = False
    print('Yes' if good else 'No')
    return

if __name__ == '__main__':
    main()