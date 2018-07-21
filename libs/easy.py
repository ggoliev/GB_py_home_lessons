import os


def current_dir():
    print('Текущая директория - ', os.getcwd())
    print('Список доступных директорий:')
    print(next(os.walk('.'))[1])
    # for root, dirs, files in os.walk('.'): - # неверно. выдает вложенные папки в том же списке
    #     for dirname in dirs:
    #         print(dirname)


def change_dir():
    current_dir()
    target_folder = input('Введите название папки для перехода: ')
    path = os.getcwd() + '\\' + target_folder
    try:
        os.chdir(path)
        print('Перешли в папку - ', os.getcwd())
    except FileNotFoundError:
        print('Невозможно перейти. Указанная папка не существует.')


def delete_dir():
    current_dir()
    target_folder = input('Введите название удаляемой папки: ')
    path = os.getcwd() + '\\' + target_folder
    try:
        os.rmdir(path)
        print('Папка удалена - ', path)
    except FileNotFoundError:
        print('Невозможно удалить. Указанная папка не существует')
    except PermissionError:
        print('Папка не пустая и не может быть удалена')


def create_dir():
    current_dir()
    target_folder = input('Введите название создаваемой  папки: ')
    path = os.getcwd() + '\\' + target_folder
    try:
        os.mkdir(path)
        print('Папка добавлена - ', path)
    except FileExistsError:
        print('Невозможно создать. Указанная папка уже существует')