# task 1
# player = {'name':'', 'health': 100, 'damage': 30}
# enemy = {'name':'', 'health': 100, 'damage': 20}
#
# def name_player(name):
#     player['name'] = name
#
# def name_enemy(name):
#     enemy['name'] = name
#
# inputPlayerName = name_player(input('Имя героя: '))
# inputEnemyName = name_enemy(input('Имя врага: '))
#
# def attack(person1, person2):
#     person2['health'] -= person1['damage']
#
# def whoIsAttack(name):
#     if name == player['name']:
#         attack(player, enemy)
#     else:
#         attack(enemy, player)
#
# inputWhoIsAttack = whoIsAttack(input('Введите имя атакующего: '))
#
# print(player)
# print(enemy)

# task 2

player = {'name':'', 'health': 100, 'damage': 30, 'armor': 1.2}
enemy = {'name':'', 'health': 100, 'damage': 20, 'armor': 1.2}

def writeFile(hero):
    with open(str(hero['name'])+'.txt', 'w', encoding = 'utf-8') as file:
        for k, d in hero.items():
            file.write(str(k)+':'+str(d)+'\n')

def readFile(hero):
    with open(str(hero['name']) + '.txt', 'r', encoding='utf-8') as file:
        for line in file:
            line = line.strip('\n')            
            k = line.split(':')[0]
            if k in hero.keys():
                try:
                    hero[k] = float(line.split(':')[1])
                except ValueError:
                    hero[k] = line.split(':')[1]

def name_player(name):
    player['name'] = name
    writeFile(player)

def name_enemy(name):
    enemy['name'] = name
    writeFile(enemy)

inputPlayerName = name_player(input('Имя героя: '))
inputEnemyName = name_enemy(input('Имя врага: '))

def attack(person1, person2):
    damage = realDamage(person1['damage'], person2['armor'])
    person2['health'] -= damage
    game(person1, person2)
    # writeFile(person1)
    # writeFile(person2)

def realDamage(damageP1, armorP2):
    damage = damageP1/armorP2
    return damage

def whoIsAttack(name):
    readFile(player)
    readFile(enemy)
    if name == player['name']:
        attack(player, enemy)
    else:
        attack(enemy, player)

def game(person1, person2):
    if person1['health']>0 and person2['health']>0:
        attack(person2, person1)
        # print(person1, person2)
    elif person1['health']<=0:
        print('Победителем стал:', person2['name'], 'здоровье:', person2['health'])
    else:
        print('Победителем стал:', person1['name'], 'здоровье:', person1['health'])

inputWhoIsAttack = whoIsAttack(input('Введите имя атакующего: '))
