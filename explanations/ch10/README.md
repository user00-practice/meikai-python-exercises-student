# 第10章　モジュールとパッケージ　解答例・解説

[← 目次に戻る](../../README.md)　／　[問題](../../exercises/ch10/README.md)

## 10-1　モジュール

### 問1　次の import のしかたで、モジュール `tools`（ファイル名 tools.py）の関数 `f` をどのように呼び出しますか。

（1）`import tools`  
（2）`import tools as t`  
（3）`from tools import f`  
（4）`from tools import f as g`  

#### 解答例

（1）`tools.f()`　（2）`t.f()`　（3）`f()`　（4）`g()`

#### 解説

（1）の `tools.f` のように「モジュール名.名前」と書く形を完全修飾名といいます。どのモジュールの f かがはっきりします。

`from tools import *` は、どこから来た名前かわからなくなるので使わないのが原則です。

---

### 問2　次のモジュール calc.py を、別のファイル main.py から `import calc` したとき、`テスト：3` は表示されますか。calc.py を直接実行したときはどうですか。

**calc.py**

```python
def add(a, b):
    return a + b

if __name__ == '__main__':
    print('テスト：', add(1, 2))
```

#### 解答例

import したとき：表示されない　　直接実行したとき：表示される

#### 解説

直接実行したときは `__name__` が `'__main__'`、import されたときはモジュール名 `'calc'` になります。

モジュールの動作確認のためのコードを書くときに使う、定番の書き方です。

---

### 問3　授業で乱数の練習をするために、自分のファイルを random.py という名前で保存し、次のように書いたところエラーになりました。理由と対処法を答えなさい。

**random.py**

```python
import random
print(random.randint(1, 6))
```

**エラー**

```text
AttributeError: module 'random' has no attribute 'randint'
```

#### 解答例

理由：import したときに、標準ライブラリの random ではなく、先に見つかった自分の random.py が読み込まれてしまったため。

対処法：ファイル名を dice.py などの別の名前に変える（同じフォルダにできた `__pycache__` も削除する）。

#### 解説

モジュールは、実行したプログラムのフォルダから先に探されます（モジュール検索パス）。標準ライブラリと同じ名前のファイルを作らないようにしましょう。

Python 3.13 以降では、エラーメッセージに「ファイル名を変えては？」というヒントが表示されます。

---

## 10-2　パッケージ

### 問4　次のフォルダ構成について答えなさい。

```text
project/
    app.py
    shop/
        __init__.py
        price.py
        cart.py
```

（1）shop フォルダに __init__.py を置く理由を答えなさい。  
（2）app.py から、price.py の関数 `with_tax` を使えるようにする import 文を答えなさい。  
（3）cart.py から、同じパッケージの price.py の `with_tax` を相対インポートで使う import 文を答えなさい。  

#### 解答例

（1）shop フォルダを正規パッケージにするため（パッケージの目印。中身は空でもよい）。

（2）`from shop.price import with_tax`（または `import shop.price`）

（3）`from .price import with_tax`

#### 解説

（3）の `.` は「自分と同じパッケージ」を表します。相対インポートを含むファイル（cart.py）を直接実行するとエラーになるので、パッケージの外の app.py から実行します。

---

## 応用問題（プログラムを作る）

### 問5　自作モジュールを作って使う

次の2つの関数を持つモジュール mymath.py を作りなさい。また、同じフォルダの q05_main.py から mymath を import して使いなさい。

（1）`square(x)`：x の2乗を返す  
（2）`is_even(n)`：n が偶数なら True を返す  

**q05_main.py の実行例**

```text
整数：7
7 の2乗：49
7 は偶数：False
```

#### 解答例

**mymath.py**

```python
"""簡単な計算のモジュール"""


def square(x):
    """x の2乗を返す"""
    return x * x


def is_even(n):
    """n が偶数なら True を返す"""
    return n % 2 == 0


if __name__ == '__main__':
    print(square(3), is_even(4))
```

**q05_main.py**

```python
import mymath

n = int(input('整数：'))
print(f'{n} の2乗：{mymath.square(n)}')
print(f'{n} は偶数：{mymath.is_even(n)}')
```

#### 解説

`if __name__ == '__main__':` の中は、mymath.py を直接実行したときだけ動く動作確認用のコードです。import したときは実行されません。

---

### 問6　（発展）パッケージを作って使う

次の構成で shop パッケージを作り、q06_shop_app.py から使いなさい。

```python
q06_shop_app.py
shop/
    __init__.py   （空でよい）
    price.py      税率 TAX_RATE = 0.1 と、税込価格を返す with_tax(price)
    cart.py       価格のリストの税込合計を返す total(items)（with_tax を使う）
```

**実行例**

```text
価格をスペース区切りで：100 200 1980
税込合計：2,508円
```

#### 解答例

**shop/price.py**

```python
TAX_RATE = 0.1


def with_tax(price):
    """税込価格（1円未満切り捨て）を返す"""
    return int(price * (1 + TAX_RATE))
```

**shop/cart.py**

```python
from .price import with_tax


def total(items):
    """価格のリストの税込合計を返す"""
    return sum([with_tax(p) for p in items])
```

**q06_shop_app.py**

```python
from shop.cart import total

items = [int(x) for x in input('価格をスペース区切りで：').split()]
print(f'税込合計：{total(items):,}円')
```

#### 解説

cart.py は同じパッケージの price.py を相対インポート（`.price`）で使い、q06_shop_app.py は絶対インポート（`shop.cart`）で使っています。

`int()` は小数点以下を切り捨てます。100 × 1.1 は浮動小数点数の誤差で 110.00000000000001 になりますが、切り捨てて 110 になります。合計は 110 ＋ 220 ＋ 2178 ＝ 2508 です。

---
