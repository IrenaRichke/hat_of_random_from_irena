from tkinter import *
import random
import openpyxl

book = openpyxl.open("People_and_zones.xlsx", read_only=True) #Обращаемся к файлу

sheet_people = book.worksheets[0] #Обращаемся к 1 листу в файле
sheet_zones = book.worksheets[1] #Обращаемся к 2 листу в файле

#Создаем пустые скиски
people = []
zones = []

for row1 in range(2, sheet_people.max_row+1): #Берет столбцы от 1 до последнего
    people.append(sheet_people[row1][1].value) #Добавляем каждое значение(кроме заголовка) в список


for row2 in range(2, sheet_zones.max_row+1): #Берет столбцы от 1 до последнего
    zones.append(sheet_zones[row2][1].value) #Добавляем каждое значение(кроме заголовка) в список


#сохраняем изменяемый список в неизменяемый кортеж
initial_list = tuple(people)

#генерация нового списка дежурных
def generate_new_list():
    random.shuffle(people) #рандомизируем список
    duty_dictionary = dict(zip(zones, people)) #сшиваем список зон и рандомизированный список людей в словарь
    row_counter = 1
    for cells in duty_dictionary: #циклом выводим в 2 колонки список, соотнесённый со списком зон
        output_zones = Label(main_window, text=str(cells), font=("Century Gothic", 14), bg='white', fg='black')
        output_zones.grid(column=1, row=row_counter)
        output_people = Label(main_window, text="     "+duty_dictionary.get(cells, 0) + "     ", font=("Century Gothic", 14), bg='white', fg='black')
        output_people.grid(column=2, row=row_counter)
        row_counter += 1
    return duty_dictionary #функция возвращает словарь

def save_appointment_to_excel():
    book = openpyxl.open("People_and_zones.xlsx", read_only=False)
    sheet_archive = book.worksheets[2]  # Обращаемся к 2 листу в файле
    archive_counter = 0
    for i in range(0, len(zones)+1):
        sheet_archive[f'A{archive_counter}'] = zones[archive_counter]
        sheet_archive[f'B{archive_counter}'] = people[archive_counter]
        archive_counter += 1

#инициализация интерфейса
main_window = Tk()
main_window.geometry('1200x800')
main_window.configure(bg='white')
main_window.title("HAT OF RANDOM by Korfitz SoftWare (2022)")

#выводим список жильцов
greeting = Label(main_window, text="   В Доме живут   ", font=("Century Gothic", 20), bg='white', fg='black')
greeting.grid(column=0, row=0)
people_counter = 0
row_counter = 1
for inhabitant in people:
    cell = Label(main_window, text=initial_list[people_counter], font=("Century Gothic", 14), bg='white', fg='black')
    cell.grid(column=0, row=row_counter)
    row_counter += 1
    people_counter += 1

#создаём кнопку и вешаем на неё функцию клика
generate_new_appointment_list = Button(main_window, text="создать новый список", font=("Century Gothic", 14), bg='white', fg='black', command=generate_new_list)
generate_new_appointment_list.grid(column=1, row=0)

save_new_appointment_to_excel = Button(main_window, text='сохранить новый список в архив', bg='white', fg='black', command=save_appointment_to_excel )
save_new_appointment_to_excel.grid(column=3, row=0)

main_window.mainloop()
