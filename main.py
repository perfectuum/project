print("____________________КАЛЬКУЛЯТОР______________________\n\n")

while True:
    try:
        name37 = float(input("Введите первое число: "))
        break
    except ValueError:
        print("Ошибка, введите число правильно: ")

while True:
    try:
        name38 = float(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка, введите число правильно: ")


znaki = """
Выберите действие: 
1. Арифметические операторы             
    + Сложение
    - Вычитание
    * Умножение
    / Деление
    // Целочисленное деление
    % Остаток от деления
    ** Возведение в степень

2. Операторы сравнения
    == Равно
    != Не равно
    > Больше
    < Меньше
    >= Больше или равно
    <= Меньше или равно

3. Логические операторы
    and Логическое И
    or Логическое ИЛИ
    not Логическое НЕ
    
4. Операторы принадлежности
    in Принадлежность
    not in Не принадлежность

5. Операторы тождественности
    is Тождественно
    is not Не тождественно
"""
print(znaki, "\n")

while True:
    name22 = input("Введите Ваш выбор: ")
    if name22 == "+":
        print("Ответ:", name37 + name38)
        break
    elif name22 == "-":
        print("Ответ:", name37 - name38)
        break
    elif name22 == "*":
        print("Ответ:", name37 * name38)
        break
    elif name22 == "/":
        if name38 == 0:
            print("Делить не 0 нельзя!")
        else:
            print("Ответ:", name37 / name38)
        continue
    elif name22 == "//":
        if name38 == 0:
            print("Делить на 0 нельзя!")
        else:
            print("Ответ:", name37 // name38)
        continue
    elif name22 == "%":
        if name38 == 0:
            print("Действие с 0 невозможно!")
        else:
            print("Ответ:", name37 % name38)
        continue
    elif name22 == "**":
        print("Ответ:", name37 ** name38)
        break
    elif name22 == "==":
        print("Ответ:", name37 == name38)
        break
    elif name22 == "!=":
        print("Ответ:", name37 != name38)
        break
    elif name22 == ">":
        print("Ответ:", name37 > name38)
        break
    elif name22 == "<":
        print("Ответ:", name37 < name38)
        break
    elif name22 == ">=":
        print("Ответ:", name37 >= name38)
        break
    elif name22 == "<=":
        print("Ответ:", name37 <= name38)
        break
    elif name22 == "and":
        print("Ответ:", bool(name37) and bool(name38))
        break
    elif name22 == "or":
        print("Ответ:", bool(name37) or bool(name38))
        break
    elif name22 == "not":
        print("Ответ для первого числа:", not bool(name37))
        print("Ответ для второго числа:", not bool(name38))
        break
    elif name22 == "in":
        print("Ответ:", str(name37) in str (name38))
        break
    elif name22 == "not in":
        print("Ответ:", str(name37) not in str(name38))
        break
    elif name22 == "is":
        print("Ответ:", name37 is name38)
        break
    elif name22 == "is not":
        print("Ответ:", name37 is not name38)
        break
    elif name22 == "exit":
        print("Удачи на дорогах!")
        break
    else:
        print("Неправильный ввод, повторите попытку")




    
    
