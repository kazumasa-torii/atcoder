import sys
input = sys.stdin.readline

def main():
    a, b, c, d = map(int, input().split())
    print((a+b) * (c-d))
    print("Takahashi")
    return

if __name__ == '__main__':
    main()