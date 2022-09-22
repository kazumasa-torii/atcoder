import sys
input = sys.stdin.readline

def main():
    n = int(input())
    a = list(map(int, input().split()))
    upFlag = False
    downFlag = False
    check = a[0]
    ans = 1

    for i in range(1, n):
        if check == a[i]:continue
        elif check < a[i]:
            upFlag = True
            check = a[i]
        else:
            downFlag = True
            check=a[i]
        if upFlag and downFlag:
            upFlag, downFlag = False, False
            ans += 1

    print(ans)
    return

if __name__ == '__main__':
    main()