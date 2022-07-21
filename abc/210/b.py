import sys
input = sys.stdin.readline
def main():
    n = int(input())
    s = input().strip()
    for i in range(n):
        if s[i] == '1':
            if i % 2 == 0:
                print('Takahashi')
                exit()
            else:
                print('Aoki')
                exit()
    return

if __name__ == '__main__':
    main()
