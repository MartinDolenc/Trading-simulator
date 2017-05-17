import ystockquote
import tkinter as tk
import time

global denar
denar = 10000

class Delnice:

    def __init__(self, lokacija, oznaka, stevilo_delnic):
        self.lokacija = lokacija
        self.oznaka = oznaka
        self.stevilo_delnic = stevilo_delnic
        self.trenutna_vrednost = ystockquote.get_last_trade_price(oznaka)
        self.prejsnje_vrednosti = 5*[0]


        self.posodobi()

    def nakup(self, oznaka, kolicina):
        denar -= ystockquote.get_last_trade_price(oznaka)*kolicina


    def prodaja(self, oznaka, kolicina):
        denar += ystockquote.get_last_trade_price(oznaka)*kolicina

    def graf(self, prejsnje_vrednosti):
        self.graf = tk.Canvas


    def posodobi(self):
        while True:
            self.trenutna_vrednost = ystockquote.get_last_trade_price(self.oznaka)
            self.prejsnje_vrednosti = self.prejsnje_vrednosti[1:].append(self.trenutna_vrednost)
            self.graf(self.prejsnje_vrednosti)


            time.sleep(5)








def pridobljaj_cene(perioda):

    while True:

        time.sleep(perioda)


def pridobi_zadnjo_ceno(oznaka):
    return ystockquote.get_last_trade_price(oznaka)
