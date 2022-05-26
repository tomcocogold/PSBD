from tkinter import *
from tkinter import ttk
import login_window
import register_window
import mysql.connector as sql


def everything():

    account_window = Tk()
    window_width = 900
    window_height = 600
    screen_width = account_window.winfo_screenwidth()
    screen_height = account_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    account_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    account_window.title("KOREPETIX/PANEL UŻYTKOWNIKA")
    account_window.config(background="#29fbc1")
    account_window.resizable(FALSE, FALSE)

    notebook = ttk.Notebook(account_window)  # widget that manages a collection of windows/displays
    tab1 = Frame(notebook, bg="#29fbc1")  # new frame for tab 1
    tab2 = Frame(notebook, bg="#29fbc1")  # new frame for tab 2
    tab3 = Frame(notebook, bg="#29fbc1")  # new frame for tab 3

    notebook.add(tab1, text='Dane użytkownika')
    notebook.add(tab2, text='Ogłoszenia')
    notebook.add(tab3, text='Ustawienia konta')
    notebook.pack(expand=True, fill='both')
    # expand = expand to fill any space not otherwise used
    # fill = fill space on x and y axis

    frame1 = Frame(tab1)
    frame1.pack()
    

    frame2 = Frame(tab2)
    frame2.pack()


    account_window.mainloop()
