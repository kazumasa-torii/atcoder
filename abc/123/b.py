import sys
input = sys.stdin.readline
def main():
    li = []
    li.append(int(input()))
    li.append(int(input()))
    li.append(int(input()))
    li.append(int(input()))
    li.append(int(input()))
    mn = int(1e19)
    for i in li:
        tmp = str(i)
        tmp = tmp[-1]
        if tmp == '0': continue
        mn = min(int(tmp), mn)
    total = 0
    for i in li:
        tmp = i // 10
        amari = i % 10
        if amari != 0: tmp += 1
        total += tmp
    total *= 10
    if mn != int(1e19):
        total += mn
        total -= 10
    print(total)
    return

if __name__ == '__main__':
    main()
