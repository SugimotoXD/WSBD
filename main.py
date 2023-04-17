import tkinter
from tkinter import *
from tkinter import ttk
import tkinter as tk
import pyodbc

root = Tk()
root.title("Тест")
root.geometry("1000x500")
root.resizable(False,False)
root.rowconfigure(index=0, weight=1)
root.columnconfigure(index=0, weight=1)

con = pyodbc.connect('Driver={SQL Server};'
                     'Server=SAICHI-SAMA\SQLEXPRESS;'
                     'Database=Test;'
                     'Trusted_Connection=yes;')

columns = ("first_name", "second_name", "last_name", "phone_num", "email_add", "organisation")

tree = ttk.Treeview(columns= columns, show="headings", displaycolumns=(
"first_name", "second_name", "last_name", "phone_num", "email_add", "organisation"))
tree.grid(row=1, columns=1, sticky="nsew")

Cor = con.execute("SELECT * FROM Client")

tree.heading("first_name", text="#", anchor= W)
tree.heading("second_name", text="ФИО", anchor= W)
tree.heading("last_name", text="Контакты", anchor= W)
tree.heading("phone_num", text="Номер", anchor= W)
tree.heading("email_add", text="Мыло", anchor= W)
tree.heading("organisation", text="Организация", anchor= W)

tree.column("#0", stretch=NO, width=50)
tree.column("#1", stretch=NO, width=50)
tree.column("#2", stretch=NO, width=50)
tree.column("#3", stretch=NO, width=100)
tree.column("#4", stretch=NO, width=100)
tree.column("#5", stretch=NO, width=100)

for person in Cor:
    tree.insert("", "end", values=list(person))

class Test():
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry('500x400')
        label = tkinter.ttk.Label(self.root, text="Введите имя")
        label.pack(fill='y')
        edit_first = Entry(self.root, width=30, bg="grey")
        edit_first.pack(fill="y", pady=15)
        label = tkinter.ttk.Label(self.root, text="Введите Фамилию")
        label.pack(fill='y')
        edit_second = Entry(self.root, width=30, bg="grey")
        edit_second.pack(fill="y", pady=15)
        label = tkinter.ttk.Label(self.root, text="Введите номер телефона")
        label.pack(fill='y')
        edit_third = Entry(self.root, width=30, bg="grey")
        edit_third.pack(fill="y", pady=15)
        label = tkinter.ttk.Label(self.root, text="Введите регистрационный логин")
        label.pack(fill='y')
        edit_four = Entry(self.root, width=30, bg="grey")
        edit_four.pack(fill="y", pady=15)
        label = tkinter.ttk.Label(self.root, text="Введите регистрационный пароль")
        label.pack(fill='y')
        edit_five = Entry(self.root, width=30, bg="grey")
        edit_five.pack(fill="y", pady=15)
        button = tk.Button(self.root, text='Добавить записи в таблицу', )
        button.pack(fill='y', pady=15)
        self.root.mainloop()


app = Test


btn = ttk.Button(text="Личное посещение", command=app).place(x=500, y= 300)

scrollbar = ttk.Scrollbar(orient=VERTICAL, command=tree.yview)

scrollbar.grid(row=0, column=1)
root.mainloop()