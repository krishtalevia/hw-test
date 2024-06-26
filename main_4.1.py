import math

def input_number(number: str) -> float:
    while True:
        try:
            return float(input(number))
        except ValueError:
            print('Неподходящий тип данных! Введите снова.')
            continue

# 1 (Квадратное уравнение)

def quadratic_equation():
    print('Введите коэффициенты a, b и c для уравнения ax^2 + bx + c = 0')
    a = input_number('a = ')
    b = input_number('b = ')
    c = input_number('c = ')

    if (a == 0) or (b == 0):
        print('Коэффициенты равны нулю!')
        return

    discriminant = b ** 2 - 4 * a * c

    if discriminant > 0:
        root_1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root_2 = (-b - math.sqrt(discriminant)) / (2 * a)
        print('Корни уравнения: ', root_1, 'и', root_2)

    elif discriminant == 0:
        root = -b / (2 * a)
        print('Единственный корень уравнения: ', root)

    else:
        print('У уравнения нет действительных корней')

# 2 (Площадь треугольника)

def triangle_area():
    print('Введите длины сторон треугольника a, b и c')
    a = input_number('a = ')
    b = input_number('b = ')
    c = input_number('c = ')

    if (a + b > c) and (a + c > b) and (b + c > a):
        p = (a + b + c) / 2
        area = math.sqrt(p * (p - a) * (p - b) * (p - c))
        print('Площадь треугольника: ', area)
    else:
        print('Треугольник с такими сторонами не может существовать!')

# 3 (Конвертация температуры)

def temperature_conversion():
    print('Введите номер опции: ')
    print('1. Конвертировать Цельсий в Фаренгейт')
    print('2. Конвертировать Фаренгейт в Цельсий')
    choice = input('')

    if choice == '1':
        celsius = input_number('Введите температуру в градусах Цельсия: ')
        fahrenheit = (celsius * 9/5) + 32
        print('Температура в градусах Фаренгейта: ', fahrenheit)
    elif choice == '2':
        fahrenheit = input_number('Введите температуру в градусах Фаренгейта: ')
        celsius = (fahrenheit - 32) * 5/9
        print('Температура в градусах Цельсия: ', celsius)
    else:
        print('Неправильный выбор!')

quadratic_equation()
triangle_area()
temperature_conversion()