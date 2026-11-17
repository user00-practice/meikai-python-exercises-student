# 第12章　例外処理　解答例・解説

[← 目次に戻る](../../README.md)　／　[問題](../../exercises/ch12/README.md)

## 12-1　例外処理

### 問1　次のプログラムを実行すると、どの例外が起きますか。

（1）`int('abc')`  
（2）`[1, 2][5]`  
（3）`{'a': 1}['b']`  
（4）`10 / 0`  
（5）`'a' + 1`  
（6）`open('nothing.txt')`（ファイルがないとき）  

#### 解答例

（1）ValueError　（2）IndexError　（3）KeyError　（4）ZeroDivisionError　（5）TypeError　（6）FileNotFoundError

#### 解説

どれも、これまでの章で見てきた例外です。例外の名前から原因がわかるようにしておきましょう。

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

#### 解答例

① ZeroDivisionError　② 0 で割った（空のリストを渡したので len(a) が 0 になった）　③ 2行目の average 関数の中（5行目の呼び出しから）

#### 解説

いちばん下の行が例外の種類と原因、その上が起きた場所です。下にあるほど、実際に例外が起きた場所に近くなります。

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

#### 解答例

0 のとき：`0 では割れません` → `終了`

2 のとき：`結果： 5.0` → `終了`

#### 解説

else は例外が起きなかったときだけ、finally は例外が起きても起きなくても必ず実行されます。

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

#### 解答例

理由：except は上から順に調べられる。Exception は ValueError や ZeroDivisionError の基底クラス（親）なので、すべての例外が最初の `except Exception:` でつかまってしまう。

直し方：`except Exception:` を削除する（または、いちばん最後に移動する）。

#### 解説

例外はクラスの継承関係（階層）になっています。except は、指定したクラスとその派生クラスの例外をすべてつかまえます。

具体的な例外を先に、一般的な例外を後に書きます。何でもつかまえる `except Exception:` は、本当のバグまで隠してしまうので、なるべく使わないようにしましょう。

---

### 問5　年齢が 0 未満のときに ValueError を送出する関数 `check_age(age)` を作りなさい。また、その例外をつかまえてメッセージを表示する呼び出し側のプログラムも書きなさい。

**check_age(-5) を呼んだときの表示**

```text
エラー：年齢が負です：-5
```

#### 解答例

```python
def check_age(age):
    if age < 0:
        raise ValueError(f'年齢が負です：{age}')
    return age


try:
    check_age(-5)
except ValueError as e:
    print('エラー：', e)
```

#### 解説

`raise 例外クラス('メッセージ')` で自分で例外を起こせます。`as e` で受け取った例外を print すると、そのメッセージが表示されます。

---

### 問6　ユーザ定義の例外

残高不足を表す自作の例外クラス `InsufficientFundsError` を定義しなさい。

#### 解答例

```python
class InsufficientFundsError(Exception):
    """残高不足を表す例外"""
    pass
```

#### 解説

Exception クラスを継承して作ります。クラス名は「〜Error」で終わらせるのが慣習です。

専用の例外にすると、呼び出し側でほかの原因の例外と区別して対処できます。

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

#### 解答例

```python
while True:
    try:
        n = int(input('整数：'))
        break
    except ValueError:
        print('整数を入力してください')
print(f'{n} の2倍は {n * 2} です')
```

#### 解説

変換に成功したら break でくり返しを抜け、失敗したら except でメッセージを表示してもう一度入力させます。

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

#### 解答例

```python
try:
    a = int(input('割られる数：'))
    b = int(input('割る数：'))
    q = a / b
except ValueError:
    print('整数を入力してください')
except ZeroDivisionError:
    print('0 では割れません')
else:
    print(f'{a} ÷ {b} = {q:.2f}')
finally:
    print('計算を終わります')
```

#### 解説

try の中には例外が起きそうな処理だけを書き、成功したときの表示は else に分けています。

「最後に必ず」行う処理は finally に書きます。

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

#### 解答例

```python
class InsufficientFundsError(Exception):
    """残高不足を表す例外"""
    pass


def withdraw(balance, amount):
    """引き出したあとの残高を返す"""
    if amount < 0:
        raise ValueError('金額が負です')
    if amount > balance:
        raise InsufficientFundsError(f'残高不足：あと{amount - balance}円')
    return balance - amount
```

#### 解説

例外が起きると `balance = withdraw(…)` の代入は行われないので、残高は変わりません。

関数の中で print せずに例外を送出すると、「どう対処するか（表示する・ログに残す・やり直すなど）」を呼び出し側で決められます。

---
