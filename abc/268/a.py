import sys
input = sys.stdin.readline

def main():
    print(len(set(map(int, input().split()))))
    return

if __name__ == '__main__':
    main()