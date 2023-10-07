class VeryLong:
    def __init__(self, num_str):
        # Видалити зайві нулі з початку числа
        num_str = num_str.lstrip('0')
        # Якщо після видалення нулів число порожнє, замінити його на "0"
        self.value = num_str if num_str else '0'

    # Перевизначення оператора віднімання
    def __sub__(self, other):
        result = []
        num1 = self.value.rjust(len(other.value), '0')
        num2 = other.value.rjust(len(self.value), '0')
        borrow = 0 # відслідковування позичення з іншого розряду

        for i in range(len(num1) - 1, -1, -1):
            digit = int(num1[i]) - int(num2[i]) - borrow # Обчислення різниці поточних розрядів
            # Позичення із іншого розряду
            if digit < 0: # Зберігання поточного розряду при виконанні віднімання чисел
                digit += 10 
                borrow = 1
            else:
                borrow = 0
            result.append(str(digit)) # Додавання десятки із іншого розряду, якщо не вистачає
        return VeryLong(''.join(result[::-1]))

    # Перевизначення оператора ділення 
    def __truediv__(self, other):
        num1 = int(self.value)
        num2 = int(other.value)

        # Функція для перевірки ділення на 0
        if num2 == 0:
            print("Помилка: ділення на нуль!")
            return VeryLong('0')
        # Операція ділення та повернення значення у типі str
        Riznitsya = num1 // num2
        return VeryLong(str(Riznitsya))

    # Перевизначення оператора додавання 
    def __add__(self, other):
        result = []
        num1 = self.value.rjust(len(other.value), '0') # Метод вирівнювання чисел до одного і того ж розміру перед виконанням операції
        num2 = other.value.rjust(len(self.value), '0')
        perenos = 0 # У додаванні чисел зправа на ліво, коли один розряд числа більший за розряд іншого числа, додавання цих двох розрядів може призвести до "переносу" - додаткової одиниці, яку потрібно додати до наступного меншого розряду

        for i in range(len(num1) - 1, -1, -1): # Перебір розрядів чисел з право на ліво
            digit_sum = int(num1[i]) + int(num2[i]) + perenos # Обчислення суми поточних розрядів
            perenos = digit_sum // 10 
            digit_sum %= 10 # Вказує на суму поточних розрядів чисел під час додавання
            result.append(str(digit_sum)) # Результат суми 1 розряду + 2 розряду + perenos
        if perenos > 0: # Перевіряє чи можливий перенос між розрядами
            result.append(str(perenos)) # додає перенос до результату
        return VeryLong(''.join(result[::-1]))

    # Перевизначення оператора множення 
    def __mul__(self, other):
        num1 = self.value
        num2 = other.value
        result = VeryLong('0') # Початкове значення результату

        for i in range(len(num2) - 1, -1, -1): # Перебір розрядів чисел з право на ліво
            digit = int(num2[i]) # Збереження поточного розряду змінної num2
            partial_result = VeryLong('0')
            perenos = 0
            for j in range(len(num1) - 1, -1, -1): # Перебір розрядів чисел з право на ліво
                product = int(num1[j]) * digit + perenos # Обчислення добутку поточних розрядів
                perenos = product // 10
                product %= 10 # Зберігає залишок від ділення product на 10, який буде використовуватися як розряд
                partial_result.value = str(product) + partial_result.value
            if perenos > 0: # Перевіряє чи можливий перенос між розрядами
                partial_result.value = str(perenos) + partial_result.value # Додає необхідну кількість нулів, залежно від розряду, який обробляється у цій ітераці
            partial_result.value += '0' * (len(num2) - 1 - i)
            result += partial_result

        return result

    # Перевизначення оператора для  виведення у рядок
    def __str__(self):
        return self.value