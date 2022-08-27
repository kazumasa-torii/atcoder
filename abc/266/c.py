import sys
input = sys.stdin.readline
def main():
    li = [list(map(int, input().split())) for _ in range(4)]
    for i in range(4):
        for j in range(2):
            if li[i][j] < 0:li[i][j] = -li[i][j]
    flag = True

    #a 比べる対象 b,d
    if (-li[0][0] <= li[3][0] <= li[0][0] and -li[0][0] <= li[0][0] <= li[1][0]) or (-li[0][1] <= li[3][1] <= li[0][1] and -li[0][1] <= li[1][1] <= li[0][1]):pass
    else:flag=False

    #b 比べる対象 a,c
    if (-li[1][0] <= li[0][0] <= li[1][0] and -li[1][0] <= li[2][0] <= li[1][0]) or (-li[1][1] <= li[0][1] <= li[1][1] and -li[1][1] <= li[2][1] <= li[1][1]):pass
    else:flag=False

    #c 比べる対象 b,d
    if (-li[2][0] <= li[1][0] <= li[2][0] and -li[2][0] <= li[3][0] <= li[1][0]) or (-li[2][1] <= li[1][1] <= li[2][1] and -li[2][1] <= li[3][1] <= li[2][1]):pass
    else:flag=False

    #d 比べる対象 a,c
    if (-li[3][0] <= li[0][0] <= li[3][0] and -li[3][0] <= li[2][0] <= li[1][0]) or (-li[3][1] <= li[0][1] <= li[3][1] and -li[3][1] <= li[2][1] <= li[3][1]):pass
    else:flag=False
    print('Yes' if flag else 'No')

    return

if __name__ == '__main__':
    main()
