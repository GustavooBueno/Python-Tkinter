import tkinter as tk

class MyGui:
    def __init__(self):
        self.janela = tk.Tk()
        self.frameTopo = tk.Frame(self.janela)
        self.frameBase = tk.Frame(self.janela)

        #labels pro frame topo
        self.label1 = tk.Label(self.frameTopo, text= 'Um')
        self.label2 = tk.Label(self.frameTopo, text='Dois')
        self.label3 = tk.Label(self.frameTopo, text='Tres')

        #empilhando as labels
        self.label1.pack(side='top')
        self.label2.pack(side='top')
        self.label3.pack(side='top')

        #labels pro frame base
        self.label4 = tk.Label(self.frameBase, text= 'Quatro')
        self.label5 = tk.Label(self.frameBase, text='Cinco')
        self.label6 = tk.Label(self.frameBase, text='Seis')

        #empilhando as labels
        self.label4.pack(side='left')
        self.label5.pack(side='left')
        self.label6.pack(side='left')

        #empacotando os frames
        self.frameTopo.pack()
        self.frameBase.pack()

        #entra no mainloop
        self.janela.mainloop()

def main():
    MyGui()

main()

