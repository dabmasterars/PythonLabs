file_rus = "russian.txt"
file_eng = "english.txt"

with open(file_rus, 'r', encoding='utf-8') as f:
    russian_words = f.read().splitlines()
with open(file_eng, 'r', encoding='utf-8') as f:
    english_words = f.read().splitlines()

if len(russian_words) != len(english_words):#проверка, одинаковое ли кол-во строк
    print("Количество слов в файлах не совпадает")
    exit()

total = 0
correct = 0

for i in range(len(russian_words)):
    rus_word = russian_words[i]
    correct_translation = english_words[i]

    print("Слово:",rus_word)
    user_input = input("Ваш перевод:").strip()

    total += 1
    if user_input.lower() == correct_translation.lower():
        print("Верно")
        correct += 1
    else:
        print("Неверно, правильный перевод:",correct_translation)

print("\nВсего задач:",total)
print("Правильно решённых:",correct)
grade_test = correct/total
print("Процент выполнения",grade_test*100)
if grade_test<0.5:
    print("Оценка: 2")
elif grade_test>=0.5 and grade_test<0.7:
    print("Оценка: 3")
elif grade_test>=0.7 and grade_test<0.9:
    print("Оценка: 4")
elif grade_test>0.9:
    print("Оценка: 5")