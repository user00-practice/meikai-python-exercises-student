# 第4章　プログラムの流れの繰返し　練習問題

[← 目次に戻る](../../README.md)　／　[解答例・解説](../../explanations/ch04/README.md)

くり返しの問題は、変数の値がどう変わるかを表（トレース表）に書いて追いかけると確実です。無限ループになったら、PyCharm の停止ボタン（赤い四角）で止めましょう。

> 📝 マークの問題は、このフォルダの .py ファイルにプログラムを書きます。書けたら、プロジェクトのフォルダで `python tools/check.py ch04` を実行してチェックしましょう。

## 4-1　while文

### 問1　次のプログラムで、n に 3 を入力したときの表示を答えなさい。

```python
n = int(input('いくつから：'))
while n > 0:
    print(n)
    n -= 1
print('発射！')
```

---

### 問2　次のプログラムは終わりません。理由を説明し、正しく直しなさい。

```python
i = 1
while i <= 5:
    print(i)
```

---

### 問3　次のプログラムの表示を答えなさい。

```python
for i in range(1, 10):
    if i % 3 == 0:
        continue
    if i == 7:
        break
    print(i, end=' ')
```

---

### 問4　累算代入演算子

（1）次のプログラムの表示を答えなさい。

```python
x = 2
x *= 3
x -= 1
x //= 2
print(x)
```

（2）次のプログラムの4行目と5行目を、累算代入演算子を使って書き直しなさい。

```python
count = 0
i = 0
while i < 5:
    count = count + 2
    i = i + 1
print(count)
```

---

## 4-2　for文

### 問5　次の range が作る数の並びを答えなさい。

（1）`range(5)`  
（2）`range(1, 6)`  
（3）`range(0, 10, 3)`  
（4）`range(5, 0, -1)`  
（5）`range(10, 0, -3)`  

---

### 問6　1 から n までの和を求めるつもりのプログラムですが、n に 5 を入力すると 10 と表示されます。理由を説明し、正しく直しなさい。

```python
n = int(input('n：'))
total = 0
for i in range(1, n):
    total += i
print(total)
```

---

### 問7　次のプログラムで、n に 9 と 7 を入力したときの表示をそれぞれ答えなさい。

```python
n = int(input('整数：'))
for i in range(2, n):
    if n % i == 0:
        print('素数ではない')
        break
else:
    print('素数')
```

---

### 問8　次の while文を、for文と range を使って書き直しなさい。

```python
i = 0
while i < 10:
    print(i)
    i += 2
```

---

## 4-3　多重ループ

### 問9　次のプログラムの表示を答えなさい。

**（1）**

```python
for i in range(1, 4):
    for j in range(i):
        print('*', end='')
    print()
```

**（2）**

```python
count = 0
for i in range(3):
    for j in range(4):
        count += 1
print(count)
```

---

## 応用問題（プログラムを作る）

### 問10　0 が入力されるまでの合計

整数を次々に入力し、0 が入力されたら、それまでの合計を表示するプログラムを作りなさい。

**実行例**

```text
整数：5
整数：3
整数：0
合計は8です
```

> 📝 解答ファイル：[`exercises/ch04/q10_sum_until_zero.py`](./q10_sum_until_zero.py)

---

### 問11　九九の1つの段

段（1〜9）を入力すると、その段の九九を表示するプログラムを作りなさい。

**実行例**

```text
段：3
3 × 1 = 3
3 × 2 = 6
（中略）
3 × 9 = 27
```

> 📝 解答ファイル：[`exercises/ch04/q11_times_table.py`](./q11_times_table.py)

---

### 問12　右寄せの直角三角形

段数を入力すると、右寄せの直角三角形を * で表示するプログラムを作りなさい。

**実行例**

```text
段数：4
   *
  **
 ***
****
```

> 📝 解答ファイル：[`exercises/ch04/q12_triangle.py`](./q12_triangle.py)

---

### 問13　（発展）FizzBuzz

1 から入力した数までを順に表示するプログラムを作りなさい。ただし、3 の倍数のときは「Fizz」、5 の倍数のときは「Buzz」、3 と 5 の両方の倍数のときは「FizzBuzz」と表示しなさい。

> 📝 解答ファイル：[`exercises/ch04/q13_fizzbuzz.py`](./q13_fizzbuzz.py)

---
