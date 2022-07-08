import sys
input = sys.stdin.readline

def main():
    A, B, C = map(int, input().split())
    ans = str()
    if A == 0 and B == 0:
        ans = '='
    elif A == 0 and B > 0:
        ans = '<'
    elif B == 0 and A > 0:
        ans = '>'
    elif C % 2 == 0:
        if A < 0:
            A *= -1
        if B < 0:
            B *= -1
    if A < B:
        ans = '<'
    elif A > B:
        ans = '>'
    elif A == B:
        ans = '='


    print(ans)
    return

if __name__ == '__main__':
    main()
