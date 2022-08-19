import sys
input = sys.stdin.readline
def main():
    a, b = map(int, input().split())
    for i in range(10000):
        if (i*8)//100 == a and (i*10)//100 == b:exit(print(i))
    print(-1)
    return

if __name__ == '__main__':
    main()
