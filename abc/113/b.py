import sys
input = sys.stdin.readline
def main():
    n = int(input())
    t, a = map(int, input().split())
    h = list(map(int, input().split()))
    li = []
    for i in range(n):
        li.append(abs(t-(h[i]*0.006)-a))
    print(li.index(min(li)) + 1)
    return

if __name__ == '__main__':
    main()
