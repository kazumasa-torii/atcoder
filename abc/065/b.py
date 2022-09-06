import sys
input = sys.stdin.readline
def main():
    n = int(input())
    a = [int(input()) - 1 for _ in range(n)]
    memo = [False] * n
    button = 0
    while True:
        if memo[button]:break
        if memo[1]:break
        memo[button] = True 
        button = a[button]
    print(sum(memo) - 1 if memo[1] else -1)
    return

if __name__ == '__main__':
    main()