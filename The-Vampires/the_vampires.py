class Warrior:

    def __init__(self):
        self.health = 50
        self.attack = 5

    def attacked(self, other):
        self.health -= other.attack
        if isinstance(other, Vampire):
            other.health += other.vampirism * other.attack

    @property
    def is_alive(self):
        return self.health > 0


class Knight(Warrior):

    def __init__(self):
        super().__init__()
        self.attack = 7


class Defender(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 60
        self.attack = 3
        self.defense = 2

    def attacked(self, other):
        damage = other.attack - self.defense
        if other.attack > self.defense:
            self.health -= damage
            if isinstance(other, Vampire):
                other.health += other.vampirism * damage


class Vampire(Warrior):

    def __init__(self):
        super().__init__()
        self.health = 40
        self.attack = 4
        self.vampirism = .5


def fight(first, second):
    while first.is_alive and second.is_alive:
        second.attacked(first)
        if second.is_alive:
            first.attacked(second)
    return first.is_alive


class Army:

    def __init__(self):
        self.units = []

    def add_units(self, obj, n):
        self.units.extend([obj() for x in range(n)])

    def __len__(self):
        return len(self.units)


class Battle:

    def fight(self, army1, army2):
        while len(army1) > 0 and len(army2) > 0:
            fight_result = fight(army1.units[0], army2.units[0])
            if fight_result:
                army2.units.pop(0)
            else:
                army1.units.pop(0)
        if len(army1) > 0:
            return True
        else:
            return False


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing

    #fight tests
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

    assert fight(chuck, bruce) == True
    assert fight(dave, carl) == False
    assert chuck.is_alive == True
    assert bruce.is_alive == False
    assert carl.is_alive == True
    assert dave.is_alive == False
    assert fight(carl, mark) == False
    assert carl.is_alive == False
    assert fight(bob, mike) == False
    assert fight(lancelot, rog) == True
    assert fight(eric, richard) == False
    assert fight(ogre, adam) == True

    #battle tests
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

    assert battle.fight(my_army, enemy_army) == False
    assert battle.fight(army_3, army_4) == True
    
    print("Coding complete? Let's try tests!")
