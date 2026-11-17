# 第11章　クラス　解答例・解説

[← 目次に戻る](../../README.md)　／　[問題](../../exercises/ch11/README.md)

## 11-1　クラス

### 問1　次の（　）に当てはまる言葉を答えなさい。

（1）クラスから作られた実物を（　①　）という。  
（2）インスタンスを作るときに自動的に呼ばれる、初期化のためのメソッドは（　②　）である。  
（3）メソッドの最初の引数には、インスタンス自身を表す（　③　）を書く。  
（4）データを外から直接触らせず、メソッドを通してだけ操作させる考え方を（　④　）という。  

#### 解答例

① インスタンス（オブジェクト）　② `__init__`　③ `self`　④ カプセル化（データ隠蔽）

#### 解説

`__init__` の前後はアンダースコア2つずつです。1つだと初期化メソッドとして呼ばれません。

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

#### 解答例

```text
2 1
```

#### 解説

`self.count` はインスタンス変数なので、a と b はそれぞれ別の count を持っています。

`a.up()` と呼ぶと、self には a が自動的に入ります。

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

#### 解答例

理由：メソッド bark の最初の引数 self がない。`Dog('ポチ').bark()` と呼ぶとインスタンスが自動で渡されるが、受け取る引数がないため TypeError になる。

**正しい書き方**

```python
    def bark(self):
```

#### 解説

メソッドを定義するときは、引数がなくても必ず self を書きます。

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

#### 解答例

```text
ペン（120円）
商品：ペン（120円）
```

#### 解説

`__str__` を定義すると、print や f文字列で、そのインスタンスを表示するときに使われます。定義しないと `<__main__.Item object at 0x…>` のような表示になります。

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

#### 解答例

```text
2 佐藤 鈴木
```

#### 解説

`count` はクラス変数で、すべてのインスタンスで共有されます。インスタンスを作るたびに 1 増えます。

クラス変数を変更するときは `Member.count` のようにクラス名を付けて書きます。`self.count += 1` だと、インスタンス変数が新しく作られてしまいます。

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

#### 解答例

```text
ポチ ワン
タマ ニャー
？ …
```

#### 解説

Dog と Cat は Animal を継承し、speak をオーバライド（定義し直し）しています。`__init__` は Animal のものがそのまま使われます。

同じ `a.speak()` という呼び出しで、クラスごとに違う動きをすることを多相性（ポリモーフィズム）といいます。

---

### 問7　問6のクラスについて、次の式の結果（True または False）を答えなさい。

（1）`isinstance(Dog('ポチ'), Animal)`  
（2）`isinstance(Dog('ポチ'), Cat)`  
（3）`issubclass(Cat, Animal)`  
（4）`issubclass(Animal, object)`  

#### 解答例

（1）True　（2）False　（3）True　（4）True

#### 解説

Dog は Animal の一種（is-A の関係）なので、Dog のインスタンスは Animal のインスタンスでもあります。

すべてのクラスは object クラスを継承しています。

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

#### 解答例

```python
class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return (self.width + self.height) * 2

    def __str__(self):
        return f'長方形（横{self.width}×縦{self.height}）'
```

#### 解説

メソッドの中では、`self.width` のように self を通して自分の属性を使います。

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

#### 解答例

```python
class Account:
    def __init__(self, name, balance=0):
        self.name = name
        self.__balance = balance

    @property
    def balance(self):
        return self.__balance

    def deposit(self, amount):
        if amount <= 0:
            print('金額が正しくありません')
            return
        self.__balance += amount

    def withdraw(self, amount):
        if amount > self.__balance:
            print('残高不足です')
            return
        self.__balance -= amount

    def __str__(self):
        return f'{self.name}：{self.__balance:,}円'
```

#### 解説

`a.balance = 0` のように外から書き換えようとすると、セッタがないので AttributeError になります。残高は deposit と withdraw でしか変えられません。

第12章では、「残高不足です」と表示する代わりに例外を送出する方法を学びます。

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

#### 解答例

```python
import math


class Shape:
    def area(self):
        return 0

    def __str__(self):
        return f'{type(self).__name__}：面積 {self.area():.1f}'


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side ** 2


class Circle(Shape):
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r ** 2
```

#### 解説

`__str__` は Shape だけに書いていますが、その中で呼ぶ `self.area()` は、それぞれのクラスでオーバライドした area が使われます（多相性）。

`type(self).__name__` で、インスタンスのクラス名を文字列として取り出せます。

新しい図形（三角形など）を追加しても、area を定義するだけで、表示のループはそのまま使えます。

Square(1.5) の面積 2.25 は、`:.1f` では偶数側に丸められて 2.2 と表示されます。

---
