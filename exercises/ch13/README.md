# 第13章　ファイル処理　練習問題

[← 目次に戻る](../../README.md)　／　[解答例・解説](../../explanations/ch13/README.md)

ファイルを開くときは `with open(ファイル名, モード, encoding='utf-8') as f:` の形を基本にしましょう。プログラムを作る問題は、このフォルダにある score.txt を使います。PyCharm で実行するときは、作業ディレクトリがこのフォルダになっているか確認しましょう。

> 📝 マークの問題は、このフォルダの .py ファイルにプログラムを書きます。書けたら、プロジェクトのフォルダで `python tools/check.py ch13` を実行してチェックしましょう。

## 13-1　ファイル処理の基礎

### 問1　open のモードについて、次の目的に合うモードを答えなさい。

（1）ファイルを読み込む  
（2）新しく書き込む（あれば中身を消して最初から）  
（3）今の内容の末尾に書き足す  
（4）画像ファイルを読み込む  

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

---

### 問4　with 文

次のプログラムを with 文を使って書き直しなさい。また、with 文を使う利点を説明しなさい。

```python
f = open('memo.txt', encoding='utf-8')
print(f.read())
f.close()
```

---

## 13-2　バイナリファイル

### 問5　次の式の結果を答えなさい。

（1）`len('abc'.encode('utf-8'))`  
（2）`len('あいう'.encode('utf-8'))`  
（3）`len('あいう')`  
（4）`b'\x41\x42'.decode()`  

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

> 📝 解答ファイル：[`exercises/ch13/q06_score_file.py`](./q06_score_file.py)

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

> 📝 解答ファイル：[`exercises/ch13/q07_safe_read.py`](./q07_safe_read.py)

---

### 問8　（発展）合格者をファイルに書き出す

score.txt を読み込み、70点以上の人の名前に番号を付けて passed.txt に書き出すプログラムを作りなさい。書き出したあと、passed.txt を読み込んで内容を表示しなさい。

**passed.txt（表示される内容）**

```text
1. 佐藤
2. 高橋
3. 田中
```

> 📝 解答ファイル：[`exercises/ch13/q08_write_passed.py`](./q08_write_passed.py)

---
