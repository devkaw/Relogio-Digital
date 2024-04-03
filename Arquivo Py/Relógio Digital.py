from tkinter import *
from time import strftime

def atualizar_relogio():
    horario_atual = strftime("%H:%M:%S %p")
    rotulo_relogio.config(text=horario_atual)
    rotulo_relogio.after(1000, atualizar_relogio)

janela = Tk()
janela.title('Relógio Digital')
rotulo_relogio = Label(
    janela,
    font=('Arial', 40, 'bold'),
    bg="light blue",
    fg="white"
)
rotulo_relogio.pack(anchor='center')
atualizar_relogio()
janela.mainloop()