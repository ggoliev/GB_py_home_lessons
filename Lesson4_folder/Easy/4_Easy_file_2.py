# Задание-2:
# Даны два списка фруктов.
# Получить список фруктов, присутствующих в обоих исходных списках.

# Я тут немного заблудился в трёх соснах
# если значения в списке НЕ повторяются:
list1 = ['grape', 'lemon', 'pineapple', 'pear']
list2 = ['pear', 'plum', 'lemon', 'peach']

in_both1 = [e for e in list1 if e in list2]

print(in_both1)

# если значения в списке повторяются:
list3 = ['grape', 'lemon', 'pineapple', 'pear', 'lemon']
list4 = ['pear', 'plum', 'lemon', 'peach', 'pear']
in_both2 = []


# in_both2 = set(list3).intersection(list4) - не работает, выдаёт только 'lemon', 'pear'

for item_a in list3:
    for item_b in list4:
        if item_a == item_b:
            in_both2.append(item_a)
# Это работает, но это не генератор списка

print(in_both2)
# returnMatches - what's this?
