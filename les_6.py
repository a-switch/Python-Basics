
class Person:
    def __init__(self, name, health = 100, damage=30, armor = 1.2):
        self.name = name
        self.health = health
        self.damage = damage
        self.armor = armor
        self.hero = {'name': self.name, 'health': self.health, 'damage': self.damage, 'armor': self.armor}



class Player(Person):
    pass
    # def __init__(self, player_name):
    #     self.name = player_name
    # pass

class Enemy(Person):
    pass
    # def __init__(self, enemy_name):
    #     self.name = enemy_name

player1 = Player('ivan',100 ,40, 1.5)
print(player1.hero)

player2 = Enemy('zmey',100 ,35, 1.6)
print(player2.hero)
