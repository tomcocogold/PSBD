from tkinter import *
import register_window
import account_window
import mysql.connector as sql

import search_engine


def everything():
    color = "#29fbc1"

    def return_button():
        advert_window.destroy()
        search_engine.everything()

    def sign_up():
        pass

    def add_opinion():
        pass

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

    frame = Frame(advert_window, bg=color)
    frame.pack()
    subject = Label(frame, text="Przemiot", font=("Arial", 10), bg=color)
    price = Label(frame, text="Cena [zł/h]", font=("Arial", 10), bg=color)
    duration = Label(frame, text="Czas lekcji [min]", font=("Arial", 10), bg=color)
    mode = Label(frame, text="Tryb", font=("Arial", 10), bg=color)
    description = Label(frame, text="Opis", font=("Arial", 10), bg=color)
    links = Label(frame, text="Linki", font=("Arial", 10), bg=color)
    films = Label(frame, text="Filmy", font=("Arial", 10), bg=color)
    images = Label(frame, text="Ilustracje", font=("Arial", 10), bg=color)
    subject_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    price_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    duration_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    mode_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    description_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    links_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    films_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    images_entry = Label(frame, text="", font=("Arial", 14), bg="white", relief="sunken")
    return_button = Button(frame, text="Wróć", command=return_button)
    sign_up_button = Button(frame, text="Zapisz się", command=sign_up)
    add_opinion_button = Button(frame, text="Dodaj opinię", command=add_opinion)

    subject.grid(row=0, column=0)
    price.grid(row=5, column=0)
    duration.grid(row=10, column=0)
    mode.grid(row=15, column=0)
    description.grid(row=20, column=0)
    links.grid(row=25, column=0)
    films.grid(row=30, column=0)
    images.grid(row=35, column=0)

    subject_entry.grid(row=0, column=1, sticky='ew')
    price_entry.grid(row=5, column=1, sticky='ew')
    duration_entry.grid(row=10, column=1, sticky='ew')
    mode_entry.grid(row=15, column=1, sticky='ew')
    description_entry.grid(row=20, column=1, sticky='ew')
    links_entry.grid(row=25, column=1, sticky='ew')
    films_entry.grid(row=30, column=1, sticky='ew')
    images_entry.grid(row=35, column=1, sticky='ew')

    return_button.grid(row=40, column=0)
    sign_up_button.grid(row=40, column=1)
    add_opinion_button.grid(row=45, column=1)

    advert_window.mainloop()

