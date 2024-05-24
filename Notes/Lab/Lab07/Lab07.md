[TOC]

# Lab 7: Object-Oriented Programming, Linked Lists, Mutable Trees

实验链接：[Lab 7: Object-Oriented Programming, Linked Lists, Mutable Trees](https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab07/)

如何下载实验压缩包：

```shell
wget https://inst.eecs.berkeley.edu/~cs61a/sp21/lab/lab07/lab07.zip
```

## WWPD: Objects

### Q1: The Car class

使用如下命令进行测试：

```shell
python3 ok -q wwpd-car -u --local
```

测试过程如下：

```shell
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Car > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.model
? 'Model S'
-- OK! --

>>> deneros_car.gas = 10
>>> deneros_car.drive()
? 'Tesla Model S goes vroom!'
-- OK! --

>>> deneros_car.drive()
? 'Cannot drive!'
-- OK! --

>>> deneros_car.fill_gas()
? 'Gas level: 20'
-- OK! --

>>> deneros_car.gas
? 20
-- OK! --

>>> Car.gas
? 30
-- OK! --

---------------------------------------------------------------------
Car > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = Car('Tesla', 'Model S')
>>> deneros_car.wheels = 2
>>> deneros_car.wheels
? 2
-- OK! --

>>> Car.num_wheels
? 4
-- OK! --

>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? 'Tesla Model S goes vroom!'
-- Not quite. Try again! --

? 'Cannot drive!'
-- OK! --

>>> Car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? 'Cannot drive!'
-- OK! --

---------------------------------------------------------------------
Car > Suite 1 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from car import *
>>> deneros_car = MonsterTruck('Monster', 'Batmobile')
>>> deneros_car.drive() # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? 'Monster Batmobile goes vroom!'
-- OK! --

>>> MonsterTruck.drive(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
(line 1)? Vroom! This Monster Truck is huge!
(line 2)? 'Monster Batmobile goes vroom!'
-- OK! --

>>> Car.rev(deneros_car) # Type Error if an error occurs and Nothing if nothing is displayed
? Error
-- OK! --

---------------------------------------------------------------------
OK! All cases for Car unlocked.
```



## Magic: The Lambda-ing

### Q2: Making Cards

实现`Card`类的`__init__`和`play`函数。

`__init__`：初始化一张卡牌

- `name`：卡牌的名字，字符串
- `attack`：卡牌的攻击力，整型
- `defense`：卡牌的防御力，整型

`power`：根据对手和自己的卡牌，计算权值，公式为`(player card's attack) - (opponent card's defense) / 2`

- `opponent_card`：对手出的卡牌，`Card`

实现如下：

```python
def __init__(self, name: str, attack: int, defense: int) -> None:
    """
    Create a Card object with a name, attack,
    and defense.
    >>> staff_member = Card('staff', 400, 300)
    >>> staff_member.name
    'staff'
    >>> staff_member.attack
    400
    >>> staff_member.defense
    300
    >>> other_staff = Card('other', 300, 500)
    >>> other_staff.attack
    300
    >>> other_staff.defense
    500
    """
    "*** YOUR CODE HERE ***"
    self.name = name
    self.attack = attack
    self.defense = defense
    

def power(self, opponent_card: 'Card'):
    """
    Calculate power as:
    (player card's attack) - (opponent card's defense)/2
    >>> staff_member = Card('staff', 400, 300)
    >>> other_staff = Card('other', 300, 500)
    >>> staff_member.power(other_staff)
    150.0
    >>> other_staff.power(staff_member)
    150.0
    >>> third_card = Card('third', 200, 400)
    >>> staff_member.power(third_card)
    200.0
    >>> third_card.power(staff_member)
    50.0
    """
    "*** YOUR CODE HERE ***"
    return self.attack - opponent_card.defense / 2
```

注意，我们在`power`函数中参数列表中，将`opponent_card`参数的类型注解为`Card`：

