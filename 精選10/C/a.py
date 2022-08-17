import sys
input = sys.stdin.readline
def main():
    s = input().strip()
    ans = 0
    for i in list(s):
        if i == '1': ans += 1
    print(ans)
    return

if __name__ == '__main__':
    main()
