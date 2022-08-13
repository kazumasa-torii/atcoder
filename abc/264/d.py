import sys
input = sys.stdin.readline
def main():
    n = 'atcoder'
    s = list(input().strip())
    ans = 0
    for i in n:
        idx = s.index(i)
        ans += idx
        del s[idx]
    print(ans)
    return

if __name__ == '__main__':
    main()
