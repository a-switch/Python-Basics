name = input('Введите ваше имя: ')
last_name = input('Введите вашу фамилию: ')
age = input('Введите ваш возраст: ')
weight = input('Введите ваш вес: ')

# age = int(input('Введите ваш возраст: '))
# weight = int(input('Введите ваш вес: '))

while bool(name) is False or bool(last_name) is False or bool(age) is False or bool(weight) is False:
    if bool(name) is False:
        name = input('Вы не введи имя. Введите ваше имя: ')
    elif bool(last_name) is False:
        last_name = input('Вы не ввели фамилию. Введите вашу фамилию: ')
    elif bool(age) is False:
        age = input('Вы забыли указать возраст. Ваш возраст: ')
    elif bool(weight) is False:
        weight = input('Вы забыли указать вес. Ваш вес: ')

def digit(x):
    y = int(x)
    return y

while type(age) != int:
    try:
        age = int(age)
        age = digit(age)
    except ValueError:
        age = input('Вы ввели в поле "возраст" не число. Введите цифры: ')

while type(weight) != int:
    try:
        weight = int(weight)
        weight = digit(weight)
    except ValueError:
        weight = input('Вы ввели в поле "вес" не число. Введите цифры: ')

def diagnosis(age, weight):
    if age <= 30 and 50 <= weight <= 120:
        epic = 'хорошее состояние'
    elif age <= 30 and 50 >= weight:
        epic = 'больше лопай каши!'
    elif 30< age <=40 and 50 >= weight >= 120:
        epic = 'следует заняться собой'
    elif 30< age <=40 and 50 <= weight <= 120:
        epic = 'хорошее состояние'
    elif 40< age <= 50 and 50 >= weight >= 120:
        epic = 'следует записаться к врачу на осмотр'
    elif 40< age <= 50 and 50 >= weight >= 120:
        epic = 'следует записаться к врачу на осмотр'
    elif age > 50:
        epic = 'пора пожить в свое удовольствие'
    return epic

print(name, last_name + ',', age, 'год' + ',', 'вес', weight, '-', diagnosis(age, weight))
