"""
貪欲法にて対応
"""
def main():
    n, a, b, c, d = map(int, input().split())
    s = input()
    for i in range(a, max(c, d)):
        if s[i-1:i+1] == '##':exit(print('No'))
    if c < d: exit(print('Yes'))
    for i in range(b-1, d):
        if s[i-1:i+2] == '...':exit(print('Yes'))
    print('No')
    return

if __name__ == '__main__':
    main()