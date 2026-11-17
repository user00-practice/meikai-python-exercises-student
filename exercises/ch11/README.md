# 第11章　クラス　練習問題

[← 目次に戻る](../../README.md)　／　[解答例・解説](../../explanations/ch11/README.md)

クラスは「データ（属性）と処理（メソッド）をまとめた設計図」、インスタンスは「設計図から作った実物」です。self は「今あつかっているインスタンス自身」を表します。

> 📝 マークの問題は、このフォルダの .py ファイルにプログラムを書きます。書けたら、プロジェクトのフォルダで `python tools/check.py ch11` を実行してチェックしましょう。

## 11-1　クラス

### 問1　次の（　）に当てはまる言葉を答えなさい。

（1）クラスから作られた実物を（　①　）という。  
（2）インスタンスを作るときに自動的に呼ばれる、初期化のためのメソッドは（　②　）である。  
（3）メソッドの最初の引数には、インスタンス自身を表す（　③　）を書く。  
（4）データを外から直接触らせず、メソッドを通してだけ操作させる考え方を（　④　）という。  

---

### 問2　次のプログラムの表示を答えなさい。

```python
class Counter:
    def __init__(self):
        self.count = 0

    def up(self):
        self.count += 1

a = Counter()
b = Counter()
a.up()
a.up()
b.up()
print(a.count, b.count)
```

---

### 問3　次のプログラムはエラーになります。理由と正しい書き方を答えなさい。

```python
class Dog:
    def __init__(self, name):
        self.name = name

    def bark():
        print(f'{self.name}：ワン')

Dog('ポチ').bark()
```

---

### 問4　次のプログラムの表示を答えなさい。

```python
class Item:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    def __str__(self):
        return f'{self.name}（{self.price}円）'

x = Item('ペン', 120)
print(x)
print(f'商品：{x}')
```

---

## 11-2　クラス変数とクラスメソッド

### 問5　次のプログラムの表示を答えなさい。

```python
class Member:
    count = 0

    def __init__(self, name):
        self.name = name
        Member.count += 1

    @classmethod
    def get_count(cls):
        return cls.count

a = Member('佐藤')
b = Member('鈴木')
print(Member.get_count(), a.name, b.name)
```

---

## 11-3　継承

### 問6　次のプログラムの表示を答えなさい。

```python
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return '…'

class Dog(Animal):
    def speak(self):
        return 'ワン'

class Cat(Animal):
    def speak(self):
        return 'ニャー'

for a in [Dog('ポチ'), Cat('タマ'), Animal('？')]:
    print(a.name, a.speak())
```

---

### 問7　問6のクラスについて、次の式の結果（True または False）を答えなさい。

（1）`isinstance(Dog('ポチ'), Animal)`  
（2）`isinstance(Dog('ポチ'), Cat)`  
（3）`issubclass(Cat, Animal)`  
（4）`issubclass(Animal, object)`  

---

## 応用問題（プログラムを作る）

### 問8　長方形クラス

横と縦の長さを属性に持つ Rectangle クラスを作りなさい。面積を返す area メソッド、周の長さを返す perimeter メソッド、表示用の __str__ メソッドを持たせなさい。

**使い方**

```python
r = Rectangle(5, 3)
print(r)
print(f'面積：{r.area()}　周の長さ：{r.perimeter()}')
```

**実行結果**

```text
長方形（横5×縦3）
面積：15　周の長さ：16
```

> 📝 解答ファイル：[`exercises/ch11/q08_rectangle.py`](./q08_rectangle.py)

---

### 問9　銀行口座クラス

名義（name）と残高（balance）を持つ Account クラスを作りなさい。条件は次のとおりです。

（1）残高は `__balance` として外から直接変更できないようにし、`@property` で読み取りだけできるようにする。  
（2）deposit(amount)：預け入れ。0 以下の金額なら「金額が正しくありません」と表示して何もしない。  
（3）withdraw(amount)：引き出し。残高より多ければ「残高不足です」と表示して何もしない。  
（4）`print(a)` で「佐藤：1,300円」のように表示する。  

**使い方**

```python
a = Account('佐藤', 1000)
a.deposit(500)
a.withdraw(3000)
a.withdraw(200)
print(a)
print(a.balance)
```

**実行結果**

```text
残高不足です
佐藤：1,300円
1300
```

> 📝 解答ファイル：[`exercises/ch11/q09_account.py`](./q09_account.py)

---

### 問10　（発展）図形クラスと多相性

面積を返す area メソッドを持つ基底クラス Shape と、それを継承した正方形 Square（1辺 side）・円 Circle（半径 r）を作りなさい。Shape の __str__ で「クラス名：面積 〇〇」と表示するようにし、いろいろな図形をリストに入れて、まとめて表示しなさい。

**使い方**

```python
shapes = [Square(3), Circle(2), Square(1.5)]
for s in shapes:
    print(s)
```

**実行結果**

```text
Square：面積 9.0
Circle：面積 12.6
Square：面積 2.2
合計面積：23.8
```

> 📝 解答ファイル：[`exercises/ch11/q10_shapes.py`](./q10_shapes.py)

---
