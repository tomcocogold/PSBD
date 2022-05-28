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

    login_window = Tk()

    window_width = 900
    window_height = 600
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    login_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

    login_window.title("KOREPETIX/LOGOWANIE")
    login_window.config(background=color)
    login_window.resizable(FALSE, FALSE)

    frame = Frame(login_window)
    frame.pack()
    # login
    Label(frame, text="Logowanie", font=("Arial", 20), bg=color, pady=30).grid(row=0, column=0, sticky="nsew")

    # email
    Label(frame, text="Email", font=('Arial', 10), bg=color, pady=5).grid(row=2, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white").grid(row=3, column=0, sticky="nsew")

    # password
    Label(frame, text="Hasło", font=('Arial', 10),bg=color, pady=5).grid(row=5, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white", show="*").grid(row=6, column=0, sticky="nsew")

    # login button
    Label(frame, text="", font=('Arial', 10), bg=color, pady=5).grid(row=7, column=0, sticky="nsew")

    Button(frame, text="Zaloguj się", command=login).grid(row=8, column=0, sticky="nsew")
    # register button
    Label(frame, text="", font=('Arial', 10), bg=color).grid(row=9, column=0, sticky="nsew")

    Button(frame, text="Zarejestruj się", command=register).grid(row=10, column=0, sticky="nsew")

    login_window.mainloop()
