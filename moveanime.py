from tkinter import BOTTOM, END, LEFT, RIGHT, TOP, Y, Button, Entry, Label, Scrollbar, ttk
import tkinter as tk
import random
from xml.dom.minidom import Entity
import os
# Файлы списка


with open('anime.txt', encoding='utf-8') as file:
    spisok_anime = file.readlines()

with open('film.txt', encoding='utf-8') as file_1:
    spisok_film = file_1.readlines()

with open('serial.txt', encoding='utf-8') as file_2:
    spisok_serial = file_2.readlines()

root = tk.Tk()

# Окно
root.title("Что посмотреть")
root.geometry("1000x768+440+140")
root.resizable(False, False)
root.iconbitmap('frico.ico')

bg = tk.PhotoImage(
    file="PcsvHLoqBSU.png")
my_lab = tk.Label(root, image=bg)
my_lab.place(x=0, y=0, relwidth=1, relheight=1)

# Функции программы

move = ["Аниме", "Фильмы", "Сериалы"]


def list_anime():
    global spisok_anime
    root = tk.Tk()
    root.title("Аниме")
    root.geometry("600x550+350+250")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')
    but_tx = tk.Text(root,
                     font=("Comic Sans MS", 15))
    for i in range(len(spisok_anime)):
        but_tx.insert(END, f"{spisok_anime[i]} \n")
    but_tx.grid()

    root.mainloop()


def list_film():
    global spisok_film
    root = tk.Tk()
    root.title("Фильмы")
    root.geometry("600x550+350+250")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')
    but_tx_1 = tk.Text(root,
                       font=("Comic Sans MS", 15))
    for i in range(len(spisok_film)):
        but_tx_1.insert(END, f"{spisok_film[i]} \n")
    but_tx_1.grid()

    root.mainloop()


def list_serial():
    global spisok_serial
    root = tk.Tk()
    root.title("Сериалы")
    root.geometry("600x550+350+250")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')
    but_tx_2 = tk.Text(root,
                       font=("Comic Sans MS", 15))
    for i in range(len(spisok_serial)):
        but_tx_2.insert(END, f"{spisok_serial[i]} \n")
    but_tx_2.grid()

    root.mainloop()


def list_random():
    global but_combo
    but_4 = tk.Entry(root,
                     font=("Comic Sans MS", 20))
    but_4.grid(row=1, column=2, columnspan=1, sticky="wens", padx=20, pady=65)
    if but_combo.get() == 'Аниме':
        but_4.insert(0, random.choice(spisok_anime))
    elif but_combo.get() == 'Фильмы':
        but_4.insert(0, random.choice(spisok_film))
    elif but_combo.get() == 'Сериалы':
        but_4.insert(0, random.choice(spisok_serial))

def app_list_select_anime():
    f = open('anime.txt', 'a', encoding='utf-8')
    root = tk.Tk()
    root.title("Добавить аниме")
    root.geometry("320x90+700+500")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')
    but_5 = Entry(root,
                  font=("Comic Sans MS", 20),
                  bg="#88ff4d")
    but_5.grid(row=0, column=0, sticky="wens")

    but_6 = tk.Button(root,
                      font=("Comic Sans MS", 15),
                      text="Добавить",
                     command=lambda: f.write(f"{but_5.get()} \n"))
    but_6.grid(row=1, column=0, sticky="wens")

def app_list_select_film():
    f_1 = open('film.txt', 'a', encoding='utf-8')
    root = tk.Tk()
    root.title("Добавить фильм")
    root.geometry("320x90+700+500")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')
    but_5 = Entry(root,
                  font=("Comic Sans MS", 20),
                  bg="#88ff4d")
    but_5.grid(row=0, column=0, sticky="wens")

    but_6 = tk.Button(root,
                      font=("Comic Sans MS", 15),
                      text="Добавить",
                     command=lambda: f_1.write(f"{but_5.get()} \n"))
    but_6.grid(row=1, column=0, sticky="wens")

def app_list_select_serial():
    f_2 = open('serial.txt', 'a', encoding='utf-8')
    root = tk.Tk()
    root.title("Добавить сериал")
    root.geometry("320x90+700+500")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')
    but_5 = Entry(root,
                  font=("Comic Sans MS", 20),
                  bg="#88ff4d")
    but_5.grid(row=0, column=0, sticky="wens")

    but_6 = tk.Button(root,
                      font=("Comic Sans MS", 15),
                      text="Добавить",
                     command=lambda: f_2.write(f"{but_5.get()} \n"))
    but_6.grid(row=1, column=0, sticky="wens")

