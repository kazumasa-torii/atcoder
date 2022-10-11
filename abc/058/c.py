"""
各Alphabetに対して配列を作成しておく
各文字の文字の個数をカウントしておきそこから最小値を取得
その後最小値を文字列に連結させて答えを出力
"""
def main():
    n = int(input())
    a = [[0] * n for _ in range(26)]
    for i in range(n):
        for j in list(input()):
            a[ord(j) - 97][i] += 1
    
    ans = str()
    for i in range(26):
        ans += min(a[i]) * chr(i+97)
    print(ans)
    return

if __name__ == '__main__':
    main()