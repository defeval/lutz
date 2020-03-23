# операции со строками

s = 'spam'
print(len(s))  # string length
print(s[0])    # первый элемент
print(s[1])    # последний эемент
print(s[1:3])  # срез со второго по третий не включительно
print(s[1:])   # срез всего кроме первого
print(s[:3])   # то же что и [0:3]

print(s[0:-1] == s[0:3])

print(s.find('a'))  # Вернет смещение (т.е. сколько символов до нужной строки или -1 если ничего не найдено

s1 = 'souse'.replace('s', '$', 2)  # вернет $ou$e
print(s1)

line = 'aaa,bbb,ССС,dd'

print(line.split(','))  # вернет список

print(line.upper())  # вернет верхний регистр
print(line.lower())  # вернет нижний регистр

# узнать что делает метод
print(help(s.join))

print('.'.join(['ab', 'pq', 'rs']))  # 'ab.pq.rs'




