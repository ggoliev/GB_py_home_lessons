# Эти задачи необходимо решить используя регулярные выражения!

# Задача - 1
# Запросите у пользователя имя, фамилию, email.
# Теперь необходимо совершить проверки, имя и фамилия должны иметь заглавные первые буквы. email - не должен иметь заглавных букв и должен быть в формате: текст в нижнем регистре,
# допускается нижнее подчеркивание и цифры, потом @, потом текст, допускаются цифры, точка, ru или org или com.
# Например:
# Пупкин василий - неверно указано имя, te$T@test.net - неверно указан email (спецсимвол, заглавная буква, .net), te_4_st@test.com - верно указан.

import re

pattern_capital = '^[A-Z][a-z]*$'  #Звёздочка (а не плюс)- на случай какой-нибудь китайской фамилии типа "У"
pattern_email = '^[-a-z0-9_]*@([a-z0-9]([-a-z0-9]{0,61}[a-z0-9])?\.)*(ru|org|com)$'  #Неполное - допускает _@fufu.com

name = input('Enter your name. The first letter must me capital: ')
while not re.findall(pattern_capital, name):
    name = input('The first letter must me capital. Enter your name: ')

surname = input('Enter your surname. The first letter must me capital:')
while not re.findall(pattern_capital, surname):
    surname = input('The first letter must me capital. Enter your surname: ')

email = input ('Enter email:')
while not re.findall(pattern_email, email):
    surname = input('Enter the email in the right format: ')




