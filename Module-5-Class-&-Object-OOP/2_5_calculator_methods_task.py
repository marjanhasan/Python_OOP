class Calculator:
    brand = "Casio MS-990"

    def add(self, a, b):
        res = a + b
        return res

    def sub(self, a, b):
        res = a - b
        return res

    def mul(self, a, b):
        res = a * b
        return res

    def div(self, a, b):
        res = a / b
        return res


my_calc = Calculator()
addition = my_calc.add(5, 8)
print(addition)
subtraction = my_calc.sub(8, 5)
print(subtraction)
multiplication = my_calc.mul(8, 5)
print(multiplication)
division = my_calc.div(15, 3)
print(division)
