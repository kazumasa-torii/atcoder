import sys
input = sys.stdin.readline
def main():
    dic = dict()
    s = input().strip()
    for i in range(97, 97+26):
        dic[chr(i)] = 0

    for i in list(s):
        dic[i] += 1

    for v, i in enumerate(dic):
        if dic[i] == 0:
            exit(print(i))
    print('None')
    return

if __name__ == '__main__':
    main()
