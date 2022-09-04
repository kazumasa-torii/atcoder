"""
実際の暗証番号はたかだか3桁なので000～999までの全通りを試す
そしてそれを与えられた番号から抽出できるかを全探索すればOK
計算量は 1000*30000 なので間に合う
"""
def main():
    n = int(input())
    s = list(input())
    cnt = 0
    for i in range(1000):
        # 使用する番号を作成
        num = str(i).zfill(3)
        # 暗証番号の何番目まで取り出せているのかを管理
        process = 0
        for j in range(n):
            # 暗証番号のn番目とラッキーナンバーのj番目があっていれば暗証番号の桁数を進める
            if process <= 2 and num[process] == s[j]: process += 1
        if process == 3: cnt += 1
    print(cnt)
    return

if __name__ == '__main__':
    main()