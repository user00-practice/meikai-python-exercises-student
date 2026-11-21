# 新・明解Python入門（第2版）練習問題

書籍『新・明解Python入門（第2版）』の各章に対応した練習問題と、解答例・解説です。
問題文・解答例・解説はすべて Markdown で書かれていて、PyCharm や GitHub でそのまま読めます。

> このリポジトリは、講師のリポジトリから GitHub Actions で自動的に作られています。
> 直接 push しても、次の更新で上書きされるので注意してください。
> 自分の解答を GitHub に保存したいときは、講師の指示に従ってください。

- 全13章・140問（うちプログラム作成問題 36問）
- Python 3.11 以降で動きます

## 章の一覧

| 章 | タイトル | 問題 | 解答例・解説 | 問題数 | プログラム作成 |
| --- | --- | --- | --- | --- | --- |
| 第1章 | Pythonをはじめよう！ | [問題](exercises/ch01/README.md) | [解答例・解説](explanations/ch01/README.md) | 12 | 0 |
| 第2章 | 画面への表示とキーボードからの入力 | [問題](exercises/ch02/README.md) | [解答例・解説](explanations/ch02/README.md) | 12 | 4 |
| 第3章 | プログラムの流れの分岐 | [問題](exercises/ch03/README.md) | [解答例・解説](explanations/ch03/README.md) | 15 | 3 |
| 第4章 | プログラムの流れの繰返し | [問題](exercises/ch04/README.md) | [解答例・解説](explanations/ch04/README.md) | 13 | 4 |
| 第5章 | オブジェクトと型 | [問題](exercises/ch05/README.md) | [解答例・解説](explanations/ch05/README.md) | 10 | 2 |
| 第6章 | 文字列 | [問題](exercises/ch06/README.md) | [解答例・解説](explanations/ch06/README.md) | 11 | 3 |
| 第7章 | リスト | [問題](exercises/ch07/README.md) | [解答例・解説](explanations/ch07/README.md) | 11 | 3 |
| 第8章 | タプルと辞書と集合 | [問題](exercises/ch08/README.md) | [解答例・解説](explanations/ch08/README.md) | 10 | 3 |
| 第9章 | 関数 | [問題](exercises/ch09/README.md) | [解答例・解説](explanations/ch09/README.md) | 13 | 3 |
| 第10章 | モジュールとパッケージ | [問題](exercises/ch10/README.md) | [解答例・解説](explanations/ch10/README.md) | 6 | 2 |
| 第11章 | クラス | [問題](exercises/ch11/README.md) | [解答例・解説](explanations/ch11/README.md) | 10 | 3 |
| 第12章 | 例外処理 | [問題](exercises/ch12/README.md) | [解答例・解説](explanations/ch12/README.md) | 9 | 3 |
| 第13章 | ファイル処理 | [問題](exercises/ch13/README.md) | [解答例・解説](explanations/ch13/README.md) | 8 | 3 |

## フォルダの構成

```
meikai-python-exercises-student/
├── README.md            このファイル（目次）
├── exercises/           問題と、プログラムを書くためのファイル
│   ├── ch01/
│   │   └── README.md    第1章の問題
│   ├── ch02/
│   │   ├── README.md    第2章の問題
│   │   ├── q09_greeting.py   ← ここにプログラムを書く
│   │   └── …
│   └── …
├── explanations/        解答例・解説
│   ├── ch01/README.md
│   └── …
└── tools/
    ├── check.py         プログラム作成問題の自動チェック
    └── tests.json       チェック用の入力と期待される表示
```

## PyCharm でクローンする

1. PyCharm を起動し、ようこそ画面の［VCS から取得］をクリックします。
   （プロジェクトを開いている場合は、メニューの［Git］→［クローン…］）
2. ［URL］にこのリポジトリの URL を入力し、［ディレクトリー］に保存先を指定して［クローン］をクリックします。
3. プロジェクトが開いたら、左のプロジェクトツールウィンドウで `exercises/ch01/README.md` を開きます。
   PyCharm では Markdown がプレビュー表示されます（エディターの右上でプレビューの表示方法を切り替えられます）。

## 問題の解き方

1. `exercises/chXX/README.md` を開いて問題を読みます。
2. 答えを書く問題は、ノートや配布された解答用紙などに答えを書きます。
   インタラクティブシェル（PyCharm の［Python コンソール］）で試して確かめてもかまいません。
3. プログラムを作る問題（📝 マークの付いた問題）は、指定された `.py` ファイルを開いて、プログラムを書きます。
   ファイルを右クリック →［実行］で動かしてみましょう。
4. 解き終わったら、`explanations/chXX/README.md` の解答例・解説で確かめます。
   プログラムの解答例は読むだけにして、自分のプログラムは自分で書いて動かしましょう。

## 自動チェック

プログラムを作る問題は、決められた入力を与えたときに、実行例どおりに表示されるかを自動でチェックできます。
PyCharm の［ターミナル］で、プロジェクトのフォルダで次のように実行します。

```
python tools/check.py          すべての章をチェック
python tools/check.py ch04     第4章だけチェック
```

`○` が付けば正解です。`×` のときは、期待される表示と実際の表示が並んで表示されるので、違いを確かめましょう。
全角と半角、スペースの数、`：`（全角コロン）なども正確に一致している必要があります。

## 注意

- 第13章（ファイル処理）のプログラムは、`exercises/ch13/score.txt` を読み込みます。
  PyCharm でファイルを右クリック →［実行］で実行すると、作業ディレクトリはそのファイルのあるフォルダになります。
- 自分で作るファイルに `random.py` など、標準ライブラリと同じ名前を付けないでください（第10章 問3）。
