import random
import os
import time
from random import randint

print('Привет, предлагаю на выбор любую из 8 игр'
      '\n Угадай число = 1'
      '\n Виселица = 2'
      '\n Сгенерировать пароль = 3'
      '\n Камень-ножницы-бумага = 4'
      '\n Последовательность фибоначи = 5'
      '\n Простые числа = 6'
      '\n Калькулятор = 7'
      '\n Игра в "очко" = 8')


def number():
    random_number = random.randint(1, 100)
    user_guess = 0
    print('Я загадал число от 1 до 100, попробуй его угадать!')
    while user_guess != random_number:
        user_guess = int(input('> '))
        if random_number > user_guess:
            print('Больше, чем {}!'.format(user_guess))
        elif random_number < user_guess:
            print('Меньше, чем {}!'.format(user_guess))
        else:
            print('Верно! Я загадал число {}'.format(random_number))


def suicide():
    list_of_words = [
        'яблоко',
        'виселица',
        'программирование',
        'терминал',
        'ноутбук'
    ]
    random_word = list_of_words[random.randint(0, len(list_of_words) - 1)]
    set_of_symbols = set(random_word)
    discovered_symbols = set()
    health = 5
    print('_ ' * len(random_word))
    while discovered_symbols != set_of_symbols and health > 0:
        user_symbol = input('> ')
        assert len(user_symbol) == 1
        if user_symbol in discovered_symbols:
            print('Вы уже вводили эту букву, попробуйте что-нибудь другое')
        elif user_symbol not in set_of_symbols:
            health -= 1
            print('Этой буквы нет в слове. Текущее кол-во жизней: {}'.format(health))
        elif user_symbol in set_of_symbols:
            print('Буква есть в слове!')
            discovered_symbols.add(user_symbol)

        current_word_progress = ''
        for ch in random_word:
            current_word_progress += '_ ' if ch not in discovered_symbols else ch + ' '
        print(current_word_progress)
    if health == 0:
        print('Жизни закончились :(')
    else:
        print('Поздравляю, вы правильно набрали слово {}'.format(random_word))


def password():
    password = []
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(65, 90)))  # верхний регистр
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(97, 122)))  # нижний регистр
    for i in range(random.randint(2, 4)):
        password.append(chr(random.randint(48, 57)))  # цифры
    # for i in range(random.randint(2, 4)):
    # password.append(chr(random.randint(33, 148))) # специальные знаки
    random.shuffle(password)
    print('Сгенерированный пароль: {}'.format(''.join(password)))


def paper_stone_scissors():
    t = ["Камень", "Бумага", "Ножницы"]
    computer = t[randint(0, 2)]
    player = False
    while player == False:
        player = input("Камень, Ножницы, Бумага? > ")
        if player == computer:
            print("Ничья!")
        elif player == "Камень":
            if computer == "Бумага":
                print("Ты проиграл!", computer, "накрывает", player)
            else:
                print("Ты выиграл!", player, "разбивает", computer)
        elif player == "Бумага":
            if computer == "Ножницы":
                print("Ты проиграл!", computer, "режет", player)
            else:
                print("Ты победил!", player, "накрывает", computer)
        elif player == "Ножницы":
            if computer == "Камень":
                print("Ты проиграл!", computer, "разбивает", player)
            else:
                print("Ты выиграл!", player, "режет", computer)
        else:
            print("Некорректный ход!")
        player = False
        computer = t[randint(0, 2)]


def fibo():
    def fibSequence(n):
        assert n > 0
        series = [1]
        while len(series) < n:
            if len(series) == 1:
                series.append(1)
            else:
                series.append(series[-1] + series[-2])
        for i in range(len(series)):
            series[i] = str(series[i])
        return ('\n'.join(series))

    print(fibSequence(int(input('Сколько чисел? '))))


def easy_numbers():
    def isPrime(x):
        if x == 2:
            return True
        if x % 2 == 0:
            return False
        for i in range(3, int(x ** 0.5) + 1, 2):
            if x % i == 0:
                return False
        return True

    def genPrime(currentPrime):
        newPrime = currentPrime + 1
        while True:
            if not isPrime(newPrime):
                newPrime += 1
            else:
                break
        return newPrime

    currentPrime = 2
    while True:
        answer = input('Показать следующее простое число? (Y/N) ')
        if answer.lower().startswith('y'):
            print(currentPrime)
            currentPrime = genPrime(currentPrime)
        else:
            break


