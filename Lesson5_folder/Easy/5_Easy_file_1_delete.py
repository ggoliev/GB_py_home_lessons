# Задача-1:
# Напишите скрипт, создающий директории dir_1 - dir_9 в папке, из которой запущен данный скрипт.
# И второй скрипт, удаляющий эти папки.

import os
import re
import shutil


pattern = 'dir_[1-9]$'


for i in os.listdir(path='.'): # Можно оставить такую строку или лучше сделать проще(?) - через переменную my_list_dir = os.listdir(path='.')
    if re.findall(pattern, i):
        shutil.rmtree(i)

# i = 1
# while i < 10:
#     dir_name = 'dir_'+str(i)
#     os.rmdir(dir_name)
#     i += 1
# не будет работать, если одна из папок 1-9 отсутствует - была удалена вручную, например.
# не будет работать, если папки не пустые
