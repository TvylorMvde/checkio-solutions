In the previous mission - Warriors - you've learned how to make a duel between 2 warriors happen. Great job! But let's move on to something that feels a little more epic - armies! In this mission your task is to add new classes and functions to the existing ones. The new class should be the <b>Army</b> and have the method <b>add_units()</b> - for adding the chosen amount of units to the army. The first unit added will be the first to go to fight, the second will be the second, ...

Also you need to create a <b>Battle()</b> class with a <b>fight()</b> function, which will determine the strongest army.

The battles occur according to the following principles:

at first, there is a duel between the first warrior of the first army and the first warrior of the second army. As soon as one of them dies - the next warrior from the army that lost the fighter enters the duel, and a new fight begins between him and the surviving warrior, who keeps his remaining health. This continues until all the soldiers of one of the armies die. In this case, the fight() function should return <b>True</b>, if the first army won, or <b>False</b>, if the second one was stronger.

Note that army 1 has the advantage to start every fight!

![alt text](https://py-static.checkio.org/media/task/media/8f856023648b4e48837e1d2df1b434ff/battle.png)

<b>Example:</b>
```
chuck = Warrior()
bruce = Warrior()
carl = Knight()
dave = Warrior()
mark = Warrior()

fight(chuck, bruce) == True
fight(dave, carl) == False
chuck.is_alive == True
bruce.is_alive == False
carl.is_alive == True
dave.is_alive == False
fight(carl, mark) == False
carl.is_alive == False

my_army = Army()
my_army.add_units(Knight, 3)

enemy_army = Army()
enemy_army.add_units(Warrior, 3)

army_3 = Army()
army_3.add_units(Warrior, 20)
army_3.add_units(Knight, 5)

army_4 = Army()
army_4.add_units(Warrior, 30)

battle = Battle()

battle.fight(my_army, enemy_army) == True
battle.fight(army_3, army_4) == False
```
<b>Input:</b> The warriors and armies.

<b>Output:</b> The result of the battle (True or False).

<b>How it is used:</b> For computer games development.

<b>Precondition:</b>

* 2 types of units
* For all battles, each army is obviously not empty at the beginning.