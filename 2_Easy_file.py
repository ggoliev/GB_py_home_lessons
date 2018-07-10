# Задача-1:
# Дан список фруктов. Напишите программу, выводящую фрукты в виде нумерованного списка, выровненного по правой стороне.
# Пример:
# Дано: ["яблоко", "банан", "киви", "арбуз"]
# Вывод:
# 1. яблоко
# 2.  банан
# 3.   киви
# 4.  арбуз
# Подсказка: воспользоваться методом .format()
# Методичка к уроку - https://uploads.hb.cldmail.ru/asset/910568/attachment/f4bcb02be0685578209e0c6e9d04df10.pdf
# https://pythonworld.ru/osnovy/formatirovanie-strok-metod-format.html

fruits_list = ['яблоко', 'банан', 'киви', 'арбуз']  # Дан список фруктов

for fruit in fruits_list:
    print(fruits_list.index(fruit)+1, '{:>10}' .format(fruit))

# OR
# Что лучше?

i = 1
for fruit in fruits_list:
    print(i, '{:>10}' .format(fruit))
    i += 1