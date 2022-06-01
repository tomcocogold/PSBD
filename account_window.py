from tkinter import *
from tkinter import ttk
import login_window
import search_engine
import register_window
import mysql.connector as mysql


def everything():
    color = "#29fbc1"

    def log_out():
        account_window.destroy()
        login_window.everything()

    def change_password():
        def return_button():
            change_password_window.destroy()

        def change_password_button():
            pass

        change_password_window = Toplevel(bg=color)
        change_password_window.title("Zmiana hasła")
        change_password_window.geometry("250x100")
        old_password = Label(change_password_window, text="Stare hasło", font=("Arial", 10), bg=color)
        new_password = Label(change_password_window, text="Nowe hasło", font=("Arial", 10), bg=color)
        repeat_password = Label(change_password_window, text="Powtórz hasło", font=("Arial", 10), bg=color)
        old_password_entry = Entry(change_password_window)
        new_password_entry = Entry(change_password_window)
        repeat_password_entry = Entry(change_password_window)
        return_button = Button(change_password_window, text="Wróć", command=return_button)
        change_password_button = Button(change_password_window, text="Zmień hasło", command=change_password_button)

        old_password.grid(row=0, column=0)
        new_password.grid(row=1, column=0)
        repeat_password.grid(row=2, column=0)
        old_password_entry.grid(row=0, column=1)
        new_password_entry.grid(row=1, column=1)
        repeat_password_entry.grid(row=2, column=1)
        return_button.grid(row=3, column=0)
        change_password_button.grid(row=3, column=1)

        change_password_window.mainloop()

    def change_data():

        def return_button():
            change_data_window.destroy()

        def change_data_button():
            pass

        change_data_window = Toplevel(bg=color)
        change_data_window.title("Zmiana danych")
        change_data_window.geometry("250x100")
        new_name = Label(change_data_window, text="Imię", font=("Arial", 10), bg=color)
        new_surname = Label(change_data_window, text="Nazwisko", font=("Arial", 10), bg=color)
        new_email = Label(change_data_window, text="Email", font=("Arial", 10), bg=color)
        new_name_entry = Entry(change_data_window)
        new_surname_entry = Entry(change_data_window)
        new_email_entry = Entry(change_data_window)
        return_button = Button(change_data_window, text="Wróć", command=return_button)
        change_password_button = Button(change_data_window, text="Zmień dane", command=change_data_button)

        new_name.grid(row=0, column=0)
        new_surname.grid(row=1, column=0)
        new_email.grid(row=2, column=0)
        new_name_entry.grid(row=0, column=1)
        new_surname_entry.grid(row=1, column=1)
        new_email_entry.grid(row=2, column=1)
        return_button.grid(row=3, column=0)
        change_password_button.grid(row=3, column=1)

        change_data_window.mainloop()

    def add_advert():
        def return_button():
            add_advert_window.destroy()

        def create_advert():
            pass

        add_advert_window = Toplevel(bg=color)
        add_advert_window.title("Dodaj ogłoszenie")
        add_advert_window.geometry("500x400")
        frame = Frame(add_advert_window, bg=color)
        frame.pack()
        subject = Label(frame, text="Przemiot", font=("Arial", 10), bg=color)
        price = Label(frame, text="Cena [zł/h]", font=("Arial", 10), bg=color)
        duration = Label(frame, text="Czas lekcji [min]", font=("Arial", 10), bg=color)
        mode = Label(frame, text="Tryb", font=("Arial", 10), bg=color)
        description = Label(frame, text="Opis", font=("Arial", 10), bg=color)
        links = Label(frame, text="Linki", font=("Arial", 10), bg=color)
        films = Label(frame, text="Filmy", font=("Arial", 10), bg=color)
        images = Label(frame, text="Ilustracje", font=("Arial", 10), bg=color)
        subject_entry = Entry(frame)
        price_entry = Entry(frame)
        duration_entry = Entry(frame)
        mode_entry = Entry(frame)
        description_area = Frame(frame)
        description_entry = Text(description_area, width=30, height=3)
        links_area = Frame(frame)
        links_entry = Text(links_area, width=30, height=3)
        films_area = Frame(frame)
        films_entry = Text(films_area, width=30, height=3)
        images_area = Frame(frame)
        images_entry = Text(images_area, width=30, height=3)
        return_button = Button(frame, text="Wróć", command=return_button)
        create_advert_button = Button(frame, text="Utwórz ogłoszenie", command=create_advert)

        subject.grid(row=0, column=0)
        price.grid(row=1, column=0)
        duration.grid(row=2, column=0)
        mode.grid(row=3, column=0)
        description.grid(row=4, column=0)
        links.grid(row=5, column=0)
        films.grid(row=6, column=0)
        images.grid(row=7, column=0)

        subject_entry.grid(row=0, column=1, sticky='ew')
        price_entry.grid(row=1, column=1, sticky='ew')
        duration_entry.grid(row=2, column=1, sticky='ew')
        mode_entry.grid(row=3, column=1, sticky='ew')
        description_area.grid(row=4, column=1)
        description_entry.grid(row=4, column=1)
        links_area.grid(row=5, column=1)
        links_entry.grid(row=5, column=1)
        films_area.grid(row=6, column=1)
        films_entry.grid(row=6, column=1)
        images_area.grid(row=7, column=1)
        images_entry.grid(row=7, column=1)

        return_button.grid(row=8, column=0)
        create_advert_button.grid(row=8, column=1)

        add_advert_window.mainloop()

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
    account_window.config(background=color)
    account_window.resizable(FALSE, FALSE)

    notebook = ttk.Notebook(account_window)  # widget that manages a collection of windows/displays
    tab1 = Frame(notebook, bg=color)  # new frame for tab 1
    tab2 = Frame(notebook, bg=color)  # new frame for tab 2
    tab3 = Frame(notebook, bg=color)  # new frame for tab 3
    tab4 = Frame(notebook, bg=color)

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
    Label(frame1, text="Dane użytkownika", font=("Arial", 20), bg=color, pady=30).grid(row=0, column=0, sticky="nsew")

    # Name
    Label(frame1, text="Imię", font=('Arial', 10), bg=color, pady=5).grid(row=5, column=0, sticky="nsew")
    Label(frame1, text="", font=("Arial", 14), fg="black", bg="white").grid(row=10, column=0, sticky="nsew")

    # Surname
    Label(frame1, text="Nazwisko", font=('Arial', 10), bg=color, pady=5).grid(row=15, column=0, sticky="nsew")
    Label(frame1, text="", font=("Arial", 14), fg="black", bg="white").grid(row=20, column=0, sticky="nsew")

    # email
    Label(frame1, text="Email", font=('Arial', 10), bg=color, pady=5).grid(row=25, column=0, sticky="nsew")
    Label(frame1, text="", font=("Arial", 14), fg="black", bg="white").grid(row=30, column=0, sticky="nsew")
    Label(frame1, text="Rodzaj konta", font=('Arial', 10), bg=color, pady=5).grid(row=35, column=0, sticky="nsew")
    Label(frame1, text="", font=("Arial", 14), fg="black", bg="white").grid(row=40, column=0, sticky="nsew")

    frame2 = Frame(tab2) # moje ogłoszenia
    frame2.pack()
    Label(frame2, text="", bg="#29fbc1").grid(row=0, columnspan=3, sticky="nsew")
    Button(frame2, text="Dodaj ogłoszenie", command=add_advert).grid(row=5, column=0)
    Label(frame2, text="                  ", bg=color).grid(row=5, column=1, sticky="nsew")
    Button(frame2, text="Szukaj ogłoszeń", command=search_advert).grid(row=5, column=2)
    Label(frame2, text="Moje ogłoszenia", font=("Arial", 14), bg=color).grid(row=10, columnspan=3, sticky="nsew")

    frame3 = Frame(tab3) # moje zajęcia
    frame3.pack()
    Label(frame3, text="Odbyte", font=("Arial", 14), bg=color).grid(row=0, column=0, sticky="nsew")
    Label(frame3, text="                                                                             ",
          bg=color).grid(row=0, column=1, sticky="nsew")
    Label(frame3, text="Nadchodzące", font=("Arial", 14), bg=color).grid(row=0, column=2, sticky="nsew")

    frame4 = Frame(tab4) # ustawienia konta
    frame4.pack()
    Label(frame4, text="", bg=color).grid(row=0, column=0, sticky="nsew")
    Button(frame4, text="Zmień dane", command=change_data).grid(row=5, column=0)
    Label(frame4, text="", bg=color).grid(row=10, column=0, sticky="nsew")
    Button(frame4, text="Zmień Hasło", command=change_password).grid(row=15, column=0)
    Label(frame4, text="", bg=color).grid(row=20, column=0, sticky="nsew")
    Button(frame4, text="Wyloguj się", command=log_out).grid(row=25, column=0)

    account_window.mainloop()
