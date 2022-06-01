from tkinter import *
from tkinter import ttk
import login_window
import register_window
import mysql.connector as mysql


def everything():
    color = "#29fbc1"

    def log_out():
        account_window.destroy()
        login_window.everything()

    def change_password():
        pass

    def change_data():
        pass

    account_window = Tk()
    window_width = 900
    window_height = 600
    screen_width = account_window.winfo_screenwidth()
    screen_height = account_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    account_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    account_window.title("KOREPETIX/PANEL ADMINISTRATORA")
    account_window.config(background=color)
    account_window.resizable(FALSE, FALSE)

    notebook = ttk.Notebook(account_window)  # widget that manages a collection of windows/displays
    tab1 = Frame(notebook, bg=color)  # new frame for tab 1
    tab2 = Frame(notebook, bg=color)  # new frame for tab 2
    tab3 = Frame(notebook, bg=color)  # new frame for tab 3
    tab4 = Frame(notebook, bg=color)  # new frame for tab 3

    notebook.add(tab1, text='Raporty')
    notebook.add(tab2, text='Ogłoszenia')
    notebook.add(tab3, text='Użytkownicy')
    notebook.add(tab4, text='Ustawienia konta')
    notebook.pack(expand=True, fill='both')
    # expand = expand to fill any space not otherwise used
    # fill = fill space on x and y axis

    frame1 = Frame(tab1) # raporty
    frame1.pack()

    frame2 = Frame(tab2) # moderowanie ogłoszeń
    frame2.pack()

    frame3 = Frame(tab3) # operacje na użytkownikach
    frame3.pack()

    frame4 = Frame(tab4) # ustawienia konta administratora
    frame4.pack()
    Label(frame4, text="", bg=color).grid(row=0, column=0, sticky="nsew")
    Button(frame4, text="Zmień dane", command=change_data).grid(row=5, column=0)
    Label(frame4, text="", bg=color).grid(row=10, column=0, sticky="nsew")
    Button(frame4, text="Zmień Hasło", command=change_password).grid(row=15, column=0)
    Label(frame4, text="", bg=color).grid(row=20, column=0, sticky="nsew")
    Button(frame4, text="Wyloguj się", command=log_out).grid(row=25, column=0)

    account_window.mainloop()
