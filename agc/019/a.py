import sys
input = sys.stdin.readline

def main():
    q, h, s, d = map(int, input().split())
    q, h = q*4, h*2
    m1 = min(q, h, s)
    n = int(input())
    ans = 0
    if n > 2:
        m2 = min(m1*2, d)
        ans = ans + ((n//2)*m2)
        n = n % 2
    ans = ans + m1*n
    print(ans)
    return

if __name__ == '__main__':
    main()