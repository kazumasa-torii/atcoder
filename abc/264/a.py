import sys
input = sys.stdin.readline
def main():
    s = 'atcoder'
    l, r = map(int, input().split())
    l -= 1
    print(s[l:r])
    return

if __name__ == '__main__':
    main()
