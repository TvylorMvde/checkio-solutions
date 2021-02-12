In the previous mission - Army battles, you've learned how to make a battle between 2 armies. But we have only 2 types of units - the Warriors and Knights. Let's add another one - the Defender. It should be the subclass of the Warrior class and have an additional <b>defense</b> parameter, which helps him to survive longer. When another unit hits the defender, he loses a certain amount of his health according to the next formula: enemy attack - self defense (if enemy attack > self defense). Otherwise, the defender doesn't lose his health.

The basic parameters of the Defender:
health = 60
attack = 3
defense = 2

![alt text](https://py-static.checkio.org/media/task/media/105a2136dc67401c809d4a5d266ddf3e/warrior_vs_defender.png)

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

my_army = Army()
my_army.add_units(Defender, 1)
    
enemy_army = Army()
enemy_army.add_units(Warrior, 2)

army_3 = Army()
army_3.add_units(Warrior, 1)
army_3.add_units(Defender, 1)

army_4 = Army()
army_4.add_units(Warrior, 2)

battle = Battle()

battle.fight(my_army, enemy_army) == False
battle.fight(army_3, army_4) == True
```
<b>Input:</b> The warriors and armies.

<b>Output:</b> The result of the battle (True or False).

<b>How it is used:</b> For the computer games development.

<b>Note:</b> From now on, the tests from "check" part will use another type of warrior: the rookie. Its code is
```
class Rookie(Warrior):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.health = 50
        self.attack = 1
```
<b>Precondition:</b> 3 types of units