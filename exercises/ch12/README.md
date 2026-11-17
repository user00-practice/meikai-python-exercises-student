# 第12章　例外処理　練習問題

[← 目次に戻る](../../README.md)　／　[解答例・解説](../../explanations/ch12/README.md)

エラーメッセージ（トレースバック）は、いちばん下の行（例外の種類と原因）から読みましょう。except では、対処できる例外を具体的な種類で指定するのが原則です。

> 📝 マークの問題は、このフォルダの .py ファイルにプログラムを書きます。書けたら、プロジェクトのフォルダで `python tools/check.py ch12` を実行してチェックしましょう。

## 12-1　例外処理

### 問1　次のプログラムを実行すると、どの例外が起きますか。

（1）`int('abc')`  
（2）`[1, 2][5]`  
（3）`{'a': 1}['b']`  
（4）`10 / 0`  
（5）`'a' + 1`  
（6）`open('nothing.txt')`（ファイルがないとき）  

---

### 問2　次のトレースバックを読んで、①例外の種類、②原因、③例外が起きた行番号と関数名を答えなさい。

```python
Traceback (most recent call last):
  File "main.py", line 5, in <module>
    print(average([]))
  File "main.py", line 2, in average
    return sum(a) / len(a)
ZeroDivisionError: division by zero
```

---

### 問3　次のプログラムで、n に 0 を入力したときと 2 を入力したときの表示をそれぞれ答えなさい。

```python
n = int(input('整数：'))
try:
    x = 10 / n
except ZeroDivisionError:
    print('0 では割れません')
else:
    print('結果：', x)
finally:
    print('終了')
```

---

### 問4　次のプログラムでは、整数でない文字を入力しても「整数を入力してください」と表示されず、「エラーです」と表示されます。理由を説明し、正しく直しなさい。

```python
try:
    n = int(input('整数：'))
    print(10 / n)
except Exception:
    print('エラーです')
except ValueError:
    print('整数を入力してください')
except ZeroDivisionError:
    print('0 では割れません')
```

---

### 問5　年齢が 0 未満のときに ValueError を送出する関数 `check_age(age)` を作りなさい。また、その例外をつかまえてメッセージを表示する呼び出し側のプログラムも書きなさい。

**check_age(-5) を呼んだときの表示**

```text
エラー：年齢が負です：-5
```

---

### 問6　ユーザ定義の例外

残高不足を表す自作の例外クラス `InsufficientFundsError` を定義しなさい。

---

## 応用問題（プログラムを作る）

### 問7　正しく入力されるまでくり返す

整数が正しく入力されるまで何度でも入力させ、入力された整数の2倍を表示するプログラムを作りなさい。

**実行例**

```text
整数：abc
整数を入力してください
整数：3.5
整数を入力してください
整数：7
7 の2倍は 14 です
```

> 📝 解答ファイル：[`exercises/ch12/q07_input_int.py`](./q07_input_int.py)

---

### 問8　割り算の電卓

2つの整数を入力し、割り算の結果を小数点以下2桁で表示するプログラムを作りなさい。整数以外が入力されたときは「整数を入力してください」、0 で割ろうとしたときは「0 では割れません」と表示し、最後に必ず「計算を終わります」と表示しなさい。

**実行例**

```text
割られる数：10
割る数：3
10 ÷ 3 = 3.33
計算を終わります
```

> 📝 解答ファイル：[`exercises/ch12/q08_divide.py`](./q08_divide.py)

---

### 問9　（発展）自作の例外を使う

問6の InsufficientFundsError を使い、残高と金額を受け取って、引き出したあとの残高を返す関数 `withdraw(balance, amount)` を作りなさい。金額が負なら ValueError、残高より多ければ InsufficientFundsError を送出します。次のように、いろいろな金額で試しなさい。

**使い方**

```python
balance = 1000
for amount in [300, 3000, -5, 200]:
    try:
        balance = withdraw(balance, amount)
        print(f'{amount}円引き出しました。残高 {balance}円')
    except InsufficientFundsError as e:
        print('エラー：', e)
    except ValueError as e:
        print('入力エラー：', e)
```

**実行結果**

```text
300円引き出しました。残高 700円
エラー： 残高不足：あと2300円
入力エラー： 金額が負です
200円引き出しました。残高 500円
```

> 📝 解答ファイル：[`exercises/ch12/q09_custom_exception.py`](./q09_custom_exception.py)

---
