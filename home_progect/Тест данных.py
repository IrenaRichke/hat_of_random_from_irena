import openpyxl

book = openpyxl.open("People_and_zones.xlsx") #Обращаемся к файлу

sheet1 = book.worksheets[0] #Обращаемся к 1 листу в файле
sheet2 = book.worksheets[1] #Обращаемся к 2 листу в файле

print(sheet1["B6"].value) #Вынимаем значение из конкретной ячейки
print(sheet1[6][1].value) #Вынимаем значение из конкретной ячейки. первая [] ряд, вторая [] колонка

# Колонки считаются от 0. Строки от 1

diapazone = sheet1['A1':'B5'] #Обращаемся к диапазону
for number, people in diapazone:
    print(number.value, people.value) #Выводит все значения в соответствии со столбцом

for row1 in range(1, sheet1.max_row+1): #Берет столбцы от 1 до последнего
    people = sheet1[row1][1].value #первая [] это ряд, вторая [] это колонка.
    print(people) #Выводится как строка

for row2 in range(1, sheet2.max_row+1): #Берет столбцы от 1 до последнего
    zones = sheet2[row2][1].value #первая [] это ряд, вторая [] это колонка.
    print(zones) #Выводится как строка
