import Main
import tkinter as tk

okno = tk.Tk()

global denar

denar_str = tk.StringVar()

denar_str.set(str(Main.denar) + " $")

text_input = tk.Entry()
text_input.grid(row=0, column=1)
oznaka = tk.Label(okno, textvariable = denar_str)
oznaka.grid(row=0, column=0)


generiraj = tk.Button(okno, text="generiraj", command=lambda :generiraj_delnico(text_input.get()))
generiraj.grid(row=1, column=0)


kolicina_nakupa = tk.Entry()
kolicina_nakupa.grid(row=3, column=3)
kupi = tk.Button(okno, text="kupi", command=lambda :lambda_nakup())
kupi.grid(row=3, column=4)


kolicina_prodaja = tk.Entry()
kolicina_prodaja.grid(row=4, column=3)
kupi = tk.Button(okno, text="prodaj", command=lambda :lambda_prodaja())
kupi.grid(row=4, column=4)


posodobi = tk.Button(okno, text="posodobi", command=lambda: delnica.posodobi())
posodobi.grid(row=2, column=0)


def lambda_nakup():
    delnica.nakup(kolicina_nakupa.get())
    denar_str.set(str(Main.denar) + " $")


def lambda_prodaja():
    delnica.prodaja(kolicina_prodaja.get())
    denar_str.set(str(Main.denar) + " $")


def generiraj_delnico(oznaka):
    global delnica
    delnica = Main.Delnice([1,1], oznaka, okno)

    print(delnica)


okno.mainloop()
