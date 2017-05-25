import ystockquote
import tkinter as tk
import time

denar = 10000.0
canvas_width = 500.0
canvas_height = 500.0
canvas_zamik = 10.0


class Delnice:

    def __init__(self, lokacija, oznaka, stevilo_delnic, okno):
        self.lokacija = lokacija
        self.oznaka = oznaka
        self.stevilo_delnic = stevilo_delnic
        self.trenutna_vrednost = ystockquote.get_last_trade_price(oznaka)
        self.prejsnje_vrednosti = 10*[canvas_zamik/50]
        self.okno = okno


        #self.posodobi()

    def prikaz_denarja(self):
        print(denar)

    def nakup(self, kolicina):
        global denar
        denar -= float(ystockquote.get_last_trade_price(self.oznaka))*float(kolicina)
        print(denar)


    def prodaja(self, kolicina):
        global denar
        denar += float(ystockquote.get_last_trade_price(self.oznaka))*float(kolicina)
        print(denar)

    def Canvas_Graf(self):
        self.graf = tk.Canvas(self.okno, width=canvas_width, height=canvas_height)
        self.graf.grid(row=self.lokacija, column=self.lokacija)
        self.graf.create_line(canvas_zamik, canvas_height-canvas_zamik, canvas_width-canvas_zamik, canvas_height-canvas_zamik, fill="#476042",width=2)
        self.graf.create_line(canvas_zamik, canvas_height-canvas_zamik, canvas_zamik, canvas_zamik, fill="#476042",width=2)
        self.graf.create_text(0, 0, text=str((float(self.prejsnje_vrednosti[9])//10)*10 + 10) + " $", anchor="nw")
        self.graf.create_text(0, canvas_height, text=str((float(self.prejsnje_vrednosti[9])//10)*10) + " $", anchor="sw")
        self.graf.create_text(canvas_width, 0, text=self.oznaka, anchor="ne")

        # markings on x axis
        for i in range(11):
            x = 100 + (i * 30)
            self.graf.create_text(x, canvas_height, text='%d' % (30 * i), anchor="s")

        for x in range(9):
            self.graf.create_line(x*50, ((canvas_height - float(self.prejsnje_vrednosti[x]))%10)*50, (x+1)*50, ((canvas_height - float(self.prejsnje_vrednosti[x+1]))%10)*50, fill="#476042", width=2)


    def posodobi(self):
        #while True:
            self.trenutna_vrednost = ystockquote.get_last_trade_price(self.oznaka)
            self.prejsnje_vrednosti = self.prejsnje_vrednosti[1:] + [self.trenutna_vrednost]
            print(self.prejsnje_vrednosti)
            self.Canvas_Graf()
            #time.sleep(10)
            #self.posodobi()
