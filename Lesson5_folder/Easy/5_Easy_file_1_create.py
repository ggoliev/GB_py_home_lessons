# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os


i = 1
while i < 10:
    dir_name = 'dir_'+str(i)
    os.mkdir(dir_name)
    i += 1

# проверка на предварительное наличие папок не предусмотрена условием задачи