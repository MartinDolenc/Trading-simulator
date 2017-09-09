import ystockquote
import tkinter as tk
import time
from tkinter import messagebox

denar = 10000.0
canvas_width = 500.0
canvas_height = 500.0
canvas_zamik = 10.0
kolicina_delnic = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
delnice_po_abecedi = ["amd", "aapl", "kof", "fb", "googl", "intc", "logi", "msft", "tsla", "twtr"]

class Delnice:

    def __init__(self, lokacija, oznaka, okno):
        self.lokacija = lokacija
        self.oznaka = oznaka
        self.trenutna_vrednost = ystockquote.get_last_trade_price(oznaka)
        self.prejsnje_vrednosti = 10*[canvas_zamik/50]
        self.okno = okno


        self.posodobi()

    def prikaz_denarja(self):
        print(denar)

    def nakup(self, kolicina):
        global denar

        cena_nakupa = float(ystockquote.get_last_trade_price(self.oznaka))*float(kolicina)

        x = delnice_po_abecedi.index(str(self.oznaka))

        if cena_nakupa <= denar:

            denar -= cena_nakupa
            denar = round(denar, 2)

            kolicina_delnic[x] += int(kolicina)
        else:
            messagebox.showinfo("Error", "nimate dovolj denarja")

        self.posodobi()

        print(denar)
        print(kolicina_delnic)


    def prodaja(self, kolicina):
        global denar

        cena_prodaje = float(ystockquote.get_last_trade_price(self.oznaka))*float(kolicina)

        x = delnice_po_abecedi.index(str(self.oznaka))

        if int(kolicina) < kolicina_delnic[x]:

            denar += cena_prodaje
            denar = round(denar, 2)

            kolicina_delnic[x] -= kolicina
        else:
            messagebox.showinfo("Error", "nimate dovolj delnic")

        self.posodobi()

        print(denar)
        print(kolicina_delnic)

    def Canvas_Graf(self):
        self.graf = tk.Canvas(self.okno, width=canvas_width, height=canvas_height)
        self.graf.grid(row=self.lokacija[0], column=self.lokacija[1])
        self.graf.create_line(canvas_zamik, canvas_height-canvas_zamik, canvas_width-canvas_zamik, canvas_height-canvas_zamik, fill="#476042",width=2)
        self.graf.create_line(canvas_zamik, canvas_height-canvas_zamik, canvas_zamik, canvas_zamik, fill="#476042",width=2)
        self.graf.create_text(0, 0, text=str((float(self.prejsnje_vrednosti[9])//10)*10 + 10) + " $", anchor="nw")
        self.graf.create_text(0, canvas_height, text=str((float(self.prejsnje_vrednosti[9])//10)*10) + " $", anchor="sw")
        self.graf.create_text(canvas_width, 0, text=self.oznaka, anchor="ne")
        self.graf.create_text(canvas_width, 20, text="število delnic: " + str(kolicina_delnic[delnice_po_abecedi.index(str(self.oznaka))]), anchor="ne")

        # markings on x axis
        for i in range(11):
            x = 100 + (i * 30)
            self.graf.create_text(x, canvas_height, text='%d' % (30 * i), anchor="s")

        for x in range(9):
            self.graf.create_line(x*50, ((canvas_height - float(self.prejsnje_vrednosti[x]))%10)*50, (x+1)*50, ((canvas_height - float(self.prejsnje_vrednosti[x+1]))%10)*50, fill="#476042", width=2)




    def posodobi(self):
        while True:
            self.trenutna_vrednost = ystockquote.get_last_trade_price(self.oznaka)
            self.prejsnje_vrednosti = self.prejsnje_vrednosti[1:] + [self.trenutna_vrednost]
            self.Canvas_Graf()
            print(self.prejsnje_vrednosti)
            time.sleep(120)
            #self.posodobi()
