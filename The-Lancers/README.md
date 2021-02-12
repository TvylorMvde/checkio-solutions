It seems that the Warrior, Knight, Defender and Vampire are not enough to win the battle. Let's add one more powerful unit type - the Lancer.</br>
Lancer should be the subclass of the Warrior class and should attack in a specific way - when he hits the other unit, he also deals a 50% of the deal damage to the enemy unit, standing behind the firstly assaulted one (enemy defense makes the deal damage value lower - consider this).</br>

The basic parameters of the Lancer:
health = 50
attack = 6

![alt text](https://py-static.checkio.org/media/task/media/781a9b7c20ef48ceade25123266c3899/lancer_vs_warrior&knight.png)

Example :
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
freelancer = Lancer()
vampire = Vampire()

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
fight(freelancer, vampire) == True
freelancer.is_alive == True

my_army = Army()
my_army.add_units(Defender, 2)
my_army.add_units(Vampire, 2)
my_army.add_units(Lancer, 4)
my_army.add_units(Warrior, 1)
    
enemy_army = Army()
enemy_army.add_units(Warrior, 2)
enemy_army.add_units(Lancer, 2)
enemy_army.add_units(Defender, 2)
enemy_army.add_units(Vampire, 3)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Lancer, 1)
army_3.add_units(Defender, 2)

army_4 = Army()
army_4.add_units(Vampire, 3)
army_4.add_units(Warrior, 1)
army_4.add_units(Lancer, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == True
battle.fight(army_3, army_4) == False
```
<b>Input:</b> The warriors and armies.

<b>Output:</b> The result of the battle (True or False).

<b>How it is used:</b> For computer games development.

<b>Precondition:</b> 5 types of units