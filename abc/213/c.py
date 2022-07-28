"""
列と行で数字がある場所を残してそれを行を削除したと仮定して仮想の表に置き換える
もともとの表は不必要であり結果行と列の数値がどう変換していくのがいいか理解して対応させるのが良い

1. 列行で数字がある箇所を取得する
1. 重複がある場合は、その地点をsetで統合しておき小さい順に変更しておく
1. dictにもともとの列の数値に対して仮想の表の列の数値を関連付けておく
1. 行にも同じように対応しておく
1. 数字がある場所の数値を仮想の行と列に変換して出力させる
"""
import sys
input = sys.stdin.readline

def main():
    # 座標圧縮
    def compress(ar):
        ans = list(set(ar))
        ans.sort()

        conv = dict()
        for i in range(len(ans)):
            conv[ans[i]] = i + 1
        return conv

    h, w, n = map(int, input().split())

    li = []
    a = []
    b = []

    for i in range(n):
        x, y = map(int, input().split())
        li.append([x, y])
        a.append(x)
        b.append(y)

    xconv = compress(a)
    yconv = compress(b)

    for x, y in li:
        print(xconv[x], yconv[y])
    return

if __name__ == '__main__':
    main()
