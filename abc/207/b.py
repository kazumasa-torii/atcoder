import sys
input = sys.stdin.readline
def main():
    a, b, c, d = map(int,input().split())
    for i in range(10 ** 7) :
        if a + i * b <= c * i * d :
            print(i)
            exit()
    print(-1)
    return

if __name__ == '__main__':
    main()
