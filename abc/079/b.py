import sys
input = sys.stdin.readline
def main():
    n = int(input())
    ryuka = []
    ryuka.append(2)
    ryuka.append(1)
    for i in range(2, n+1):
        ryuka.append(ryuka[i-1]+ryuka[i-2])
    print(ryuka[-1])
    return

if __name__ == '__main__':
    main()
