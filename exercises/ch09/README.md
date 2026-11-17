# 第9章　関数　練習問題

[← 目次に戻る](../../README.md)　／　[解答例・解説](../../explanations/ch09/README.md)

関数は「def で定義・( ) で呼び出し・return で値を返す」が基本です。引数は「名札」が渡されることを思い出しながら考えましょう。

> 📝 マークの問題は、このフォルダの .py ファイルにプログラムを書きます。書けたら、プロジェクトのフォルダで `python tools/check.py ch09` を実行してチェックしましょう。

## 9-1　関数の基礎

### 問1　次のプログラムの表示を答えなさい。

```python
def triple(x):
    return x * 3

print(triple(4))
print(triple('ab'))
print(triple(triple(1)))
```

---

### 問2　次のプログラムの表示を答えなさい。

```python
def hello():
    print('こんにちは')

r = hello()
print(r)
```

---

### 問3　次のプログラムの表示を答えなさい。

```python
def add1(x):
    x += 1

def add_item(a):
    a.append(1)

n = 10
add1(n)
lst = [0]
add_item(lst)
print(n, lst)
```

---

### 問4　次の関数について、各呼び出しの表示を答えなさい。

```python
def greet(name, msg='こんにちは'):
    print(f'{msg}、{name}さん')
```

（1）`greet('佐藤')`  
（2）`greet('佐藤', 'おはよう')`  
（3）`greet(msg='こんばんは', name='鈴木')`  

---

### 問5　次のプログラムの表示を答えなさい。

```python
def total(*args):
    return sum(args)

print(total())
print(total(1, 2, 3))
nums = [4, 5]
print(total(*nums))
```

---

### 問6　再帰呼出し

1 から n までの和を、くり返し（for や while）を使わずに再帰呼出しで求める関数 `sum_to(n)` を作りなさい。`sum_to(5)` は 15 になります。

---

## 9-2　文書化文字列とアノテーション／9-3　名前空間とスコープ

### 問7　次の関数に、文書化文字列（docstring）とアノテーション（型ヒント）を付けなさい。

```python
def is_even(n):
    return n % 2 == 0
```

---

### 問8　次のプログラムの表示を答えなさい。

```python
x = 10

def f():
    x = 20

def g():
    global x
    x = 30

f()
print(x)
g()
print(x)
```

---

## 9-4　高階関数／9-5　ラムダ式

### 問9　次の式の結果を答えなさい。

（1）`list(map(lambda x: x * 2, [1, 2, 3]))`  
（2）`list(filter(lambda x: x % 2 == 0, range(10)))`  
（3）`sorted(['banana', 'kiwi', 'apple'], key=len)`  
（4）`sorted([('A', 80), ('B', 95), ('C', 70)], key=lambda t: t[1])`  

---

## 応用問題（プログラムを作る）

### 問10　3つの値の最大値を返す関数

3つの整数を受け取り、最大値を返す関数 `max3(a, b, c)` を、組込み関数 max を使わずに作りなさい。また、その関数を使って、入力した3つの整数の最大値を表示しなさい。

**実行例**

```text
a：3
b：9
c：5
最大値は9です
```

> 📝 解答ファイル：[`exercises/ch09/q10_max3.py`](./q10_max3.py)

---

### 問11　素数の一覧

整数 n が素数なら True を返す関数 `is_prime(n)` を作りなさい。また、その関数を使って、入力した数までの素数をスペース区切りで表示しなさい。

**実行例**

```text
いくつまで：20
2 3 5 7 11 13 17 19
```

> 📝 解答ファイル：[`exercises/ch09/q11_primes.py`](./q11_primes.py)

---

### 問12　（発展）成績の評価

点数を受け取り、90点以上は 'A'、80点以上は 'B'、60点以上は 'C'、それ以外は 'D' を返す関数 `grade(score)` を作りなさい。また、スペース区切りで入力した点数の評価を表示し、map を使って A の人数を数えなさい。

**実行例**

```text
点数をスペース区切りで：95 82 67 40 90
 95点：A
 82点：B
 67点：C
 40点：D
 90点：A
A の人数：2
```

> 📝 解答ファイル：[`exercises/ch09/q12_grades.py`](./q12_grades.py)

---