> 要在 Python 类的函数参数中声明参数类型为另一个类，你可以使用类型注解。在你的情况下，你可以将参数类型声明为 `Card` 类。下面是一个示例：
>
> ```python
> class Card:
>     def __init__(self, suit: str, value: int):
>         self.suit = suit
>         self.value = value
> 
>     def compare(self, other_card: 'Card') -> bool:
>         # 在这里使用参数类型为 Card 的参数
>         return self.value == other_card.value
> 
> card1 = Card('Spades', 5)
> card2 = Card('Hearts', 5)
> print(card1.compare(card2))  # 输出：True
> ```
>
> 在上面的例子中，`Card` 类的 `compare` 方法的参数 `other_card` 声明了类型为 `Card`。这样，你就可以在函数内部使用 `other_card` 对象的属性和方法。
>
> **`注意，在类型注解中引用自身类时，要使用字符串形式的类名，即 'Card'，以避免循环导入的问题。`**
>
> 希望这可以帮助你! 😊🐍

### Q3: Making a Player

实现`Player`类的`__init__`、`draw`和`play`函数。

`__init__`：初始化一个玩家

- `deck`：牌组，类型是`Deck`类的实例
- `name`：玩家的名字，字符串

`draw`：从牌组(deck)中绘制一张卡牌，并将其加入手牌(hand)中

`play`：打出一张手牌

- `card_index`：卡牌的索引，整型

实现如下：

```python
def __init__(self, deck: 'Deck', name: str):
    """Initialize a Player object.
    A Player starts the game by drawing 5 cards from their deck. Each turn,
    a Player draws another card from the deck and chooses one to play.
    >>> test_card = Card('test', 100, 100)
    >>> test_deck = Deck([test_card.copy() for _ in range(6)])
    >>> test_player = Player(test_deck, 'tester')
    >>> len(test_deck.cards)
    1
    >>> len(test_player.hand)
    5
    """
    self.deck: 'Deck' = deck
    self.name: str = name
    "*** YOUR CODE HERE ***"
    self.hand: list[Card] = [self.deck.draw() for _ in range(5)]
    

def draw(self):
    """Draw a card from the player's deck and add it to their hand.
    >>> test_card = Card('test', 100, 100)
    >>> test_deck = Deck([test_card.copy() for _ in range(6)])
    >>> test_player = Player(test_deck, 'tester')
    >>> test_player.draw()
    >>> len(test_deck.cards)
    0
    >>> len(test_player.hand)
    6
    """
    assert not self.deck.is_empty(), 'Deck is empty!'
    "*** YOUR CODE HERE ***"
    self.hand.append(self.deck.draw())


def play(self, card_index: int):
    """Remove and return a card from the player's hand at the given index.
    >>> from cards import *
    >>> test_player = Player(standard_deck, 'tester')
    >>> ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
    >>> tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
    >>> test_player.hand = [ta1, ta2, tutor1, tutor2]
    >>> test_player.play(0) is ta1
    True
    >>> test_player.play(2) is tutor2
    True
    >>> len(test_player.hand)
    2
    """
    "*** YOUR CODE HERE ***"
    return self.hand.pop(card_index)
```

## WWPD: Linked Lists

### Q4: WWPD: Linked Lists

运行以下命令进行测试：

```python
python3 ok -q link -u --local
```

测试过程如下：

