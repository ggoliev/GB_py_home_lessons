# Задача-2:
# Напишите скрипт, отображающий папки текущей директории.

import os


for root, dirs, files in os.walk('.'):
    for dirname in dirs:
        print(dirname)

# найти решение с path?