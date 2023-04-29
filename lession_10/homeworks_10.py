"""
Текстова гра на тему Українських народних казок
Правила гри:
    Гравець має обирати персонажа, за яким він буде грати. Потім гравець починає свою
    пригоду у вигляді текстових повідомлень. Гра складається з декількох етапів, на кожному з яких гравець зустрічає нових
    персонажів та переживає різні пригоди. Гравець має право вибирати, як він хоче діяти у певній
    ситуації: діалог з персонажем, бій, втеча тощо. Залежно від вибору гравця, відбуваються різні
    наслідки.

Приклади:

* Гравець обирає персонажем козака. Він зустрічає чаклуна, який накладає на нього прокляття.
    Гравець може спробувати розв'язати прокляття, знайти антидот або битися з чаклуном.
    Залежно від вибору гравця, він може отримати нову здатність або втратити частину своїх вмінь.
* Гравець обирає персонажем пересмішника. Він потрапляє в хитру ситуацію, де йому потрібно
    обдурити злодія. Гравець може скористатися своїм словесним даром, знайти слабкі місця
    злодія або спробувати зібрати команду з іншими персонажами для змагання проти злодія.

Ідеї для  тестів:

    Тест на перевірку правильності вибору персонажа гравцем.
    Тест на перевірку вибору гравцем діалогу, який приводить до нової здатності персонажа.
    Тест на перевірку вибору гравцем діалогу, який приводить до втрати здатностей персонажа.
    Тест на перевірку правильності вибору гравцем
    Тест на введення некоректної відповіді гравцем: спроба ввести символи, відмінні від "так" і "ні".
    Тест на перехід до наступної дії: перевірка, чи збільшується лічильник після завершення попередньої.
    Тест на завершення гри: перевірка, що гравець не може перейти до наступної дії, якщо він вже завершив останню.
    Тест на вибір гравцем дії: перевірка, чи збільшується лічильник правильних відповідей після кожної правильної відповіді.

Поради до написання коду:

1. Створіть словник, що містить перелік персонажів та їх характеристик, таких як ім'я,
    рівень життя, сила тощо.
2. Запросіть у гравця вибір персонажа зі списку.
3. Визначте етапи гри, наприклад, "Зустріч з першим персонажем", "Бій з монстром",
    "Вирішення головоломки" тощо.
4. Для кожного етапу гри створіть функцію, яка відповідає за обробку цього етапу.
    Функція повинна виводити текстове повідомлення, яке описує ситуацію гравця,
    а також список доступних дій, які гравець може вибрати. Наприклад,
    "Ви зустрілися з гобліном. Що ви будете робити?
    1. Почати діалог з ним. 2. Розпочати бій. 3. Спробувати втекти".
5. Для кожної дії, яку може вибрати гравець, створіть окрему функцію.
    Функція повинна перевіряти, чи є ця дія можливою в поточній ситуації,
    і виконувати відповідні дії. Наприклад, якщо гравець вибирає
    "Розпочати бій", функція повинна розпочати бій з монстром і вивести повідомлення про результат.
6. Для обробки помилок та виключень, наприклад, якщо гравець ввів
    неправильне значення, використовуйте блоки try/except.
7. Для збереження прогресу гравця у грі, зберігайте дані у файл.

Не ускладнюйте собі життя:
Достатньо 3 персонажи та 3 дії а також 3  кроки:
    1. початок(вибір героя - Котигорошко, Змій, кінь)
    2. взаємодія(комп'ютер обирає героя з тих що лишилися і пропонує дії гравцю)
    3. розв'язка ( відповідно до обраних дій та коефіцієнтів - перемога, поразка чи нічия)
І треба хоча б 9 тестів на усе це добро.
"""

import random
from my_logger import logger


herous = {
'Ursa': {'power': 52, 'health': 600, 'speed': 6, 'money': 50},
'Warlock': {'power': 34, 'health': 1200, 'speed': 4, 'money': 0},
'Luna': {'power': 42, 'health': 780, 'speed': 7, 'money': 20}}

monsters = {
'Rohan': {'name': 'Roshanum', 'health': 1500, 'power': 30, 'speed': 2},
'Goblin': {'name': 'Goblin', 'health': 300, 'power': 15, 'speed': 5}
}

