import sys
input = sys.stdin.readline
def main():
    n, y = map(int, input().split())
    man = 10000
    fsen = 5000
    sen = 1000

    for i in range(n+1):
        for j in range(n+1):
            if i + j > n: break
            if (man * i) + (fsen * j) + (sen * (n-(i+j))) == y:exit(print(i, j, (n-(i+j))))
    print(-1, -1, -1)
    return

if __name__ == '__main__':
    main()