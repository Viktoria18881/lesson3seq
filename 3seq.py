#6. (МОДУЛЬ 3) В проекте создать новый модуль 3seq.py. Задание:
#Пользователь вводит элементы 1-го списка (по очереди как в МОДУЛЬ 1 или вместе как в МОДУЛЬ 2)
#Затем он вводит элементы 2-го списка
#Удалить из первого списка элементы присутствующие во 2-ом и вывести результат на экран
#Пример работы: Введите элементы 1-го списка: 1,2,3,4,5
#Введите элементы 2-го списка: 2,5
#Результат: 1,3,4
#Предлагаю проверить работу программы на разных списках, чтобы убедиться что она работает верно

list_1 = input('Введите первый список цифр через запятую:').split(',')
numerical_list_1 = [int(elem) for elem in list_1]

list_2 = input('Введите второй список цифр через запятую:').split(',')
numerical_list_2 = [int(elem) for elem in list_2]

for num in numerical_list_1[::-1]:
    if num in list_2:
        numerical_list_2.remove(num)

print(f'Результат: {numerical_list_1}')