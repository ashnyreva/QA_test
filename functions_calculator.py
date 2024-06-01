def plus(one: float, two: float) -> float:
    """
    Выполняет действие сложения
    :param one: первое слагаемое
    :param two: второе слагаемое
    :return: сумма
    """
    res = one + two
    return res


def minus(one: float, two: float) -> float:
    """
    Выполняет действие вычитания
    :param one: уменьшаемое
    :param two: вычитаемое
    :return: разность
    """
    res = one - two
    return res


def multiply(one: float, two: float) -> float:
    """
    Выполняет действие умножения
    :param one: первый множитель
    :param two: второй множитель
    :return: произведение
    """
    res = one * two
    return res


def divide(one: float, two: float) -> float:
    """
    Выполняет действие деления
    :param one: делимое
    :param two: делитель
    :return: частное
    """
    res = one / two
    return res


def beautify(one: float, two: float, res: float) -> tuple[float, float, float]:
    """
    Убирает дробную часть, если она 0. Для красоты
    :param one: первое число
    :param two: второе число
    :param res: результат операции
    :return: числа без дробной части, если она 0
    """
    if int(one) == one:
        one = int(one)
    if int(two) == two:
        two = int(two)
    if int(res) == res:
        res = int(res)
    return one, two, res


if __name__ == '__main__':
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
                result = plus(first, second)
            elif operator == '-':
                result = minus(first, second)
            elif operator == '*':
                result = multiply(first, second)
            elif operator == '/':
                result = divide(first, second)
            else:
                # мы не должны сюда попасть, эта ошибка проверена выше
                raise ValueError(f'нет такой операции: "{operator}"')
            first, second, result = beautify(first, second, result)
            # вывод результата
            print(f'{first} {operator} {second} = {result}')
        except ValueError as e:
            print('Некорректный ввод:', e)
        except ZeroDivisionError:
            print('Делить на 0 нельзя!')

        command = input('Нажмите Enter для продолжения или введите "stop" для выхода из программы: ')
        if command.lower() == 'stop':
            break
        elif command:
            print(f'Вы ввели некорректное значение: "{command}"')
