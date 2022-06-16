import sys
input = sys.stdin.readline

def main():
    W, H, x, y = map(float, input().split())
    ans = W*H/2
    num = 1 if W==x*2 and H==y*2 else 0
    print(ans, num)
    return

main()
