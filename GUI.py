import Main
import tkinter as tk

okno = tk.Tk()

global denar

text_input = tk.Entry()
text_input.grid(row=0, column=1)
oznaka = tk.Label(okno,text= "" + str(Main.denar) + " $")
oznaka.grid(row=0, column=0)
generiraj1 = tk.Button(okno, text="generiraj", command=lambda :generiraj_delnico(text_input.get()))
generiraj1.grid(row=1, column=0)
generiraj2 = tk.Button(okno, text="generiraj", command=lambda :generiraj_delnico(text_input.get()))
generiraj2.grid(row=1, column=1)
generiraj3 = tk.Button(okno, text="generiraj", command=lambda :generiraj_delnico(text_input.get()))
generiraj3.grid(row=1, column=2)



kolicina_nakupa = tk.Entry()
kolicina_nakupa.grid(row=3, column=3)
kupi = tk.Button(okno, text="kupi", command=lambda :delnica.nakup(kolicina_nakupa.get()))
kupi.grid(row=3, column=4)




def generiraj_delnico(oznaka):
    global delnica
    delnica = Main.Delnice(1, oznaka, 10, okno)




posodobi = tk.Button(okno, text="posodobi", command=lambda: delnica.posodobi())
posodobi.grid(row=2, column=0)

okno.mainloop()
