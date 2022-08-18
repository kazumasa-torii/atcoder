import sys
input = sys.stdin.readline
def main():
    a, b = map(int, input().split())
    ans = 0
    for i in range(a, b+1):
        tmp = str(i)
        pre_one = tmp[0]
        rear_one = tmp[-1]
        pre_two = tmp[1]
        rear_two = tmp[-2]
        if pre_one == rear_one and pre_two == rear_two: ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