```python
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Unlocking tests

At each "? ", type what you would expect the output to be.
Type exit() to quit

---------------------------------------------------------------------
Link > Suite 1 > Case 1
(cases remaining: 3)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab09 import *
>>> link = Link(1000)
>>> link.first
? 1000
-- OK! --

>>> link.rest is Link.empty
? True
-- OK! --

>>> link = Link(1000, 2000)
? Error
-- OK! --

>>> link = Link(1000, Link())
? Error
-- OK! --

---------------------------------------------------------------------
Link > Suite 1 > Case 2
(cases remaining: 2)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab09 import *
>>> link = Link(1, Link(2, Link(3)))
>>> link.first
? 1
-- OK! --

>>> link.rest.first
? 2
-- OK! --

>>> link.rest.rest.rest is Link.empty
? True
-- OK! --

>>> link.first = 9001
>>> link.first
? 9001
-- OK! --

>>> link.rest = link.rest.rest
>>> link.rest.first
? 3
-- OK! --

>>> link = Link(1)
>>> link.rest = link
>>> link.rest.rest.rest.rest.first
? 1
-- OK! --

>>> link = Link(2, Link(3, Link(4)))
>>> link2 = Link(1, link)
>>> link2.first
? 1
-- OK! --

>>> link2.rest.first
? 2
-- OK! --

---------------------------------------------------------------------
Link > Suite 1 > Case 3
(cases remaining: 1)

What would Python display? If you get stuck, try it out in the Python
interpreter!

>>> from lab09 import *
>>> link = Link(5, Link(6, Link(7)))
>>> link                  # Look at the __repr__ method of Link
? Link(5, Link(6, Link(7)))
-- OK! --

>>> print(link)          # Look at the __str__ method of Link
? <5 6 7>
-- OK! --

---------------------------------------------------------------------
OK! All cases for Link unlocked.

Cannot backup when running ok with --local.
```

## Linked Lists

### Q5: Convert Link

实现`convert_link`函数。

将`Link`类的实例转换为一个Python列表。

实现如下(迭代方法)：

```python
def convert_link(link: 'Link'):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    ans: list[int] = []
    tmp: Link = link
    while tmp is not Link.empty:
        ans.append(tmp.first)
        tmp = tmp.rest

    return ans
```

实现如下(递归方法)：

```python
def convert_link(link: 'Link'):
    """Takes a linked list and returns a Python list with the same elements.

    >>> link = Link(1, Link(2, Link(3, Link(4))))
    >>> convert_link(link)
    [1, 2, 3, 4]
    >>> convert_link(Link.empty)
    []
    """
    "*** YOUR CODE HERE ***"
    # iterative solution
    # ans: list[int] = []
    # tmp: Link = link
    # while tmp is not Link.empty:
    #     ans.append(tmp.first)
    #     tmp = tmp.rest

    # return ans

    # recursive solution
    if link is Link.empty:
        return []

    tmp = [link.first]
    tmp.extend(convert_link(link.rest))
    return tmp
```

## Trees

### Q6: `Cumulative Mul`

修改树的节点的值，使其乘以其所有子树的节点值。

实现如下：

```python
def cumulative_mul(t: 'Tree'):
    """Mutates t so that each node's label becomes the product of all labels in
    the corresponding subtree rooted at t.

    >>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
    >>> cumulative_mul(t)
    >>> t
    Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return
    
    for cld in t.branches:
        cumulative_mul(cld)
        t.label *= cld.label
```

## 最终测试

至此，已经完成了除额外问题外的所有问题。

使用如下命令进行测试：

```shell
python3 ok --score --local
```

测试结果如下：

