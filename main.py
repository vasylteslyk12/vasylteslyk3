# Імпорт класів VeryLong та Calculator із відповідних файлів
from VeryLong import VeryLong
from calculator import Calculator

def main():
# Введення значень двох чисел (num1, num2)
    num1_str = input("Введіть перше число: ")
    num2_str = input("Введіть друге число: ")

# Пертворення даних типу string в об'єкти класу VeryLong
    num1 = VeryLong(num1_str)
    num2 = VeryLong(num2_str)

# Створення нового об'єкта класу Calculator
# Виклик відповідних методів класу Calculator
    calc = Calculator()
    suma = calc.suma(num1, num2)
    riz = calc.riz(num1, num2)
    dobutok = calc.dobutok(num1, num2)
    dilen = calc.dilen(num1, num2)

# Форматований вивід результату виконання методів
    print(f"Сума = {suma}")
    print(f"Різниця = {riz}")
    print(f"Добуток = {dobutok}")
    print(f"Частка = {dilen}")

if __name__ == "__main__":
    main()

