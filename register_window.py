from tkinter import *
from tkinter import messagebox

import login_window
import account_window
import mysql.connector as mysql


def everything():
    color = "#29fbc1"

    def return_button():
        register_window.destroy()
        login_window.everything()

    def create_account():
        cnx = mysql.connect(user='root', password='',
                            host='127.0.0.1',
                            database='psbd')
        cursor = cnx.cursor(buffered=True)

        entered_name = name_entry.get()
        entered_surname = surname_entry.get()
        entered_email = email_entry.get()
        entered_password = password_entry.get()

        existing_account = False

        query = "SELECT * FROM uzytkownik_dane"
        cursor.execute(query)
        for email in cursor:
            if entered_email == email:
                existing_account = True
                break

        if existing_account or not entered_surname or not entered_email or not entered_name or not entered_password:
            messagebox.showwarning(title='Nieudana rejestracja', message='Spróbuj ponownie')
            email_entry.delete(0, "end")
            password_entry.delete(0, "end")
            name_entry.delete(0, "end")
            surname_entry.delete(0, "end")

        # if the account doesn't exist we can create a new account
        elif not existing_account and entered_name and entered_surname and entered_email and entered_password:
            new_account = ("""INSERT INTO uzytkownik_zarejestrowany(haslo) VALUES (%s);
                            INSERT INTO imie(imie) VALUES (%s);
                            INSERT INTO nazwisko(nazwisko) VALUES (%s);
                            INSERT INTO email(email) VALUES (%s);
                            """)
            cursor.execute(new_account, (str(entered_password), str(entered_name),
                           str(entered_surname), str(entered_email)))
            register_window.destroy()
            account_window.everything() #TODO wyciągnąć z bazy danych iduzytkownika
        cnx.commit()
        cursor.close()
        cnx.close()

    register_window = Tk()
    window_width = 900
    window_height = 600
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    register_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    register_window.title("KOREPETIX/REJESTRACJA")
    register_window.config(background=color)
    register_window.resizable(FALSE, FALSE)

    frame = Frame(register_window)
    frame.pack()

    # register
    register_label = Label(frame, text="Rejestracja", font=("Arial", 20), bg=color, pady=30)

    # Name
    name_label = Label(frame, text="Imię", font=('Arial', 10), bg=color, pady=5)
    name_entry = Entry(frame, font=("Arial", 14), fg="black", bg="white")

    # Surname
    surname_label = Label(frame, text="Nazwisko", font=('Arial', 10), bg=color, pady=5)
    surname_entry = Entry(frame, font=("Arial", 14), fg="black", bg="white")

    # email
    email_label = Label(frame, text="Email", font=('Arial', 10), bg=color, pady=5)
    email_entry = Entry(frame, font=("Arial", 14), fg="black", bg="white")

    # password
    password_label = Label(frame, text="Hasło", font=('Arial', 10), bg=color, pady=5)
    password_entry = Entry(frame, font=("Arial", 14), fg="black", bg="white", show="*")

    var = IntVar()  # control variable for Radio Buttons in the group
    empty_label1 = Label(frame, text="", font=('Arial', 10), bg=color, pady=5)
    tutor_button = Radiobutton(frame, text="Korepetytor", font=('Arial', 10), variable=var, value=1)
    empty_label2 = Label(frame, text="", font=('Arial', 10), bg=color, pady=5)
    pupil_button = Radiobutton(frame, text="Uczeń", font=('Arial', 10), variable=var, value=2)

    empty_label3 = Label(frame, text="", font=('Arial', 10), bg=color, pady=5)
    create_button = Button(frame, text="Utwórz konto", command=create_account)

    empty_label4 = Label(frame, text="", font=('Arial', 10), bg=color)
    return_button = Button(frame, text="Wróć", command=return_button)

    register_label.grid(row=5, column=0, sticky="nsew")
    name_label.grid(row=10, column=0, sticky="nsew")
    name_entry.grid(row=15, column=0, sticky="nsew")
    surname_label.grid(row=20, column=0, sticky="nsew")
    surname_entry.grid(row=25, column=0, sticky="nsew")
    email_label.grid(row=30, column=0, sticky="nsew")
    email_entry.grid(row=35, column=0, sticky="nsew")
    password_label.grid(row=40, column=0, sticky="nsew")
    password_entry.grid(row=45, column=0, sticky="nsew")
    empty_label1.grid(row=50, column=0, sticky="nsew")
    tutor_button.grid(row=55, column=0, sticky="nsew")
    empty_label2.grid(row=60, column=0, sticky="nsew")
    pupil_button.grid(row=65, column=0, sticky="nsew")
    empty_label3.grid(row=70, column=0, sticky="nsew")
    create_button.grid(row=75, column=0, sticky="nsew")
    empty_label4.grid(row=80, column=0, sticky="nsew")
    return_button.grid(row=85, column=0, sticky="nsew")

    register_window.mainloop()