def math_calc():
    def calc(a, b, op):
        if op not in '+-/*':
            return 'Пожалуйста, выберите тип операции: "+, -, *, /"!'
        if op == '+':
            return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a + b))
        if op == '-':
            return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a - b))
        if op == '*':
            return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a * b))
        if op == '/':
            return (str(a) + ' ' + op + ' ' + str(b) + ' = ' + str(a / b))

    def main():
        a = int(input('Пожалуйста, введите первое число: '))
        b = int(input('Пожалуйста, введите второе число: '))
        op = input(
            'Какой вид операции Вы желаете осуществить?\
            \nВыберите между "+, -, *, /" : ')
        print(calc(a, b, op))

    if __name__ == '__main__':
        main()


def twenty_one():
    score_playera = 0
    score_bota = 0

    all_carts = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
    print("Поиграем в 21? \nЕсли хотите играть нажмите Enter, если хотите выйти, то нажмите Ctrl + C")
    input()
    os.system('CLS')

    while True:
        if score_playera == 21:
            print("Больше карт не надо, у вас 21")
            print("Вы автоматически победили бота, так как у вас 21.")
            input("Нажмите Enter, чтобы закрыть окно.");
            break
        if score_playera > 21:
            print("Вы проиграли, так как набрали больше 21")
            print("Попытайте свою попытку в другой раз.")
            input("Нажмите Enter, чтобы закрыть окно.");
            break
        yes_or_no = input("Будете ли вы брать карту?\nВведите y, "
                          "если хотите брать карту или введите n, "
                          "если не берете карту.\n")
        os.system('CLS')
        if yes_or_no == 'y':
            os.system('CLS')
            score_carts = random.choice(all_carts)
            print("Вы взяли карту выпало:", score_carts)
            score_playera += score_carts
            print("Сейчас у вас ", score_playera)
        if yes_or_no == 'n':
            print("У вас ", score_playera, "очков.")
            print("Ход бота")
            time.sleep(3)
            os.system('CLS')
            while True:
                print("У вас ", score_playera, "очков.")
                if score_bota > 21:
                    print("Бот проиграл.\nТак как у него больше 21")
                    input("Нажмите Enter, чтобы закрыть");
                    exit(0)
                if score_bota > score_playera:
                    print("Бот победил.\nТак как у него",
                          score_bota,
                          "очков, а у вас ",
                          score_playera,
                          "\nНе растраивайтесь. Попробуйте ещё раз.")
                    input("Нажмите Enter, чтобы закрыть");
                    exit(0)
                if score_bota == score_playera:
                    print("Вы набрали равное количество очков и у вас ничья")
                    input("Нажмите Enter, чтобы закрыть");
                    exit(0)
                if score_bota < 21:
                    score_carts = random.choice(all_carts)
                    print("Боту выпало", score_carts, "очков.")
                    score_bota += score_carts
                    print("У бота ", score_bota, "очков.")
                    time.sleep(3)
                    os.system('CLS')


class switch(object):
    def __init__(self, value):
        self.value = value
        self.fall = False

    def __iter__(self):
        yield self.match
        raise StopIteration

    def match(self, *args):
        if self.fall or not args:
            return True
        elif self.value in args:
            self.fall = True
            return True
        return False


def run():
    global choose
    while True:
        number = input()
        if number.isdigit():
            choose = int(number)
            if choose > 8 or choose < 0:
                print('Введите число от 1 до 8')
                continue
            else:
                break
        else:
            print('Введите число от 1 до 8')
            continue
    try:
        for case in switch(choose):
            if case(1):
                number()
                break
            if case(2):
                suicide()
                break
            if case(3):
                password()
                break
            if case(4):
                paper_stone_scissors()
            if case(5):
                fibo()
                break
            if case(6):
                easy_numbers()
                break
            if case(7):
                math_calc()
                break
            if case(8):
                twenty_one()
                break
    except Exception:
        print('Введите число от 1 до 8')


run()
