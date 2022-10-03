import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n = int(input())
    n = '{:02x}'.format(n)
    print(n.upper())
    return

if __name__ == '__main__':
    main()