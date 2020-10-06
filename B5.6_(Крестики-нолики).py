# В консоль вводить всё на русском: и 'х', и 'о', и тд. И да вместо '0' буква 'о'.
# Да, я знаю что в задании не было сказано про цветные списки и выборы, но я попытался сделать максимально удобную и многофункциональную (если так можно сказать) игру.

from colorama import Fore, Style
from random import randint


def win(list_):  # Проверка победы
    length = len(list_)
    x = ['х', 'х', 'х']
    o = ['о', 'о', 'о']
    if any([list_[0] == o,  # Строки

            list_[1] == o,

            list_[2] == o,

            [list_[i][0] for i in range(length)] == o,  # Столбцы

            [list_[i][1] for i in range(length)] == o,

            [list_[i][2] for i in range(length)] == o,

            [list_[i][i] for i in range(length)] == o,  # Диагональ

            [list_[length-1-i][i] for i in range(length)] == o,  # Обратная диагональ

            list_[0] == x,  # Строки

            list_[1] == x,

            list_[2] == x,

            [list_[i][0] for i in range(length)] == x,  # Столбцы

            [list_[i][1] for i in range(length)] == x,

            [list_[i][2] for i in range(length)] == x,

            [list_[i][i] for i in range(length)] == x,  # Диагональ

            [list_[length-1-i][i] for i in range(length)] == x  # Обратная диагональ
            ]):
        return 1  # Значит победа


def draw(list_):
    count = 0
    for i in range(len(list_)):
        for j in range(len(list_)):
            if list_[i][j] == '-':
                count += 1
    if count == 0:
        return count  # Значит ничья


def print_list(list_):  # Вывод поля игры
    for i in range(len(list_)):
        for j in range(len(list_)):
            if any([list_[i][j] == 'о',
                    list_[i][j] == 'х',
                    list_[i][j] == '-']):
                print(Fore.RED, list_[i][j], end=' ')
            else:
                print(Fore.BLUE, list_[i][j], end=' ')
        print(Style.RESET_ALL)
    print()


playing_field_reserve = [['-' for i in range(3)] for j in range(3)]  # Генератор списка для проверки


playing_field = [[' ', '0', '1', '2'],  # Список для пользователя
                 ['0', '-', '-', '-'],
                 ['1', '-', '-', '-'],
                 ['2', '-', '-', '-']]

# Если ввели неверно, то проверка и заново
while True:
    choice_player = input("Выберите за кого играть: 'о' или 'х'\n")
    if choice_player == 'о' or choice_player == 'х':
        break
    else:
        print("Вы ввели не верно (может быть другая расскладка)\n")

user_turn = 'х' if choice_player == 'х' else 'о'
random_turn = 'о' if user_turn == 'х' else 'х'
print()

# Если ввели неверно, то проверка и заново
while True:
    first_move = input("Выбирете кто делает первый ход: 'я', 'компьютер', 'случайно'\n")
    if any([first_move == 'я',
            first_move == 'компьютер',
            first_move == 'случайно']):
        break
    else:
        print("Вы ввели не верно (может быть другая расскладка)\n")
if first_move == 'компьютер':
    first_move = 1
elif first_move == 'случайно':
    first_move = randint(0, 1)
else:
    first_move = 0
print()

print_list(playing_field)

# Основная программа (процесс игры)
while True:
    if first_move == 0:  # Если первый ход не мой
        print("\nВаш ход")
    while True:  # Ход игрока
        if first_move == 1:  # Если первый ход не мой
            first_move = 0
            break
        i_user, j_user = int(input("Введите строку: ")) + 1, int(input("Введите столбец: ")) + 1
        if any([i_user < 0,  # Проверка индека
                i_user > 3,
                j_user < 0,
                j_user > 3]):
            print(Fore.GREEN, "Неверный индекс, введите строку и столбец заново", Style.RESET_ALL, '\n')
            continue
        elif any([playing_field[i_user][j_user] == 'х',  # Проверка занято или нет
                  playing_field[i_user][j_user] == 'о']):
            print(Fore.GREEN, "Ячейка занята, выберете другую", Style.RESET_ALL, '\n')
            continue
        else:
            playing_field[i_user][j_user] = user_turn  # Присвоение новой ячейки в основном списке
            playing_field_reserve[i_user-1][j_user-1] = user_turn  # Присвоение новой ячейки во втором списке
            print_list(playing_field)  # Показать обновленный список
            break

# Проверка победы
    verify_win = win(playing_field_reserve)
    if verify_win == 1:
        print("Вы выиграли")
        break

# Проверка ничьи
    check_draw = draw(playing_field_reserve)
    if check_draw == 0:
        print("Ничья")
        break

    print("\nХод компьютера")

    while True:
        i_random, j_random = randint(1, 3), randint(1, 3)  # Случайный индекс
        if any([i_random < 0,  # Проверка индека
                i_random > 3,
                j_random < 0,
                j_random > 3]):
            continue
        elif any([playing_field[i_random][j_random] == 'х',  # Проверка занято или нет
                  playing_field[i_random][j_random] == 'о']):
            continue
        else:
            playing_field[i_random][j_random] = random_turn  # Присвоение новой ячейки в основном списке
            playing_field_reserve[i_random-1][j_random-1] = random_turn  # Присвоение новой ячейки во втором списке
            break

    print_list(playing_field)  # Показать обновленный список

# Проверка победы
    verify_win = win(playing_field_reserve)
    if verify_win == 1:
        print()
        print("Вы проиграли")
        break

# Проверка ничьи
    check_draw = draw(playing_field_reserve)
    if check_draw == 0:
        print()
        print("Ничья")
        break