```python
=====================================================================
Assignment: Lab 7
OK, version v1.18.1
=====================================================================

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Scoring tests

---------------------------------------------------------------------
Link
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Doctests for convert_link

>>> from lab07 import *
>>> link = Link(1, Link(2, Link(3, Link(4))))
>>> convert_link(link)
[1, 2, 3, 4]
>>> convert_link(Link.empty)
[]
Score: 1.0/1

---------------------------------------------------------------------
Doctests for cumulative_mul

>>> from lab07 import *
>>> t = Tree(1, [Tree(3, [Tree(5)]), Tree(7)])
>>> cumulative_mul(t)
>>> t
Tree(105, [Tree(15, [Tree(5)]), Tree(7)])
Score: 1.0/1

---------------------------------------------------------------------
Car
    Passed: 0
    Failed: 0
[k..........] 0.0% passed

---------------------------------------------------------------------
Doctests for Card.__init__

>>> from classes import *
>>> staff_member = Card('staff', 400, 300)
>>> staff_member.name
'staff'
>>> staff_member.attack
400
>>> staff_member.defense
300
>>> other_staff = Card('other', 300, 500)
>>> other_staff.attack
300
>>> other_staff.defense
500
Score: 1.0/1

---------------------------------------------------------------------
Doctests for Card.power

>>> from classes import *
>>> staff_member = Card('staff', 400, 300)
>>> other_staff = Card('other', 300, 500)
>>> staff_member.power(other_staff)
150.0
>>> other_staff.power(staff_member)
150.0
>>> third_card = Card('third', 200, 400)
>>> staff_member.power(third_card)
200.0
>>> third_card.power(staff_member)
50.0
Score: 1.0/1

---------------------------------------------------------------------
Doctests for Player.__init__

>>> from classes import *
>>> test_card = Card('test', 100, 100)
>>> test_deck = Deck([test_card.copy() for _ in range(6)])
>>> test_player = Player(test_deck, 'tester')
>>> len(test_deck.cards)
1
>>> len(test_player.hand)
5
Score: 1.0/1

---------------------------------------------------------------------
Doctests for Player.draw

>>> from classes import *
>>> test_card = Card('test', 100, 100)
>>> test_deck = Deck([test_card.copy() for _ in range(6)])
>>> test_player = Player(test_deck, 'tester')
>>> test_player.draw()
>>> len(test_deck.cards)
0
>>> len(test_player.hand)
6
Score: 1.0/1

---------------------------------------------------------------------
Doctests for Player.play

>>> from classes import *
>>> from cards import *
>>> test_player = Player(standard_deck, 'tester')
>>> ta1, ta2 = TACard("ta_1", 300, 400), TACard("ta_2", 500, 600)
>>> tutor1, tutor2 = TutorCard("t1", 200, 500), TutorCard("t2", 600, 400)
>>> test_player.hand = [ta1, ta2, tutor1, tutor2]
>>> test_player.play(0) is ta1
True
>>> test_player.play(2) is tutor2
True
>>> len(test_player.hand)
2
Score: 1.0/1

---------------------------------------------------------------------
Point breakdown
    Link: 0.0/0
    convert_link: 1.0/1
    cumulative_mul: 1.0/1
    Car: 0.0/0
    Card.__init__: 1.0/1
    Card.power: 1.0/1
    Player.__init__: 1.0/1
    Player.draw: 1.0/1
    Player.play: 1.0/1

Score:
    Total: 7.0

Cannot backup when running ok with --local.
```

## Optional Questions

### Q7: Tutors: Flummox

实现`TutorCard`的`effect`方法，使得对手丢弃前三张手牌，并重新绘制三张手牌。

实现如下：

```python
class TutorCard(Card):
    cardtype = 'Tutor'

    def effect(self, opponent_card: Card, player: Player, opponent: Player):
        """
        Discard the first 3 cards in the opponent's hand and have
        them draw the same number of cards from their deck.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> opponent_card = Card('other', 500, 500)
        >>> tutor_test = TutorCard('Tutor', 500, 500)
        >>> initial_deck_length = len(player2.deck.cards)
        >>> tutor_test.effect(opponent_card, player1, player2)
        p2 discarded and re-drew 3 cards!
        >>> len(player2.hand)
        5
        >>> len(player2.deck.cards) == initial_deck_length - 3
        True
        """
        "*** YOUR CODE HERE ***"
        #Uncomment the line below when you've finished implementing this method!
        print('{} discarded and re-drew 3 cards!'.format(opponent.name))
        opponent.hand = opponent.hand[3:]
        for _ in range(3):
            opponent.draw()
```

### Q8: TAs: Shift

实现`TutorCard`的`effect`方法，使得`opponent_card`这张卡的攻击力和防御力数值互换。

实现如下：