print("Hello, my dear guest. Let's try to play the game")

def start_game():
    while True:
        key_hero = input("Please make a choice! You have three herous to choose from(Ursa, Warlock and Luna): ").capitalize()
        try:
            if key_hero in herous:
                print(f"You hero is {key_hero}. It's not a bad choice.")
                print(f'Your skills: \n Health: {herous[key_hero]["health"]}\n Power: {herous[key_hero]["power"]}\n Speed: {herous[key_hero]["speed"]}\n Money: {herous[key_hero]["money"]}')  #Need to add a function with oppotunities of selected hero later
                logger.info(f'The hero was selected. Your hero is {key_hero}.')
                return key_hero
            else:
                raise ValueError('Something went wrong. Please try again to type a hero')
        except ValueError as mistake:
            print(mistake)



#start_game()

def random_monster():
    'This function is for selecting a monstar randomly'
    monster = None
    monster = random.choice(list(monsters))
    return monster

#random_monster()


def first_stage(monster, hero):
    print(f"Unfortunately, on the way to your goal you encountered {monster}.\nHis amount of health: {monsters[monster]['health']}, his power: {monsters[monster]['power']}")
    logger.info(f"Monster will be in the current game : {monster}")
    your_action = input("What are you gooing to do? Fight, Run or Compensate?" ).capitalize()
    print('You have chosen :', your_action)
    if your_action == 'Fight':
        logger.info('The hero decided to choose: fight')
        return fight_action(monster, hero)
    elif your_action == 'Run':
        logger.info('The hero decided to choose: run')
        return run_action(monster, hero)
    elif your_action == 'Compensate':
        logger.info('The hero decided to choose: compensate')
        return compensate_action(monster, hero)
    else:
        print("Your selected action looks weird. Please try again")
        logger.info('The user typed incorrect action')
        return first_stage(monster, hero)


def fight_action(monster, key_hero):
    'This is fight between you and random monster'
    if herous[key_hero]["power"] > monsters[monster]["power"]:
        herous[key_hero]["power"] += monsters[monster]["power"]
        print(f'Congratulations! You won, the {monster} was killed')
        logger.info('The hero is stronger than the monster')
    elif herous[key_hero]["power"] == monsters[monster]["power"]:
        herous[key_hero]["power"] += monsters[monster]["power"] / 2
        print(f'The fight was hard, but the draw won. Now you and {monster} are friends')
        logger.info('The hero was on an equal footing with the monster')
    else:
        monsters[monster]["power"] += herous[key_hero]["power"]
        print('Unfortunately, the monster is stronger than you, but today he is in a good mood and let you go')
        logger.info('The hero is weaker than the monster')

def run_action(monster, key_hero):
    'This is the run of life between monster and hero'
    if herous[key_hero]["speed"] > monsters[monster]["speed"]:
        herous[key_hero]["speed"] += monsters[monster]["speed"]
        print(f"Congratulations! The right choice, it's better not to put yourself at risk."
        f" {monster} can't catch up with you anymore")
        logger.info('The hero was faster than the monster')
    elif herous[key_hero]["speed"] == monsters[monster]["speed"]:
        herous[key_hero]["speed"] += monsters[monster]["speed"] / 2
        print(f"You had a gap at the start, the {monster} can't catch up with you")
        logger.info('The hero was on an equal footing with the monster')
    else:
        monsters[monster]["speed"] += herous[key_hero]["speed"]
        print(f"You're caught, but the {monster} doesn't need you")
        logger.info('The hero was slower than the monster')

def compensate_action(monster, key_hero):
    'This is compensate action between monster and hero'
    if herous[key_hero]["money"] > 0:
        monsters[monster]["money"] += herous[key_hero]["money"]
        print(f"{monster} didn't touch you, but he took all your money")
        logger.info('The hero paid off the monster')
    else:
        print("You can't negotiate because you have no money. Think again about what I say and choose an action")
        logger.info('The hero has no money')
        return first_stage(monster, key_hero)

my_hero = start_game()
met_monster = random_monster()
first_stage(met_monster, my_hero)
