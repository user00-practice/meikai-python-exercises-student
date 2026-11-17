# 第13章　ファイル処理　解答例・解説

[← 目次に戻る](../../README.md)　／　[問題](../../exercises/ch13/README.md)

## 13-1　ファイル処理の基礎

### 問1　open のモードについて、次の目的に合うモードを答えなさい。

（1）ファイルを読み込む  
（2）新しく書き込む（あれば中身を消して最初から）  
（3）今の内容の末尾に書き足す  
（4）画像ファイルを読み込む  

#### 解答例

（1）`'r'`（省略してもよい）　（2）`'w'`　（3）`'a'`　（4）`'rb'`

#### 解説

`'w'` は既存のファイルの中身を消してしまうので注意が必要です。書き足すなら `'a'` を使います。

---

### 問2　memo.txt の内容が次のとき、各プログラムの表示（または結果）を答えなさい。

**memo.txt**

```text
1行目
2行目
3行目
```

**（1）**

```python
with open('memo.txt', encoding='utf-8') as f:
    print(f.readline())
```

**（2）**

```python
with open('memo.txt', encoding='utf-8') as f:
    print(f.readlines())
```

**（3）**

```python
with open('memo.txt', encoding='utf-8') as f:
    for line in f:
        print(line.rstrip())
```

#### 解答例

**（1）（改行が2回出るので、空の行が入る）**

```text
1行目

```

**（2）**

```text
['1行目\n', '2行目\n', '3行目\n']
```

**（3）**

```text
1行目
2行目
3行目
```

#### 解説

読み込んだ行の末尾には改行 `\n` が付いています。（1）は、その改行と print の改行で、空の行が1行入ります。

（3）`rstrip()` で末尾の改行を取り除いてから表示しています。ファイルを1行ずつ処理するときの定番の書き方です。

---

### 問3　次のプログラムを順に実行したあとの log.txt の内容を答えなさい（log.txt は最初はないものとします）。

```python
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('A\n')
with open('log.txt', 'a', encoding='utf-8') as f:
    f.write('B\n')
with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('C\n')
with open('log.txt', 'a', encoding='utf-8') as f:
    print('D', file=f)
```

#### 解答例

```text
C
D
```

#### 解説

3回目の `'w'` で、それまでの A と B は消えます。そのあと `'a'` で D が書き足されます。

`print(…, file=f)` はファイルに書き込みます。print なので改行は自動で付きます。

---

### 問4　with 文

次のプログラムを with 文を使って書き直しなさい。また、with 文を使う利点を説明しなさい。

```python
f = open('memo.txt', encoding='utf-8')
print(f.read())
f.close()
```

#### 解答例

```python
with open('memo.txt', encoding='utf-8') as f:
    print(f.read())
```

利点：with のブロックが終わると、ファイルが自動的に閉じられる。途中で例外が起きても必ず閉じられるので、close() の書き忘れがない。

#### 解説

ファイルを閉じ忘れると、書き込んだ内容が保存されないことがあります。ファイル処理は with 文で書くのが基本です。

---

## 13-2　バイナリファイル

### 問5　次の式の結果を答えなさい。

（1）`len('abc'.encode('utf-8'))`  
（2）`len('あいう'.encode('utf-8'))`  
（3）`len('あいう')`  
（4）`b'\x41\x42'.decode()`  

#### 解答例

（1）`3`　（2）`9`　（3）`3`　（4）`'AB'`

#### 解説

UTF-8 では、英数字は1バイト、ひらがなは1文字3バイトです。文字数（len）とバイト数は同じとは限りません。

（4）16進数の 41 は 'A'、42 は 'B' の文字コードです。

---

## 応用問題（プログラムを作る）

### 問6　ファイルを使った成績処理

「名前,点数」の形で1行ずつ書かれた score.txt を読み込み、1人ずつ表示したあと、人数・合計・平均を表示するプログラムを作りなさい。

**score.txt**

```text
佐藤,80
鈴木,65
高橋,90
田中,72
```

**実行結果**

```text
佐藤：80点
鈴木：65点
高橋：90点
田中：72点
人数 4　合計 307　平均 76.8
```

#### 解答例

```python
total = 0
count = 0
with open('score.txt', encoding='utf-8') as f:
    for line in f:
        name, score = line.rstrip().split(',')
        score = int(score)
        print(f'{name}：{score}点')
        total += score
        count += 1
print(f'人数 {count}　合計 {total}　平均 {total / count:.1f}')
```

#### 解説

1行ずつ読み、`rstrip()` で改行を取り、`split(',')` でカンマで分けて、名前と点数にアンパックします。

点数は文字列として読み込まれるので、計算する前に `int()` で変換します。

このようなカンマ区切りの形式を CSV といいます。本格的に扱うなら標準ライブラリの csv モジュールを使います。

---

### 問7　ファイルがないときの対処

ファイル名を入力すると、そのファイルの行数を表示するプログラムを作りなさい。ファイルがないときは「〇〇 が見つかりません」と表示しなさい。

**実行例**

```text
ファイル名：score.txt
score.txt は 4 行です

ファイル名：nothing.txt
nothing.txt が見つかりません
```

#### 解答例

```python
name = input('ファイル名：')
try:
    with open(name, encoding='utf-8') as f:
        lines = f.readlines()
except FileNotFoundError:
    print(f'{name} が見つかりません')
else:
    print(f'{name} は {len(lines)} 行です')
```

#### 解説

ファイルがないと FileNotFoundError になります。第12章の try / except で対処します。

実習でよくある原因は、ファイル名の打ち間違いと、PyCharm の作業ディレクトリが違うことです。

---

### 問8　（発展）合格者をファイルに書き出す

score.txt を読み込み、70点以上の人の名前に番号を付けて passed.txt に書き出すプログラムを作りなさい。書き出したあと、passed.txt を読み込んで内容を表示しなさい。

**passed.txt（表示される内容）**

```text
1. 佐藤
2. 高橋
3. 田中
```

#### 解答例

```python
PASS_LINE = 70

passed = []
with open('score.txt', encoding='utf-8') as f:
    for line in f:
        name, score = line.rstrip().split(',')
        if int(score) >= PASS_LINE:
            passed.append(name)

with open('passed.txt', 'w', encoding='utf-8') as f:
    for i, name in enumerate(passed, 1):
        print(f'{i}. {name}', file=f)

with open('passed.txt', encoding='utf-8') as f:
    print(f.read(), end='')
```

#### 解説

読み込み・処理・書き出しの3つに分けて書くと、わかりやすくなります。

合格点を定数 PASS_LINE にしておくと、基準が変わっても1か所直すだけで済みます。

これまでの章の内容（定数・if文・リスト・enumerate・f文字列）を総合的に使っています。

---
