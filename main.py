# Podanie wektora liczb rzeczywistych, sprawdzenie wejścia, wykonanie statystyk obliczeniowych

from tkinter import *
from tkinter import ttk
import math
import numpy as np
from scipy.stats import kurtosis


def userInput(n):
    elements = []
    el = 0
    while el < n:
        currEl = input("Podaj " + str(el + 1) + " element wektora: ")
        try:
            elements.append(float(currEl))
            el += 1
        except:
            print("Nie możesz podawać wartości innych niż liczbowe.")
    return elements


def mean(elements):
    return sum(elements) / len(elements)


def deviation(elements):
    currVal = 0
    for x in elements:
        currVal += (x-mean(elements))**2
    return math.sqrt(currVal/len(elements))


def view(elements):
    string = ""
    for x in range(len(elements)-1):
        string += str(elements[x]) + ", "
    return string + str(elements[-1])


def cov(elements):
    x = mean(elements)
    if x != 0:
        return (deviation(elements) / mean(elements)) * 100
    else:
        return "Średnia równa 0"


def generateView(args):
    win = Tk()

    # wybór rozmiaru okna tkinter
    win.geometry("700x600")
    win.title("Statystyka opisowa")
    s = ttk.Style()
    s.theme_use('clam')

    s.configure('Treeview', rowheight=40)

    tree = ttk.Treeview(win, column=("c1", "c2"), show='headings', height=14)
    tree.column("# 1", anchor=CENTER)
    tree.heading("# 1", text="Statystyka")
    tree.column("# 2", anchor=CENTER)
    tree.heading("# 2", text="Wynik")

    # dane
    tree.insert(parent='', index='end', iid=1, text='',
                   values=('Średnia', mean(args)))
    tree.insert(parent='', index='end', iid=2, text='',
                   values=('Odchylenie standardowe', deviation(args)))
    tree.insert(parent='', index='end', iid=3, text='',
                   values=('Współczynnik zmienności', cov(args)))
    tree.insert(parent='', index='end', iid=4, text='',
                   values=('Minimum', min(args)))
    tree.insert(parent='', index='end', iid=5, text='',
                   values=('10 Percentyl', np.percentile(args, 10)))
    tree.insert(parent='', index='end', iid=6, text='',
                   values=('1 Kwartyl', np.percentile(args, 25)))
    tree.insert(parent='', index='end', iid=7, text='',
                   values=('Mediana', np.percentile(args, 50)))
    tree.insert(parent='', index='end', iid=8, text='',
                   values=('3 Kwartyl', np.percentile(args, 75)))
    tree.insert(parent='', index='end', iid=9, text='',
                   values=('90 Percentyl', np.percentile(args, 90)))
    tree.insert(parent='', index='end', iid=10, text='',
                   values=('Maximum', max(args)))
    tree.insert(parent='', index='end', iid=11, text='',
                   values=('Rozstęp danych', max(args)-min(args)))
    tree.insert(parent='', index='end', iid=12, text='',
                   values=('Rozstęp międzykwartylowy', np.percentile(args, 75) - np.percentile(args, 25)))
    tree.insert(parent='', index='end', iid=13, text='',
                   values=('Skośność', 3*((mean(args) - np.percentile(args, 50))/deviation(args))))
    tree.insert(parent='', index='end', iid=14, text='',
                   values=('Kurtoza', kurtosis(args)))


    # generowanie
    tree.pack()
    win.mainloop()

if __name__ == '__main__':
    length = input("Podaj długość wektora, któreg dane będziesz wprowadzał: ")

    try:
        tab = userInput(int(length))
        # widok tabeli
        if type(tab) == list:
            generateView(tab)
    except:
        print("Źle wprowadzone dane")
