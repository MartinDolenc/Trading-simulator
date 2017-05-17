import tkinter as tk


okno = tk.Tk()


gumb = tk.Entry()
gumb.grid(row=0, column=1)
oznaka = tk.Label(okno,text='Hello')
oznaka.grid(row=0, column=0)



okno.mainloop()
