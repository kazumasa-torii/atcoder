import sys
input = sys.stdin.readline
def main():
    n = int(input())
    s = input().strip()
    dic = dict()
    for i in ('A','B'):
        dic[i] = 0

    for i in range(n):
        dic[s[i]] += 1

    if dic['A'] == dic['B']:
        print('No')
    else:
        print('Yes')
    return

if __name__ == '__main__':
    main()