```python
class TACard(Card):
    cardtype = 'TA'

    def effect(self, opponent_card: Card, player: Player, opponent: Player):
        """
        Swap the attack and defense of an opponent's card.
        >>> from cards import *
        >>> player1, player2 = Player(player_deck, 'p1'), Player(opponent_deck, 'p2')
        >>> opponent_card = Card('other', 300, 600)
        >>> ta_test = TACard('TA', 500, 500)
        >>> ta_test.effect(opponent_card, player1, player2)
        >>> opponent_card.attack
        600
        >>> opponent_card.defense
        300
        """
        "*** YOUR CODE HERE ***"
        opponent_card.attack, opponent_card.defense = opponent_card.defense, opponent_card.attack

```

### Q9: The Professor Arrives

实现`ProfessorCard`的`effect`方法，使得双方牌组的卡牌都提升`x`点攻击力和`y`点防御力(`x`、`y`为`opponent_card`的攻击力和防御力)，并把对手牌组中攻击力和防御力相同的卡牌移除。

注意：迭代列表时修改列表可能会出现问题。

> 在 Python 中，如果你在迭代一个列表时，删除了列表的某些元素，会导致迭代器失效，从而引发 `RuntimeError` 异常。这是因为在迭代器遍历列表时，它会记录当前迭代到的位置，如果你删除了列表中的元素，列表的长度会发生变化，从而导致迭代器无法正确地遍历列表。
>
> 为了避免这种情况，你可以使用以下两种方法之一：
>
> 1. 创建一个新的列表，将需要保留的元素添加到新列表中，然后使用新列表进行迭代。这种方法可以避免在迭代时修改原始列表，从而保证迭代器的正确性。
>
> ```python
> my_list = [1, 2, 3, 4, 5]
> new_list = []
> for item in my_list:
>     if item % 2 == 0:
>         new_list.append(item)
> for item in new_list:
>     print(item)
> ```
>
> 2. 使用倒序迭代。这种方法可以避免在迭代时删除元素导致的问题，因为倒序迭代时，删除元素不会影响前面的元素。
>
> ```python
> my_list = [1, 2, 3, 4, 5]
> for i in range(len(my_list)-1, -1, -1):
>     if my_list[i] % 2 == 0:
>         del my_list[i]
> for item in my_list:
>     print(item)
> ```
>
> 希望这可以帮助你! 😊🐍

实现如下：

```python
class ProfessorCard(Card):
    cardtype = 'Professor'

    def effect(self, opponent_card: Card, player: Player, opponent: Player):
        """
        Adds the attack and defense of the opponent's card to
        all cards in the player's deck, then removes all cards
        in the opponent's deck that share an attack or defense
        stat with the opponent's card.
        >>> test_card = Card('card', 300, 300)
        >>> professor_test = ProfessorCard('Professor', 500, 500)
        >>> opponent_card = test_card.copy()
        >>> test_deck = Deck([test_card.copy() for _ in range(8)])
        >>> player1, player2 = Player(test_deck.copy(), 'p1'), Player(test_deck.copy(), 'p2')
        >>> professor_test.effect(opponent_card, player1, player2)
        3 cards were discarded from p2's deck!
        >>> [(card.attack, card.defense) for card in player1.deck.cards]
        [(600, 600), (600, 600), (600, 600)]
        >>> len(player2.deck.cards)
        0
        """
        orig_opponent_deck_length = len(opponent.deck.cards)
        "*** YOUR CODE HERE ***"
        for card in player.deck.cards:
            card.attack += opponent_card.attack
            card.defense += opponent_card.defense

        deck_cards_tmp: list[Card] = []

        for card in opponent.deck.cards:
            card.attack += opponent_card.attack
            card.defense += opponent_card.defense
            if (card.attack != card.defense):
                deck_cards_tmp.append(card)

        opponent.deck.cards = deck_cards_tmp
        discarded = orig_opponent_deck_length - len(opponent.deck.cards)
        if discarded:
            #Uncomment the line below when you've finished implementing this method!
            print('{} cards were discarded from {}\'s deck!'.format(discarded, opponent.name))
            return
```

### Q10: Cycles

