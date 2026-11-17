# 第9章　関数　解答例・解説

[← 目次に戻る](../../README.md)　／　[問題](../../exercises/ch09/README.md)

## 9-1　関数の基礎

### 問1　次のプログラムの表示を答えなさい。

```python
def triple(x):
    return x * 3

print(triple(4))
print(triple('ab'))
print(triple(triple(1)))
```

#### 解答例

```text
12
ababab
9
```

#### 解説

同じ関数でも、渡す値の型によって `*` の意味（掛け算・くり返し）が変わります。

（3）内側の `triple(1)` が先に計算されて 3 になり、`triple(3)` で 9 になります。

---

### 問2　次のプログラムの表示を答えなさい。

```python
def hello():
    print('こんにちは')

r = hello()
print(r)
```

#### 解答例

```text
こんにちは
None
```

#### 解説

return がない関数は、最後まで実行すると None を返します。

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

#### 解答例

```text
10 [0, 1]
```

#### 解説

引数には名札が渡されます。int はイミュータブルなので、関数の中で `x += 1` としても呼び出し元の n は変わりません。

リストはミュータブルなので、関数の中で append すると呼び出し元の lst も変わります。

---

### 問4　次の関数について、各呼び出しの表示を答えなさい。

```python
def greet(name, msg='こんにちは'):
    print(f'{msg}、{name}さん')
```

（1）`greet('佐藤')`  
（2）`greet('佐藤', 'おはよう')`  
（3）`greet(msg='こんばんは', name='鈴木')`  

#### 解答例

（1）`こんにちは、佐藤さん`　（2）`おはよう、佐藤さん`　（3）`こんばんは、鈴木さん`

#### 解説

（1）msg を省略するとデフォルト値が使われます。（3）キーワード引数は、名前で指定するので順番を変えても渡せます。

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

#### 解答例

```text
0
6
9
```

#### 解説

定義の `*args` は、渡された引数をタプルにまとめます。何も渡さないと空のタプル `()` になり、合計は 0 です。

呼び出しの `*nums` は、リストをばらして `total(4, 5)` として渡します。

---

### 問6　再帰呼出し

1 から n までの和を、くり返し（for や while）を使わずに再帰呼出しで求める関数 `sum_to(n)` を作りなさい。`sum_to(5)` は 15 になります。

#### 解答例

```python
def sum_to(n):
    if n <= 1:
        return n
    return n + sum_to(n - 1)
```

#### 解説

`sum_to(n)` は「n ＋ 1 から n−1 までの和」なので、`n + sum_to(n - 1)` と表せます。

n が 1 以下のときに再帰を止める条件が必要です。ないと無限に呼び出して RecursionError になります。

---

## 9-2　文書化文字列とアノテーション／9-3　名前空間とスコープ

### 問7　次の関数に、文書化文字列（docstring）とアノテーション（型ヒント）を付けなさい。

```python
def is_even(n):
    return n % 2 == 0
```

#### 解答例

```python
def is_even(n: int) -> bool:
    """n が偶数なら True を返す"""
    return n % 2 == 0
```

#### 解説

`help(is_even)` で docstring を表示できます。型ヒントは実行時にはチェックされませんが、PyCharm がまちがった型に警告を出してくれます。

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

#### 解答例

```text
10
30
```

#### 解説

f の中の `x = 20` は、新しいローカル変数を作るだけで、外の x は変わりません。

g は `global x` と宣言しているので、グローバル変数の x に代入されます。global の多用はプログラムをわかりにくくするので注意しましょう。

---

## 9-4　高階関数／9-5　ラムダ式

### 問9　次の式の結果を答えなさい。

（1）`list(map(lambda x: x * 2, [1, 2, 3]))`  
（2）`list(filter(lambda x: x % 2 == 0, range(10)))`  
（3）`sorted(['banana', 'kiwi', 'apple'], key=len)`  
（4）`sorted([('A', 80), ('B', 95), ('C', 70)], key=lambda t: t[1])`  

#### 解答例

（1）`[2, 4, 6]`　（2）`[0, 2, 4, 6, 8]`　（3）`['kiwi', 'apple', 'banana']`　（4）`[('C', 70), ('A', 80), ('B', 95)]`

#### 解説

map はすべての要素に関数を適用し、filter は True を返す要素だけを残します。

（3）（4）sorted の key には「並べ替えの基準を求める関数」を渡します。（4）は点数（t[1]）の小さい順です。

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

#### 解答例

```python
def max3(a, b, c):
    """a・b・c の最大値を返す"""
    m = a
    if b > m:
        m = b
    if c > m:
        m = c
    return m


x = int(input('a：'))
y = int(input('b：'))
z = int(input('c：'))
print(f'最大値は{max3(x, y, z)}です')
```

#### 解説

関数の中では print せず、return で値を返すのがポイントです。値を返す関数は、ほかの計算や表示にそのまま使えます。

関数の定義と、それを使うメインの処理の間は、空行を2行あけるのが PEP 8 の決まりです。

---

### 問11　素数の一覧

整数 n が素数なら True を返す関数 `is_prime(n)` を作りなさい。また、その関数を使って、入力した数までの素数をスペース区切りで表示しなさい。

**実行例**

```text
いくつまで：20
2 3 5 7 11 13 17 19
```

#### 解答例

```python
def is_prime(n: int) -> bool:
    """n が素数なら True を返す"""
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


n = int(input('いくつまで：'))
primes = [x for x in range(2, n + 1) if is_prime(x)]
print(*primes)
```

#### 解説

割り切れる数が見つかった時点で return False すれば、残りは調べずに済みます。

`print(*primes)` は、リストをばらして print に渡すので、スペース区切りで表示されます（`*` のアンパック）。

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

#### 解答例

```python
def grade(score: int) -> str:
    """点数から評価（A〜D）を返す"""
    if score >= 90:
        return 'A'
    elif score >= 80:
        return 'B'
    elif score >= 60:
        return 'C'
    else:
        return 'D'


scores = [int(x) for x in input('点数をスペース区切りで：').split()]
for s in scores:
    print(f'{s:3}点：{grade(s)}')
results = list(map(grade, scores))
print(f'A の人数：{results.count("A")}')
```

#### 解説

`map(grade, scores)` は、すべての点数に grade を適用します。関数を値として渡す、高階関数の使い方です。

f文字列の中で文字列を書くときは、外側と違う種類のクォート（`"A"`）を使っています（Python 3.12 以降は同じクォートも使えます）。

---
