import tkinter as tk
from tkinter import messagebox

class MyGUI:
    def __init__(self):
        self.janela = tk.Tk()

        self.frameTopo = tk.Frame(self.janela)
        self.frameBase = tk.Frame(self.janela)

        self.cbVar1 = tk.IntVar()
        self.cbVar2 = tk.IntVar()
        self.cbVar3 = tk.IntVar()

        self.cbVar1.set(0)
        self.cbVar2.set(0)
        self.cbVar3.set(0)

        self.cb1 = tk.Checkbutton(self.frameTopo, text = 'Opção 1', variable=self.cbVar1)
        self.cb2 = tk.Checkbutton(self.frameTopo, text = 'Opção 2', variable=self.cbVar2)
        self.cb3 = tk.Checkbutton(self.frameTopo, text = 'Opção 3', variable=self.cbVar3)

        self.cb1.pack()
        self.cb2.pack()
        self.cb3.pack()

        self.okButton = tk.Button(self.frameBase, text = 'OK', command = self.mostraEscolha)
        self.finalizaButton = tk.Button(self.frameBase, text = 'Finaliza', command = self.janela.destroy)

        self.okButton.pack(side='left')
        self.finalizaButton.pack(side='left')

        self.frameTopo.pack()
        self.frameBase.pack()

        tk.mainloop()

    def mostraEscolha(self):
        self.message = 'Voce selecionou: \n'

        if self.cbVar1.get()==1:
            self.message=self.message+'1\n'
        if self.cbVar2.get()==1:
            self.message=self.message+'2\n'
        if self.cbVar3.get()==1:
            self.message=self.message+'3\n'
        
        messagebox.showinfo('Seleção',self.message)

def main():
    MyGUI()

main()
        
