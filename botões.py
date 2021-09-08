import tkinter as tk

class MyGui:
    def __init__(self):
        self.janela = tk.Tk()
        self.botao1 = tk.Button(self.janela, text = 'Botão 1', command= self.processaB1)
        self.botao2 = tk.Button(self.janela, text='Botão 2', command=self.processaB2)
        self.botao1.pack()
        self.botao2.pack()
        self.label = tk.Label(self.janela, text='Escolha...')
        self.label.pack()

        tk.mainloop()
    
    def processaB1(self):
        self.label.configure(text='Botao 1 foi clicado')
    def processaB2(self):
        self.label.configure(text='Botão 2 foi clicado')

def main():
    MyGui()

main()