剑指offer中有本题的进阶版本：[JZ23 链表中环的入口结点](https://www.nowcoder.com/practice/253d2c59ec3e4bc68da16833f79a38e4?tpId=13&tqId=23449&ru=/exam/oj/ta&qru=/ta/coding-interviews/question-ranking&sourceUrl=%2Fexam%2Foj%2Fta%3Fpage%3D1%26tpId%3D13%26type%3D13)

实现`has_cycle(link: 'Link')`函数，检查`link`中是否有环。

线性空间复杂度的解法：

```python
def has_cycle(link: 'Link'):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle(t)
    False
    >>> u = Link(2, Link(2, Link(2)))
    >>> has_cycle(u)
    False
    """
    "*** YOUR CODE HERE ***"
    nodes: list[Link] = []
    link_tmp: Link = link
    
    while link_tmp is not Link.empty:
        if link_tmp in nodes:
            return True
        nodes.append(link_tmp)
        link_tmp = link_tmp.rest
    
    return False
```

常数空间复杂度的解法：

```python
def has_cycle_constant(link: 'Link'):
    """Return whether link contains a cycle.

    >>> s = Link(1, Link(2, Link(3)))
    >>> s.rest.rest.rest = s
    >>> has_cycle_constant(s)
    True
    >>> t = Link(1, Link(2, Link(3)))
    >>> has_cycle_constant(t)
    False
    """
    "*** YOUR CODE HERE ***"
    # link_tmp: Link = link
    # cnt: int = 0
    # while link_tmp is not Link.empty and cnt < 100:
    #     link_tmp = link_tmp.rest
    #     cnt += 1

    # if cnt == 100:
    #     return True

    # return False

    fast: Link = link
    slow: Link = link
    while (True):
        if slow is Link.empty or fast is Link.empty:
            return False
        
        slow = slow.rest

        fast = fast.rest
        if fast is Link.empty:
            return False
        fast = fast.rest

        if slow == fast:
            return True
```

### Q11: Every Other

实现`every_other(s: 'Link')`函数，删除链表`s`中奇数索引的节点(从`0`开始数)。

实现如下：

```python
def every_other(s: 'Link'):
    """Mutates a linked list so that all the odd-indiced elements are removed
    (using 0-based indexing).

    >>> s = Link(1, Link(2, Link(3, Link(4))))
    >>> every_other(s)
    >>> s
    Link(1, Link(3))
    >>> odd_length = Link(5, Link(3, Link(1)))
    >>> every_other(odd_length)
    >>> odd_length
    Link(5, Link(1))
    >>> singleton = Link(4)
    >>> every_other(singleton)
    >>> singleton
    Link(4)
    """
    "*** YOUR CODE HERE ***"
    idx: int = 0
    link: Link = s

    while link is not Link.empty and link.rest is not Link.empty:
        link.rest = link.rest.rest
        link = link.rest
```

### Q12: Reverse Other

实现`reverse_other(t: 'Tree')`函数，把`t`奇数层的子树的值翻转(注意：只改变值)。

实现如下：

```python
def reverse_other(t: 'Tree'):
    """Mutates the tree such that nodes on every other (odd-depth) level
    have the labels of their branches all reversed.

    >>> t = Tree(1, [Tree(2), Tree(3), Tree(4)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(4), Tree(3), Tree(2)])
    >>> t = Tree(1, [Tree(2, [Tree(3, [Tree(4), Tree(5)]), Tree(6, [Tree(7)])]), Tree(8)])
    >>> reverse_other(t)
    >>> t
    Tree(1, [Tree(8, [Tree(3, [Tree(5), Tree(4)]), Tree(6, [Tree(7)])]), Tree(2)])
    """
    "*** YOUR CODE HERE ***"
    if t.is_leaf():
        return
    
    labels: list[int] = []
    
    for i in range(len(t.branches) - 1, -1, -1):
        labels.append(t.branches[i].label)

    for i in range(len(t.branches)):
        t.branches[i].label = labels[i]

    for cld in t.branches:
        if not cld.is_leaf():
            for _ in cld.branches:
                reverse_other(_)
```















