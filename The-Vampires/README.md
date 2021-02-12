So we have 3 types of units: the Warrior, Knight and Defender. Let's make the battles even more epic and add another type - the Vampire!
Vampire should be the subclass of the Warrior class and have the additional <b>vampirism</b> parameter, which helps him to heal himself. When the Vampire hits the other unit, he restores his health by +50% of the dealt damage (enemy defense makes the dealt damage value lower).

The basic parameters of the Vampire:
health = 40
attack = 4
vampirism = 50%

You should store vampirism attribute as an integer (50 for 50%). It will be needed to make this solution evolutes to fit one of the next challenges of this saga.

![alt text](https://py-static.checkio.org/media/task/media/e698caf5f3e74bc499d4c1d8df4a7186/defender_vs_vampire.png)

<b>Example:</b>
```
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()
bob = Defender()
mike = Knight()
rog = Warrior()
lancelot = Defender()
eric = Vampire()
adam = Vampire()
richard = Defender()
ogre = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False
fight(bob, mike) == False
fight(lancelot, rog) == True
fight(eric, richard) == False
fight(ogre, adam) == True

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Warrior, 1)

enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 4)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
```
<b>Input:</b> The warriors and armies.

<b>Output:</b> The result of the battle (True or False).

<b>How it is used:</b> For the computer games development.

<b>Precondition:</b> 4 types of units