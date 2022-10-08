import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def main():
    n = int(input())
    print(sum(list(map(int, input().split()))))
    return

if __name__ == '__main__':
    main()