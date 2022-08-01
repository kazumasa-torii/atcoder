import sys
input = sys.stdin.readline
def main():
    y = int(input())
    x = y % 4
    if x == 3:
        print(y-1+4)
    elif x == 2:
        print(y)
    elif x == 1:
        print(y+1)
    elif x == 0:
        print(y+2)
    return

if __name__ == '__main__':
    main()
