from tkinter import *
from tkinter import ttk
import login_window
import register_window
import account_window
import mysql.connector as mysql


def everything():
    color = "#29fbc1"

    def return_button():
        search_window.destroy()
        account_window.everything()

    def search_tutors_adverts():
        pass

    def search_pupils_adverts():
        pass

    search_window = Tk()
    window_width = 900
    window_height = 600
    screen_width = search_window.winfo_screenwidth()
    screen_height = search_window.winfo_screenheight()

    x = int((screen_width / 2) - (window_width / 2))
    y = int((screen_height / 2) - (window_height / 2))

    search_window.geometry("{}x{}+{}+{}".format(window_width, window_height, x, y))
    search_window.title("KOREPETIX/WYSZUKIWARKA OGŁOSZEŃ")
    search_window.config(background="#29fbc1")
    search_window.resizable(FALSE, FALSE)

    search_engine = ttk.Notebook(search_window)  # widget that manages a collection of windows/displays
    tab1 = Frame(search_window, bg="#29fbc1")  # new frame for tab 1
    tab2 = Frame(search_window, bg="#29fbc1")  # new frame for tab 2

    search_engine.add(tab1, text='Ogłoszenia korepetytorów')
    search_engine.add(tab2, text='Ogłoszenia uczniów')
    search_engine.pack(expand=True, fill='both')
    # expand = expand to fill any space not otherwise used
    # fill = fill space on x and y axis

    frame1 = Frame(tab1)
    frame1.pack()
    Entry(frame1, width=50).grid(row=0, column=0)
    Button(frame1, text="Szukaj", command=search_tutors_adverts).grid(row=0, column=1)
    Label(frame1, text="                  ", bg=color).grid(row=0, column=2, sticky="nsew")
    Button(frame1, text="Wróć", command=return_button).grid(row=0, column=3)

    scrollbar = Scrollbar(frame1, bg=color)
    scrollbar.grid(rowspan=10, column=10, sticky="ns")
    advert1 = Button(frame1, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert2 = Button(frame1, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert3 = Button(frame1, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert4 = Button(frame1, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert5 = Button(frame1, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")

    advert1.grid(row=10, columnspan=4, sticky="nsew")
    advert2.grid(row=15, columnspan=4, sticky="nsew")
    advert3.grid(row=20, columnspan=4, sticky="nsew")
    advert4.grid(row=25, columnspan=4, sticky="nsew")
    advert5.grid(row=30, columnspan=4, sticky="nsew")

    frame2 = Frame(tab2)
    frame2.pack()
    Entry(frame2, width=50).grid(row=0, column=0)
    Button(frame2, text="Szukaj", command=search_pupils_adverts).grid(row=0, column=1)
    Label(frame2, text="                  ", bg=color).grid(row=0, column=2, sticky="nsew")
    Button(frame2, text="Wróć", command=return_button).grid(row=0, column=3)

    scrollbar = Scrollbar(frame2, bg=color)
    scrollbar.grid(rowspan=10, column=10, sticky="ns")
    advert1 = Button(frame2, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert2 = Button(frame2, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert3 = Button(frame2, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert4 = Button(frame2, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")
    advert5 = Button(frame2, text="Przedmiot: matematyka\nCena[zł/h]: 50\nOpis: nowe ogłoszenie")

    advert1.grid(row=10, columnspan=4, sticky="nsew")
    advert2.grid(row=15, columnspan=4, sticky="nsew")
    advert3.grid(row=20, columnspan=4, sticky="nsew")
    advert4.grid(row=25, columnspan=4, sticky="nsew")
    advert5.grid(row=30, columnspan=4, sticky="nsew")


    search_window.mainloop()
