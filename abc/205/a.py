import sys
input = sys.stdin.readline

def main():
    A, B = map(int, input().split())
    ans = (A/100) * B
    if ans % 2 == 0:
        print(int(ans))
    else:
        print(ans)
    return

main()
