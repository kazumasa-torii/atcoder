import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = list(map(int, input().split()))
    acc = [0]
    tmp = a[0]
    for i in range(1, n):
        if a[i] <= tmp: acc.append(acc[-1] + 1)
        else:acc.append(0)
        tmp = a[i]
    print(max(acc))
    return

if __name__ == '__main__':
    main()
