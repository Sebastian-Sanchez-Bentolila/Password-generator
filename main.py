# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

#Modules
import random
import os
from tkinter import *
from help import Ayuda

#Main Class
class GeneradorClaves:
    def __init__(self):
        #Main window settings
        self.ventana = Tk()
        self.ventana.geometry('640x360')
        self.ventana.title('Generador de Claves')
        self.ventana.resizable(0, 0)
        self.RutaTrabajo = os.getcwd()
        self.ventana.iconbitmap('{}\\icons\\hacker.ico'.format(self.RutaTrabajo))
        self.ventana.config(cursor='pirate')
        
        #Fondo
        self.fondo = PhotoImage(file='{}\\images\\skull.png'.format(self.RutaTrabajo))
        self.lblfondo = Label(self.ventana, image=self.fondo)
        self.lblfondo.pack()
        self.Widgets()
        
    def Widgets(self):
        #Label
        self.lbltitulo = Label(self.ventana, text='Generador de Contraseñas Seguras')
        self.lbltitulo.config(bg='light blue', fg='black', font='Consolas 12')
        self.lbltitulo.place(x=30, y=40, width=300, height=40) 

        #Entry
        self.lblgenerar = Entry(self.ventana)
        self.lblgenerar.config(bg='white', fg='black', font='Consolas 12')
        self.lblgenerar.place(x=130, y=180, width=200, height=30)
        
        #Buttons 
        self.btngenerar = Button(self.ventana, text='Generar', command= lambda: self.Generar())
        self.btngenerar.config(font='Consolas 10')
        self.btngenerar.place(x=184, y=220, width=100, height=20)
        
        self.ImAyuda = PhotoImage(file='{}\\images\\help.png'.format(self.RutaTrabajo))
        self.btnayuda = Button(self.ventana, text='Ayuda', command= lambda: Ayuda())
        self.btnayuda.config(image=self.ImAyuda, relief='flat')
        self.btnayuda.place(x=607, y=327, width=33, height=33)
        
    def RunApp(self):
        self.ventana.mainloop()
    
    def Generar(self):
        self.numeros = '0123456789'
        self.abecedario = 'abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXY'
        self.simbolos = '!#$%&()*+-./:;<=>?@[\]^_`{|}~'
        
        self.caracteres = self.numeros + self.abecedario + self.simbolos
        self.random = random.randint(12, 16)
        self.i = 0
        
        self.clave = "".join(random.choice(self.caracteres) for self.i in range(self.random))
        self.lblgenerar.delete(0, END)
        self.lblgenerar.insert(0, self.clave)


if __name__=='__main__':
    generador = GeneradorClaves().RunApp()
