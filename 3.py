N = int(input("Введите максимальное число: "))
possible_numbers = set(range(1, N + 1))

while True:
    line = input("Нужное число есть среди вот этих чисел: ").strip()
    if line == "Помогите!":
        break
    guessed_numbers = set(map(int, line.split()))
    answer = input("Ответ Ивана:").strip()

    if answer == "Да":
        possible_numbers = possible_numbers.intersection(guessed_numbers)
    elif answer == "Нет":
        possible_numbers = possible_numbers.difference(guessed_numbers)
    else:
        print("Некорректный ответ")
print("Иван мог загадать следующие числа:", *sorted(possible_numbers))