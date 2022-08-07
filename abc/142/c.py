import sys
input = sys.stdin.readline
def main():
    n = int(input())
    li = list(map(int, input().split()))
    dic = dict()
    for i in range(n):
        dic[i] = li[i]
    dic = sorted(dic.items(), key=lambda x:x[1])
    ans = []
    for i in range(n):
        x, y = dic[i]
        ans.append(x + 1)
    print(*ans)
    return

if __name__ == '__main__':
    main()
