import sys
input = sys.stdin.readline

def main():
    li = []
    for _ in range(5):
        li.append(int(input()))
    k = int(input())
    print(':(' if abs(min(li) - max(li)) > k else 'Yay!')

main()
