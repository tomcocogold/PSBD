from tkinter import *
from tkinter import ttk
import login_window
import search_engine
import register_window
import mysql.connector as sql


def everything():

    def log_out():
        account_window.destroy()
        login_window.everything()

    def change_password():
        pass

    def change_data():
        pass

    def add_advert():
        pass

    def search_advert():
        account_window.destroy()
        search_engine.everything()

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
    tab4 = Frame(notebook, bg="#29fbc1")

    notebook.add(tab1, text='Dane użytkownika')
    notebook.add(tab2, text='Moje ogłoszenia')
    notebook.add(tab3, text='Moje zajęcia')
    notebook.add(tab4, text='Ustawienia konta')
    notebook.pack(expand=True, fill='both')
    # expand = expand to fill any space not otherwise used
    # fill = fill space on x and y-axis

    frame1 = Frame(tab1) # dane użytkownika
    frame1.pack()
    # register
    Label(frame1, text="Dane użytkownika", font=("Arial", 20), bg="#29fbc1", pady=30).grid(row=0, column=0, sticky="nsew")

    # Name
    Label(frame1, text="Imię", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=5, column=0, sticky="nsew")

    Label(frame1, text="Imię", font=("Arial", 14), fg="black", bg="white").grid(row=10, column=0, sticky="nsew")

    # Surname
    Label(frame1, text="Nazwisko", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=15, column=0, sticky="nsew")

    Label(frame1, text="Nazwisko", font=("Arial", 14), fg="black", bg="white").grid(row=20, column=0, sticky="nsew")

    # email
    Label(frame1, text="Email", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=25, column=0, sticky="nsew")

    Label(frame1, text="Email", font=("Arial", 14), fg="black", bg="white").grid(row=30, column=0, sticky="nsew")

    Label(frame1, text="Rodzaj konta", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=35, column=0, sticky="nsew")

    Label(frame1, text="Uczeń", font=("Arial", 14), fg="black", bg="white").grid(row=40, column=0, sticky="nsew")

    frame2 = Frame(tab2) # moje ogłoszenia
    frame2.pack()
    Label(frame2, text="", bg="#29fbc1").grid(row=0, columnspan=3, sticky="nsew")
    Button(frame2, text="Dodaj ogłoszenie", command=add_advert).grid(row=5, column=0)
    Label(frame2, text="                  ", bg="#29fbc1").grid(row=5, column=1, sticky="nsew")
    Button(frame2, text="Szukaj ogłoszeń", command=search_advert).grid(row=5, column=2)
    Label(frame2, text="Moje ogłoszenia", font=("Arial", 14), bg="#29fbc1").grid(row=10, columnspan=3, sticky="nsew")

    frame3 = Frame(tab3) # moje zajęcia
    frame3.pack()
    Label(frame3, text="Odbyte", font=("Arial", 14), bg="#29fbc1").grid(row=0, column=0, sticky="nsew")
    Label(frame3, text="                                                                             ",
          bg="#29fbc1").grid(row=0, column=1, sticky="nsew")
    Label(frame3, text="Nadchodzące", font=("Arial", 14), bg="#29fbc1").grid(row=0, column=2, sticky="nsew")

    frame4 = Frame(tab4) # ustawienia konta
    frame4.pack()
    Label(frame4, text="", bg="#29fbc1").grid(row=0, column=0, sticky="nsew")
    Button(frame4, text="Zmień dane", command=change_data).grid(row=5, column=0)
    Label(frame4, text="", bg="#29fbc1").grid(row=10, column=0, sticky="nsew")
    Button(frame4, text="Zmień Hasło", command=change_password).grid(row=15, column=0)
    Label(frame4, text="", bg="#29fbc1").grid(row=20, column=0, sticky="nsew")
    Button(frame4, text="Wyloguj się", command=log_out).grid(row=25, column=0)

    account_window.mainloop()
