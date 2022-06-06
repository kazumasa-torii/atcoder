import sys
input = sys.stdin.readline

def main():
    li = []
    amari = []
    for _ in range(5):
        tmp = int(input())
        li.append(tmp // 10)
        if tmp % 10 != 0:
            amari.append(tmp % 10)
    amari.sort()
    index = 0
    if len(amari) != 0:
        for i in amari:
            index += 1

    print(min(amari) + (sum(li) + index) * 10)

main()
