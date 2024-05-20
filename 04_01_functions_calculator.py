def plus(one: float, two: float):
    """
    Выполняет действие сложения
    :param one: первое слагаемое
    :param two: второе слагаемое
    :return:
    """
    result = one + two
    one, two, result = beautify(one, two, result)
    # вывод результата
    print(f'{one} {operator} {two} = {result}')


def minus(one: float, two: float):
    """
    Выполняет действие вычитания
    :param one: уменьшаемое
    :param two: вычитаемое
    :return:
    """
    result = one - two
    one, two, result = beautify(one, two, result)
    # вывод результата
    print(f'{one} {operator} {two} = {result}')


def multiply(one: float, two: float):
    """
    Выполняет действие умножения
    :param one: первый множитель
    :param two: второй множитель
    :return:
    """
    result = one * two
    one, two, result = beautify(one, two, result)
    # вывод результата
    print(f'{one} {operator} {two} = {result}')


def divide(one: float, two: float):
    """
    Выполняет действие деления
    :param one: делимое
    :param two: делитель
    :return:
    """
    result = one / two
    one, two, result = beautify(one, two, result)
    # вывод результата
    print(f'{one} {operator} {two} = {result}')


def beautify(one: float, two: float, result: float):
    """
    Убирает дробную часть, если она 0. Для красоты
    :param one: первое число
    :param two: второе число
    :param result: результат операции
    :return: числа без дробной части, если она 0
    """
    if int(one) == one:
        one = int(one)
    if int(two) == two:
        two = int(two)
    if int(result) == result:
        result = int(result)
    return one, two, result


while True:
    try:
        print('Введите первое число:')
        first = float(input())
        print('Введите оператор:')
        operator = input()
        if operator not in ('+', '-', '*', '/'):
            raise ValueError(f'нет такой операции: "{operator}"')
        print('Введите второе число:')
        second = float(input())
        if operator == '+':
            plus(first, second)
        elif operator == '-':
            minus(first, second)
        elif operator == '*':
            multiply(first, second)
        elif operator == '/':
            divide(first, second)
        else:
            # мы не должны сюда попасть, эта ошибка проверена выше
            raise ValueError(f'нет такой операции: "{operator}"')
    except ValueError as e:
        print('Некорректный ввод:', e)
    except ZeroDivisionError:
        print('Делить на 0 нельзя!')

    command = input('Нажмите Enter для продолжения или введите "stop" для выхода из программы: ')
    if command.lower() == 'stop':
        break
    elif command:
        print(f'Вы ввели некорректное значение: "{command}"')
