"""
実際は、各軸の中間地点を取得するみたいな内容に言い換えられる
Hが目標地点
∑|Xi - XH|+|Yi - YH|
は言い換えれば
∑|Xi - XH| と ∑|Yi - YH|に分けることができる
ならば二次元の問題から一次元に言い換えることができる

ここまでできたら後は、各軸でリストを作成して中間地点を取得
その後各項目からマンハッタン距離を取得して答えに追加していけば終わり
"""
def main():
    def solve(Values):
        Values.sort()
        middle = len(Values) // 2
        h = Values[middle]
        return sum(abs(h-val) for val in Values)

    N = int(input())
    Xs = []
    Ys = []

    for _ in range(N):
        x, y = map(int, input().split())
        Xs.append(x)
        Ys.append(y)

    print(solve(Xs)+solve(Ys))
    return

main()
