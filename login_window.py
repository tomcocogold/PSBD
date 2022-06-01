from tkinter import *
from tkinter import messagebox
import register_window
import account_window
import mysql.connector as mysql

def everything():
    color = "#29fbc1"

    def login():
        cnx = mysql.connect(user='root', password='',
                                      host='127.0.0.1',
                                      database='psbd')
        cursor = cnx.cursor()

        query = "SELECT email, haslo FROM uzytkownik_dane"

        entered_email = email_entry.get()
        entered_password = password_entry.get()

        cursor.execute(query)

        existing_account = False

        for (email, haslo) in cursor:
            if(entered_email, entered_password) == (email, haslo):
                existing_account = True
                break

        cursor.close()
        cnx.close()

        if existing_account:
            login_window.destroy()
            account_window.everything()
        else:
            messagebox.showwarning(title='Nieudane logowanie', message='Spróbuj ponownie')
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")

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
    login_label = Label(frame, text="Logowanie", font=("Arial", 20), bg=color, pady=30)

    # email
    email_label = Label(frame, text="Email", font=('Arial', 10), bg=color, pady=5)
    email_entry = Entry(frame, font=("Arial", 14), fg="black", bg="white")

    # password
    password_label = Label(frame, text="Hasło", font=('Arial', 10),bg=color, pady=5)
    password_entry = Entry(frame, font=("Arial", 14), fg="black", bg="white", show="*")

    # login button
    empty_label1 = Label(frame, text="", font=('Arial', 10), bg=color, pady=5)
    login_button = Button(frame, text="Zaloguj się", command=login)

    # register button
    empty_label2 = Label(frame, text="", font=('Arial', 10), bg=color)
    register_button = Button(frame, text="Zarejestruj się", command=register)

    login_label.grid(row=5, column=0, sticky="nsew")
    email_label.grid(row=10, column=0, sticky="nsew")
    email_entry.grid(row=15, column=0, sticky="nsew")
    password_label.grid(row=20, column=0, sticky="nsew")
    password_entry.grid(row=25, column=0, sticky="nsew")
    empty_label1.grid(row=30, column=0, sticky="nsew")
    login_button.grid(row=35, column=0, sticky="nsew")
    empty_label2.grid(row=40, column=0, sticky="nsew")
    register_button.grid(row=45, column=0, sticky="nsew")

    login_window.mainloop()
