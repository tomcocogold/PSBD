from tkinter import *
import register_window
import mysql.connector as sql


def everything():
    def login():
        pass

    def register():
        login_window.destroy()
        register_window.everything()

    login_window = Tk()

    window_width = 1000
    window_height = 700
    screen_width = login_window.winfo_screenwidth()
    screen_height = login_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    login_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))

    login_window.title("KOREPETIX/LOGOWANIE")
    login_window.config(background="#29fbc1")
    login_window.resizable(FALSE, FALSE)

    frame = Frame(login_window)
    frame.pack()
    # login
    Label(frame, text="Logowanie", font=("Arial", 20), bg="#29fbc1", pady=30).grid(row=0, column=0, sticky="nsew")

    # email
    Label(frame, text="Email", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=2, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white").grid(row=3, column=0, sticky="nsew")

    # password
    Label(frame, text="Hasło", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=5, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white", show="*").grid(row=6, column=0, sticky="nsew")

    # login button
    Label(frame, text="", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=7, column=0, sticky="nsew")

    Button(frame, text="Zaloguj się", command=login).grid(row=8, column=0, sticky="nsew")
    # register button
    Label(frame, text="", font=('Arial', 10), bg="#29fbc1").grid(row=9, column=0, sticky="nsew")

    Button(frame, text="Zarejestruj się", command=register).grid(row=10, column=0, sticky="nsew")

    login_window.mainloop()
