import sys
input = sys.stdin.readline
def main():
    cnt = 0
    n = int(input())
    for i in map(int, input().split()):
        while i%2==0:
            i = i/2
            cnt = cnt + 1
    print(cnt)
    return

if __name__ == '__main__':
    main()
