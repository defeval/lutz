l = [123, 'spam', 1.23]

print(l)

l = l[:1]  # срез

print(l)

l = [123, 'spam', 1.23]  # удаление элеманта списка и его функция вернет его
print(l.pop(2))
print(l)

l.append([456, 789])  # добавляет в конец списка элемент
print(l)
print(l[2])

l = [123, 0, 1.23]
l.sort()  # сортирует по возрастанию, reverse() по убыванию
print(l)