from tkinter import *
import random

#список жильцов
people = ['Степан',
          'Крис',
          'Катя',
          'Андрей',
          'Наргиза',
          'Юра',
          'Даша',
          'Толис',
          'Олег',
          'Маша',
          'Дима',
          'Ирэна',
          'Аня',
          'Лина',
          'Аня2',
          'Артём',
          'Валя',
          'Ваня',
          'Толик',
          'Влада',
          'Вова',
          'Ада',
          'Лена',
          'Лиза',
          'Шамиль',
          'Саша']

#сохраняем изменяемый список в неизменяемый кортеж
initial_list = tuple(people)

#список зон ответственности
zones = ['розовый туалет',
         'голубой туалет',
         'розовый душ',
         'голубой душ',
         'предбанники туалетов и раковины',
         'кухня1',
         'кухня2',
         'гостиная1',
         'гостиная2',
         'холодильник1',
         'холодильник2',
         'коридор1',
         'коридор2',
         'прихожая',
         'зал',
         'фримаркет']

#генерация нового списка дежурных
def generate_new_list():
#рандомизируем список
    random.shuffle(people)
#сшиваем список зон и рандомизированный список людей в словарь
    duty_dictionary = dict(zip(zones, people))
    row_counter = 1
#циклом выводим в 2 колонки список, соотнесённый со списком зон
    for cells in duty_dictionary:
        output_zones = Label(main_window, text=str(cells), font=("Century Gothic", 14), bg='white', fg='black')
        output_zones.grid(column=1, row=row_counter)
        output_people = Label(main_window, text="     "+duty_dictionary.get(cells, 0) + "     ", font=("Century Gothic", 14), bg='white', fg='black')
        output_people.grid(column=2, row=row_counter)
        row_counter += 1
#функция возвращает словарь
    return duty_dictionary

#функция нажатия кнопки
def clicked():
#эта дичь уже вызывает основную функцию
    generate_new_list()


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
generate_new_appointment_list = Button(main_window, text="создать новый список", font=("Century Gothic", 14), bg='white', fg='black', command=clicked)
generate_new_appointment_list.grid(column=1, row=0)

main_window.mainloop()
