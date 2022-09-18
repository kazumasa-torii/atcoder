"""
ビットの部分集合問題に変換される
よくわからないので記事を読み込む予定
https://primenumber.hatenadiary.jp/entry/2016/12/01/000000
"""

def main():
    x = int(input())
    i = x
    li = []
    while True:
        li.append(i)
        if i == 0: break
        i = (i-1)&x
    li.sort()
    for i in li:
        print(i)
    return

if __name__ == '__main__':
    main()