# Apresentação da biblioteca tktinker
import tkinter as tk
janela = tk.Tk()
janela.geometry("250x250")
strg = "Olá Mundo!!"
strg2 = "BRASIL"
strg = strg+"\n"+strg2
labell = tk.Label(text=strg)
labell.pack()
janela.mainloop()