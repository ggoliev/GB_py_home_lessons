# Создайте программу медицинская анкета, где вы запросите у пользователя такие данные, как имя, фамилию, возраст, и вес.
# И выведите результат согласно которому пациент в хорошем состоянии, если ему до 30 лет и вес от 50 и до 120 кг,
# Пациенту требуется начать вести правильный образ жизни, если ему более 30 и вес меньше 50 или больше 120 кг
# Пациенту требуется врачебный осмотр, если ему более 40 и вес менее 50 или больше 120 кг.
# Все остальные варианты вы можете обработать на ваш вкус и полет фантазии =)
# Формула не отражает реальной действительности и здесь используется только ради примера.

# Пример: Вася Пупкин, 29 год, вес 90 - хорошее состояние
# Пример: Вася Пупкин, 31 год, вес 121 - следует заняться собой
# Пример: Вася Пупкин, 31 год, вес 49 - следует заняться собой
# Пример: Вася Пупкин, 41 год, вес 121 - следует обратится к врачу!
# Пример: Вася Пупкин, 41 год, вес 49 - следует обратится к врачу!

name = input('Имя: ')
family_name = input('Фамилия: ')
age = int(input('Возраст: '))
weight =int(input('Вес: '))
full_data = (name + ' ' + family_name + ', ' + str(age) + ' год, вес ' + str(weight))

reaction1 = (full_data + ' - Реакция 1')
reaction2 = (full_data + ' - следует заняться собой.')
reaction3 = (full_data + ' - следует обратится к врачу!')
reaction4 = (full_data + ' - хорошее состояние.')
reaction5 = (full_data + ' - Реакция 5')
reaction6 = (full_data + ' - Реакция 6')
reaction7 = (full_data + ' - Реакция 7')
#reaction8 = (full_data + ' - Реакция 8'
#reaction9 = (full_data + ' - Реакция 9'

if age < 30:
    if weight<50:
        print(reaction1)
    elif 50<=weight<=120:
        print(reaction4)
    else:
        print(reaction7)
elif 30 <= age <= 40:
    if weight < 50 or weight > 120:
        print(reaction2)
    else:
        print(reaction5)
else:
    if weight < 50 or weight > 120:
        print(reaction3)
    else:
        print(reaction6)
