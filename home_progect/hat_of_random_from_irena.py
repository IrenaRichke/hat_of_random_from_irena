from tkinter import *
import random

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

initial_list = tuple(people)

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

#output_data = {1111: "1111"}


def generate_new_list():
    random.shuffle(people)
    duty_dictionary = dict(zip(zones, people))
    row_counter = 1
    for cells in duty_dictionary:
        output_zones = Label(main_window, text=str(cells), font=("Century Gothic", 14), bg='white', fg='black')
        output_zones.grid(column=1, row=row_counter)
        output_people = Label(main_window, text="     "+duty_dictionary.get(cells, 0) + "     ", font=("Century Gothic", 14), bg='white', fg='black')
        output_people.grid(column=2, row=row_counter)
        row_counter += 1
    return duty_dictionary


'''def save_to_file():
    file_work = open('database.txt', 'w')
    file_work.write(str(output_data) + '\n')
    file_work.close()
'''


def clicked():
    generate_new_list()


'''def save_button_clicked():
    save_to_file()
'''

#инициализация интерфейса
main_window = Tk()
main_window.geometry('1200x800')
main_window.configure(bg='white')
main_window.title("HAT OF RANDOM by Korfitz SoftWare (2022)")

greeting = Label(main_window, text="   В Доме живут   ", font=("Century Gothic", 20), bg='white', fg='black')
greeting.grid(column=0, row=0)

people_counter = 0
row_counter = 1

for inhabitant in people:
    cell = Label(main_window, text=initial_list[people_counter], font=("Century Gothic", 14), bg='white', fg='black')
    cell.grid(column=0, row=row_counter)
    row_counter += 1
    people_counter += 1

generate_new_appointment_list = Button(main_window, text="создать новый список", font=("Century Gothic", 14), bg='white', fg='black', command=clicked)
generate_new_appointment_list.grid(column=1, row=0)
#save_current_appointment = Button(main_window, text="сохранить сгенерированный список", font=("OCR-A BT", 14), bg='white', fg='black', command=save_button_clicked)
#save_current_appointment.grid(column=1, row=17)

main_window.mainloop()
