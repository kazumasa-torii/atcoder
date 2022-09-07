def main():
    S = list(input())
    ans = 0
    b = 0
    for i in S:
        if i == "W": ans += b
        else: b += 1
    print(ans)
    return

if __name__ == '__main__':
    main()