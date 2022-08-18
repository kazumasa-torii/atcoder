import sys
input = sys.stdin.readline
def main():
    a = int(input())
    b = int(input())
    if a > b: print('GREATER')
    elif a < b: print('LESS')
    else: print('EQUAL')
    return

if __name__ == '__main__':
    main()
