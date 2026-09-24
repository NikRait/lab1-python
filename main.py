# Вывод приветствия
print("Hello, World!")
# Print student name
name = "Golev Sergey"
print(f"Студент: {name}")
# DATA
print("Дата: 2026-09-10")


def square(x: int) -> int:
    return x * x


number = 7
result = square(number)
print(f"Число: {number}")
print(f"Квадрат: {result}")


# Factorial
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

n = 10
print(f"Factorial for {n} = {factorial(5)}")  # Output: 120