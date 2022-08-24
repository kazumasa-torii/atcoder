import sys
input = sys.stdin.readline
def main():
    n = int(input())
    i = 1
    table = []
    while i * i <= n:
        if n%i == 0:
            table.append(i)
            table.append(n//i)
        i += 1
    table = list(set(table))
    table.sort()
    ans = int(1e19)
    for i in table:
        tmp = n // i
        tmp = tmp + i
        tmp = tmp - 2
        ans = min(ans, tmp)
    print(ans)
    return

if __name__ == '__main__':
    main()
