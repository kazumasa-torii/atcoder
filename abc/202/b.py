import sys
input = sys.stdin.readline

def main():
    S = list(input().strip())
    han = {'0':'0', '1':'1', '6':'9', '8':'8', '9':'6'}
    ans = []
    l = len(S)
    for i in range(l-1, -1, -1):
        ans.append(han[S[i]])
    print(''.join(ans))
    return

main()
