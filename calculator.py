from VeryLong import VeryLong

class Calculator:
    @staticmethod
    def suma(num1, num2):
        if isinstance(num1, VeryLong) and isinstance(num2, VeryLong):
            # Перевірка, чи обидва аргументи є об'єктами класу VeryLong
            # Реалізація операції додавання для VeryLong
            return num1 + num2
        else:
            return "Помилка: аргументи повинні бути об'єктами класу VeryLong"
    
    @staticmethod
    def riz(num1, num2):
        if isinstance(num1, VeryLong) and isinstance(num2, VeryLong):
            # Перевірка, чи обидва аргументи є об'єктами класу VeryLong
            # Реалізація операції віднімання для VeryLong
            return num1 - num2
        else:
            return "Помилка: аргументи повинні бути об'єктами класу VeryLong"
    
    @staticmethod
    def dobutok(num1, num2):
        if isinstance(num1, VeryLong) and isinstance(num2, VeryLong):
            # Перевірка, чи обидва аргументи є об'єктами класу VeryLong
            # Реалізація операції множення для VeryLong
            return num1 * num2
        else:
            return "Помилка: аргументи повинні бути об'єктами класу VeryLong"
    
    @staticmethod
    def dilen(num1, num2):
        if isinstance(num1, VeryLong) and isinstance(num2, VeryLong) and num2 != 0:
            # Перевірка, чи обидва аргументи є об'єктами класу VeryLong і num2 не є 0
            # Реалізація операції ділення для VeryLong
            return num1 / num2
        else:
            return "Помилка: аргументи повинні бути об'єктами класу VeryLong і num2 не повинен бути 0"
        