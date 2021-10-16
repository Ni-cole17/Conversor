from tkinter import *
from TkinterDnD2 import *
from tkinter import filedialog as fd
import os
from pathlib import Path
from tkinter.ttk import * 

root = Tk()
root.geometry("650x350")

def abrir():
    global namei
    root.filenames = fd.askopenfilenames(initialdir='/',title='Select the Files',filetypes=(('All files','*.*'),))
    namei = root.filenames
    
    

def selecionado(selection):
    global tipo_arquivo
    tipo_arquivo = selection

def converter():
    for i in namei:
        diretorio_atual = i
        name = os.path.split(diretorio_atual)
        os.chdir(name[0])
        p = Path(i)
        k = p.rename(p.with_suffix(tipo_arquivo))
        print(k)


st = Style()
st.configure('W.TButton', background='#345', foreground='black', font=('Arial', 14 ))

optionVar = StringVar()
optionVar.set("Selecione")
option = OptionMenu(root,optionVar,"Selecione",".wav",".mp3",".mp4",".pdf",".txt",".png",".jpg",command=selecionado)
Button_abrir = Button(root,text="Upload arquivos",command=abrir,style='W.TButton')
option
Button_converter = Button(root,text="Converter",command=converter,style='W.TButton')
Button_sair = Button(root,text="Sair",command=quit,style='W.TButton')

option['menu'].configure(font=('Arial',10))
option['width'] = 20

nome = Label(root,text="Conversor de arquivos",font=("Arial",20,"bold")).pack(pady=10)
Button_abrir.pack(pady=10)
nome = Label(root,text="Selecione o tipo de conversão",font=("Arial",10)).pack()
option.pack(pady=10)
Button_converter.pack()
Button_sair.pack(pady=30)
root.mainloop()