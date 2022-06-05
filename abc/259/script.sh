#!/bin/sh
# 第一引数 問題番号
#  cd abc/190

# 現在のパスを取得
path=$(cd $(dirname $0); pwd)

# コンテストレベル
contestLevel=${path##*atcoder/}
contestLevel=${contestLevel%/*}

# コンテスト番号
contestNumber=$(echo "$path" | sed -e 's/.*\/\([^\/]*\)$/\1/')

# 問題番号
questionNumber="$1"

# AtCoderのURL
URL="https://atcoder.jp/contests/${contestLevel}${contestNumber}/tasks/${contestLevel}${contestNumber}_${questionNumber}"

# サンプルデータダウンロード
oj login "${URL}"
oj dl "${URL}"


echo ""
echo "---------------情報----------------------"

echo "パス : "${path}
echo "大会レベル : "${contestLevel}
echo "大会番号 : "${contestNumber}
echo "問題番号 : "${questionNumber}
echo "URL : "${URL}
echo ""

# サンプルテスト
oj t -c "python ${questionNumber}.py"

# 新しくできたファイルを削除
rm -f a.out
rm -rf test
