from tkinter import *

def btn_Click(message):
    print(message)

def Centralizar():
    #dimensoes da janela
    largura = 500
    altura = 500
    #pega as dimensoes do monitor
    largura_screen = window.winfo_screenwidth()
    altura_screen = window.winfo_screenheight()
    #posicao da janela
    posx=((largura_screen-largura)/2) 
    posy= (altura_screen-altura)/2
    return (largura,altura,posx,posy)

window = Tk()
window.title("My App")
label_1=Label(window,
            text= "Este é o label 1",bg="#ffaa00",fg="red",
            font="Times")
label_1.pack()


window.geometry("%dx%d+%d+%d"%Centralizar())
window.resizable(True,True)



# window.minsize(width= 500, height= 250)
# window.maxsize(700,400)
#window.state("iconic")
window.iconbitmap("Tkinter_test\Images\Icon.ico")

btn = Button(window, text="Exit", command = lambda : btn_Click("Olá mundo!"))
btn.pack()

window.mainloop()
 
