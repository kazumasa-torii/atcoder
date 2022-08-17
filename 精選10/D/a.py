import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    ans = 0
    for i in a:
        if i % 2 != 0:exit(print(0))
    while True:
        tmp = []
        for i in range(n):
            a[i] /= 2
            tmp.append(a[i].is_integer())
        if not all(tmp): break
        ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
