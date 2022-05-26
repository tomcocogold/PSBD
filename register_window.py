from tkinter import *
import login_window
import mysql.connector as sql


def everything():

    def return_button():
        register_window.destroy()
        login_window.everything()

    def create_account():
        pass

    def tutor():
        pass

    def pupil():
        pass

    register_window = Tk()
    window_width = 900
    window_height = 600
    screen_width = register_window.winfo_screenwidth()
    screen_height = register_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    register_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    register_window.title("KOREPETIX/REJESTRACJA")
    register_window.config(background="#29fbc1")
    register_window.resizable(FALSE, FALSE)

    frame = Frame(register_window)
    frame.pack()

    # register
    Label(frame, text="Rejestracja", font=("Arial", 20), bg="#29fbc1", pady = 30).grid(row=0, column=0, sticky="nsew")

    # Name
    Label(frame, text="Imię", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=5, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white").grid(row=10, column=0, sticky="nsew")

    # Surname
    Label(frame, text="Nazwisko", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=15, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white", show="*").grid(row=20, column=0, sticky="nsew")

    # email
    Label(frame, text="Email", font=('Arial', 10), bg="#29fbc1", pady = 5).grid(row=25, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white").grid(row=30, column=0, sticky="nsew")

    # password
    Label(frame, text="Hasło", font=('Arial', 10), bg="#29fbc1", pady = 5).grid(row=35, column=0, sticky="nsew")

    Entry(frame, font=("Arial", 14), fg="black", bg="white", show="*").grid(row=40, column=0, sticky="nsew")

    Label(frame, text="", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=45, column=0, sticky="nsew")
    Checkbutton(frame, text="Korepetytor", font=('Arial', 10),command=tutor).grid(row=50, column=0, sticky="w")
    Label(frame, text="", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=52, column=0, sticky="nsew")
    Checkbutton(frame, text="Uczeń", font=('Arial', 10), command=pupil).grid(row=55, column=0, sticky="w")

    Label(frame, text="", font=('Arial', 10), bg="#29fbc1", pady=5).grid(row=60, column=0, sticky="nsew")
    Button(frame, text="Utwórz konto", command=create_account).grid(row=65, column=0, sticky="nsew")

    Label(frame, text="", font=('Arial', 10), bg="#29fbc1").grid(row=70, column=0, sticky="nsew")
    Button(frame, text="Wróć", command=return_button).grid(row=75, column=0, sticky="nsew")

    register_window.mainloop()
