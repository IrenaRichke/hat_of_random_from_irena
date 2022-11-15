from tkinter import *
from tkinter.ttk import Combobox 
import random
import openpyxl

book = openpyxl.open("People_and_zones.xlsx", read_only=False) #Обращаемся к файлу

sheet_people = book.worksheets[0] #Обращаемся к 1 листу в файле
sheet_zones = book.worksheets[1] #Обращаемся к 2 листу в файле

#Создаем пустые списки
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
        output_zones = Label(main_window, text=str(cells), font=("Arial", 12), bg='white', fg='black')
        output_zones.grid(column=1, row=row_counter)
        output_people = Label(main_window, text="     "+duty_dictionary.get(cells, 0) + "     ", font=("Arial", 12), bg='white', fg='black')
        output_people.grid(column=2, row=row_counter)
        row_counter += 1
    ask_for_periods = Label(main_window, text="выберите период дежурства", font=("Arial", 12), bg='white', fg='black')
    ask_for_periods.grid(column=3, row=0)


    save_new_appointment_to_excel = Button(main_window, text='сохранить новый список в архив', bg='white', fg='black', command=save_appointment_to_excel )
    save_new_appointment_to_excel.grid(column=5, row=0)
    return duty_dictionary #функция возвращает словарь


def selected(event):
    selection = selector.get()
    selection_monitor = Label(main_window, text=f"    вы выбрали: {selection}    " , font=("Arial", 14), bg='white', fg='red')
    selection_monitor.grid(column=3, row=1)


def save_appointment_to_excel():
    book = openpyxl.open("People_and_zones.xlsx", read_only=False)
    sheet_archive = book.worksheets[2]  # Обращаемся к 3 листу в файле
    selection_archive = selector.get() #вынимаем из селектора период
    archive_counter = 1 #Счетчик для строк
    shift_for_period = 20 #Сдвиг для каждого периода вниз по таблице
    period_counter = int(selector.current()) #вынимает из селектора индекс выбранного в комбобоксе значения
    for i in range(1, len(zones)+1):
        if period_counter == 0: #для первого периода индекс 0, поэтому дендрофекалим через +1
            sheet_archive[f'A{archive_counter * (period_counter + 1)}'] = zones[i-1]
            sheet_archive[f'B{archive_counter * (period_counter+ 1)}'] = people[i-1]
            sheet_archive[f'A{period_counter + 17}'] = selection_archive #Запихиваем в последнюю строку списка название периода
        else: #Для остальных периодов
            sheet_archive[f'A{archive_counter + period_counter * shift_for_period}'] = zones[i - 1]
            sheet_archive[f'B{archive_counter + period_counter * shift_for_period}'] = people[i - 1]
            sheet_archive[f'A{period_counter * shift_for_period + 17}'] = selection_archive #Запихиваем в последнюю строку списка название периода
        archive_counter += 1
    book.save('People_and_zones.xlsx')


#инициализация интерфейса
main_window = Tk()
main_window.geometry('1200x800')
main_window.configure(bg='white')
main_window.title("HAT OF RANDOM by Korfitz SoftWare (2022)")

#выводим список жильцов
greeting = Label(main_window, text="   В Доме живут   ", font=("Arial", 16), bg='white', fg='black')
greeting.grid(column=0, row=0)
people_counter = 0
row_counter = 1
for inhabitant in people:
    cell = Label(main_window, text=initial_list[people_counter], font=("Arial", 12), bg='white', fg='black')
    cell.grid(column=0, row=row_counter)
    row_counter += 1
    people_counter += 1

#создаём кнопку и вешаем на неё функцию клика
generate_new_appointment_list = Button(main_window, text="создать новый список", font=("Arial", 12), bg='white', fg='black', command=generate_new_list)
generate_new_appointment_list.grid(column=1, row=0)

selector = Combobox(main_window)
selector['values'] = ('1 - 15 января', '16 - 31 января',
                     '1 - 15 февраля', '16 - 28/29 февраля',
                     '1 - 15 марта', '16 - 31 марта',
                     '1 - 15 апреля', '16 - 30 апреля',
                     '1 - 15 мая', '16 - 31 мая',
                     '1 - 15 июня', '16 - 30 июня',
                     '1 - 15 июля', '16 - 31 июля',
                     '1 - 15 августа', '16 - 31 августа',
                     '1 - 15 сентября', '16 - 30 сентября',
                     '1 - 15 октября', '16 - 31 октября',
                     '1 - 15 ноября', '16 - 30 ноября',
                     '1 - 15 декабря', '16 - 31 декабря')
selector.current(0)  #вариант по умолчанию
selector.grid(column=4, row=0)
selector.bind("<<ComboboxSelected>>", selected)

main_window.mainloop()
