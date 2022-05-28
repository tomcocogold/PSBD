from tkinter import *
import register_window
import account_window
import mysql.connector as sql


def everything():
    color = "#29fbc1"

    def login():
        login_window.destroy()
        account_window.everything()

    def register():
        login_window.destroy()
        register_window.everything()

    advert_window = Tk()

    window_width = 900
    window_height = 600
    screen_width = advert_window.winfo_screenwidth()
    screen_height = advert_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    advert_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

    advert_window.title("KOREPETIX/OGŁOSZENIE")
    advert_window.config(background=color)
    advert_window.resizable(FALSE, FALSE)

    frame1 = Frame(advert_window)  # dane użytkownika
    frame1.pack()
    # register
    Label(frame1, text="Dane użytkownika", font=("Arial", 20), bg=color, pady=30).grid(row=0, column=0, sticky="nsew")

    # Name
    Label(frame1, text="Imię", font=('Arial', 10), bg=color, pady=5).grid(row=5, column=0, sticky="nsew")
    Label(frame1, text="Imię", font=("Arial", 14), fg="black", bg="white").grid(row=10, column=0, sticky="nsew")

    # Surname
    Label(frame1, text="Nazwisko", font=('Arial', 10), bg=color, pady=5).grid(row=15, column=0, sticky="nsew")
    Label(frame1, text="Nazwisko", font=("Arial", 14), fg="black", bg="white").grid(row=20, column=0, sticky="nsew")

    # email
    Label(frame1, text="Email", font=('Arial', 10), bg=color, pady=5).grid(row=25, column=0, sticky="nsew")
    Label(frame1, text="Email", font=("Arial", 14), fg="black", bg="white").grid(row=30, column=0, sticky="nsew")
    Label(frame1, text="Rodzaj konta", font=('Arial', 10), bg=color, pady=5).grid(row=35, column=0, sticky="nsew")
    Label(frame1, text="Uczeń", font=("Arial", 14), fg="black", bg="white").grid(row=40, column=0, sticky="nsew")

    advert_window.mainloop()
