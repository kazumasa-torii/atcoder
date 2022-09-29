import sys
input = sys.stdin.readline
def main():
    s = list(input())
    s.insert(0, '')
    n = len(s)
    ans = 0
    for i in range(1, n):
        if i == 1 or i == n-1:
            ans += n-2
            continue
        up = n-i-1
        down = i-1
        if s[i] == 'U':
            ans += up
            ans += down*2
        else:
            ans += up*2
            ans += down
    print(ans)
    return

if __name__ == '__main__':
    main()