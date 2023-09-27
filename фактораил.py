def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

n = int(input("Введите число: "))
if n < 0:
    print("Факториал не определен для отрицательных чисел")
else:
    print(f"Факториал {n} равен {factorial(n)}")