def delet_list():
    f = open('anime.txt', 'a', encoding='utf-8')
    f_1 = open('film.txt', 'a', encoding='utf-8')
    f_2 = open('serial.txt', 'a', encoding='utf-8')
    root = tk.Tk()
    root.title("Убрать из просмотра")
    root.geometry("320x90+700+500")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')
    but_5 = Entry(root,
                  font=("Comic Sans MS", 20),
                  bg="#88ff4d")
    but_5.grid(row=0, column=0, sticky="wens")
    def delet_ent():
        for i in range(len(spisok_anime)):
            if but_5.get() in spisok_anime[i]:
                spisok_anime.remove(spisok_anime[i])
                f = open('anime.txt', 'w+', encoding='utf-8')
                for i in spisok_anime:
                    new_spisok_anime = f.write(i)
                f.close()
                break
            break
        for i in range(len(spisok_film)):
            if but_5.get() in spisok_film[i]:
                spisok_film.remove(spisok_film[i])
                f_1 = open('film.txt', 'w+', encoding='utf-8')
                for i in spisok_film:
                    new_spisok_film = f_1.write(i)
                f_1.close()
                break
            break
        for i in range(len(spisok_serial)):
            if but_5.get() in spisok_serial[i]:
                spisok_serial.remove(spisok_serial[i])
                f_2 = open('serial.txt', 'w+', encoding='utf-8')
                for i in spisok_serial:
                    new_spisok_serial = f_2.write(i)
                f_2.close()
                break
            break
    but_6 = tk.Button(root,
                      font=("Comic Sans MS", 15),
                      text="Убрать",
                     command=delet_ent)
    but_6.grid(row=1, column=0, sticky="wens")
def app_list():
    root = tk.Tk()
    root.title("Добавить")
    root.geometry("880x140+400+500")
    root.resizable(False, False)
    root.iconbitmap('frico.ico')

    but_app_1 = tk.Button(root,text="Аниме",
                  width=8,
                  height=0,
                  font=("Comic Sans MS", 30),
                  bg="#40e66a",
                  command=app_list_select_anime)
    but_app_2 = tk.Button(root,text="Фильмы",
                  width=8,
                  height=0,
                  font=("Comic Sans MS", 30),
                  bg="#40e66a",
                  command=app_list_select_film)
    but_app_3 = tk.Button(root,text="Сериалы",
                  width=8,
                  height=0,
                  font=("Comic Sans MS", 30),
                  bg="#40e66a",
                  command=app_list_select_serial)
    but_app_4 = tk.Button(root,text="Просмотрено",
                    width=11,
                    height=0,
                    font=("Comic Sans MS", 30),
                    bg="#91ffe7",
                    command=delet_list)
    but_app_1.grid(row=0,column=0)
    but_app_2.grid(row=0,column=1)
    but_app_3.grid(row=0,column=2)
    but_app_4.grid(row=0,column=3)


# Надписи


lab_1 = tk.Label(root,
                 text=f"Сейчас у тебя {len(spisok_anime)} аниме",
                 font=("Comic Sans MS", 20),
                 bg="#ffed91")

lab_2 = tk.Label(root,
                 text=f"Сейчас у тебя {len(spisok_film)} фильмов",
                 font=("Comic Sans MS", 20),
                 bg="#ffed91")

lab_3 = tk.Label(root,
                 text=f"Сейчас у тебя {len(spisok_serial)} сериалов",
                 font=("Comic Sans MS", 20),
                 bg="#ffed91")

# Кнопки

but_1 = tk.Button(root, text="Аниме",
                  width=10,
                  height=0,
                  font=("Comic Sans MS", 40),
                  bg="#40e66a",
                  command=list_anime)

but_6 = tk.Button(root, text="Фильмы",
                  width=10,
                  height=0,
                  font=("Comic Sans MS", 40),
                  bg="#40e66a",
                  command=list_film)

but_7 = tk.Button(root, text="Сериалы",
                  width=10,
                  height=0,
                  font=("Comic Sans MS", 40),
                  bg="#40e66a",
                  command=list_serial)

but_2 = tk.Button(root, text="Добавить",
                  width=10,
                  height=0,
                  font=("Comic Sans MS", 40),
                  bg="#42e3a2",
                  command=app_list)

but_combo = ttk.Combobox(root,
                         width=10,
                         height=0,
                         font=("Comic Sans MS", 30),
                         values=move)
but_combo.current(0)

but_3 = tk.Button(root, text="Выбрать",
                  width=10,
                  height=0,
                  font=("Comic Sans MS", 20),
                  bg="#42e3a2",
                  command=list_random)

but_4 = tk.Entry(root,
                 font=("Comic Sans MS", 20))

# Расположение на окне

but_1.grid(row=0, column=0)
but_combo.grid(row=1, column=0, columnspan=1, sticky="we")
but_2.grid(row=2, column=0, columnspan=1, sticky="we")
but_3.grid(row=1, column=1, columnspan=1, sticky="wens", padx=50, pady=80)
but_4.grid(row=1, column=2, columnspan=1, sticky="wens", padx=20, pady=65)
lab_1.grid(row=3, column=0, columnspan=1, sticky="we")
lab_2.grid(row=4, column=0)
lab_3.grid(row=5, column=0)
but_6.grid(row=0, column=1, columnspan=1, sticky="we")
but_7.grid(row=0, column=2, columnspan=1, sticky="we")

# Сортировка кнопок
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(0, minsize=60)
root.grid_columnconfigure(0, minsize=20)
root.grid_columnconfigure(1, minsize=50)

root.grid_rowconfigure(0, minsize=60)
root.grid_rowconfigure(1, minsize=100)
root.grid_rowconfigure(2, minsize=10)
root.grid_rowconfigure(3, minsize=70)
root.grid_rowconfigure(4, minsize=70)
root.grid_rowconfigure(5, minsize=70)

root.mainloop()
