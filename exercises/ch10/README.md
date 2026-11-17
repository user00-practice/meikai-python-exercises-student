# 第10章　モジュールとパッケージ　練習問題

[← 目次に戻る](../../README.md)　／　[解答例・解説](../../explanations/ch10/README.md)

モジュールは .py ファイル、パッケージはモジュールをまとめたフォルダです。プログラムを作る問題は、指定されたファイル名で同じフォルダに作りましょう。

> 📝 マークの問題は、このフォルダの .py ファイルにプログラムを書きます。書けたら、プロジェクトのフォルダで `python tools/check.py ch10` を実行してチェックしましょう。

## 10-1　モジュール

### 問1　次の import のしかたで、モジュール `tools`（ファイル名 tools.py）の関数 `f` をどのように呼び出しますか。

（1）`import tools`  
（2）`import tools as t`  
（3）`from tools import f`  
（4）`from tools import f as g`  

---

### 問2　次のモジュール calc.py を、別のファイル main.py から `import calc` したとき、`テスト：3` は表示されますか。calc.py を直接実行したときはどうですか。

**calc.py**

```python
def add(a, b):
    return a + b

if __name__ == '__main__':
    print('テスト：', add(1, 2))
```

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

> 📝 解答ファイル：[`exercises/ch10/q05_main.py`](./q05_main.py)

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

> 📝 解答ファイル：[`exercises/ch10/q06_shop_app.py`](./q06_shop_app.py)

---
