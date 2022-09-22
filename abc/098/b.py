def main():
    n = int(input())
    s = list(input())
    ans = 0
    for i in range(n):
        cnt = 0
        one = set(s[:i])
        two = set(s[i:])
        ans = max(ans, len(one & two))        
    print(ans)
    return

if __name__ == '__main__':
    main()