import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = list(map(int, input().split()))
    li.insert(0, 0)
    tmp = li[-1]
    cnt = 0
    while tmp != 0:
        cnt += 1
        tmp = li[tmp-1]
    print(cnt)
    return

if __name__ == '__main__':
    main()
