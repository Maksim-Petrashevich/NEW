import random
def is_prime(arg1):
    k = 0
    for i in range(2, arg1 // 2 + 1):
        if (arg1 % i == 0):
            k = k + 1
    if (k <= 0):
      return True
    else:
        return False
print("Работа функции проверки на (не )простое число")
a = int(input("Введите число: "))
if is_prime(a) is True:
    print("Число простое")
else:
    print("Число не является простым")
def argument(input):
    if isinstance(input, list):
        return sum(input)
    elif isinstance(input, dict):
        for val in input.values():
            sorted_val=sorted(input.values())
            return sorted_val[:-4:-1]
    elif isinstance(input, int):
        if isinstance(input, float):
            input = int(input)
        if input < 0:
            input = abs(input)
        return sum(int(digit) for digit in str(input))
    elif isinstance(input, str):
        words=input.split()
        return len(words)
    else:
        return "Неизвестный тип данных"
print("Работа функции с агрументами")
print(argument([1, 2, 3, 4]))
print(argument({'a':4, 'b': 6, 'c':0, 'd':7,'e':9}))
print(argument(12345))
print(argument("Это строка"))
def findpositive(matrix):
    for rew in matrix:
        if all(x>=0 for x in row):
            return row, sum(row)
        return None, 0
print("Работа функции с матрицей")
row=int(input("Введите количество строк: "))
cols=int(input("Введите количество столбцов: "))
matrix = []
for _ in range(row):
    row = [random.randint(-10, 10) for _ in range(cols)]
    matrix.append(row)
for i in matrix:
    print(i)
result, summ = findpositive(matrix)
if result:
    print(f"\nПервая строка, в которой все элементы положительные: {result}")
    print(f"\nСумма элементов строки: {summ}")
else:
    print(f"\nВ матрице нет строки, в которой все элементы положительные")
    print("Работает фукнция try/except/finally")
def divide(a, b):
    try:
        result = a/b
    except ZeroDivisionError:
        print("Ошибка: деление на 0")
        result=None
    finally:
        print("Ввыполнение блока finally")
        return result
try:
    x=5
    y=0
    result = divide(x, y)
    print (f"Результат деления {x} на {y}={result}")
except Exception as e:
    print(f"Произошла ошибка: {e}")
