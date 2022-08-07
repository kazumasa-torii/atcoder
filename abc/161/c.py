import sys
input = sys.stdin.readline
def main():
    n, k = map(int, input().split())
    a = n % k
    print(min(a, k-a))
    return

if __name__ == '__main__':
    main()
