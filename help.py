# @Author: Sebastian Sanchez Bentolila - https://github.com/Sebastian-Sanchez-Bentolila

#Modules
import os
from tkinter import *

#Paragraph 
ayuda = '''Ayuda
*****

-¿Por què es bueno tener una contraseña segura?

Las contraseñas son una forma de autenticaciòn
que usa informaciòn secreta para controlar el 
acceso a algun recurso (ejemplo a los 
dispositivos, nuetras comunicaciones, 
billetera virtual, etc). 

Si esta clave de acceso es relativamente fàcil
te vuelve vulnerable para los cìbercriminales,
quienes pueden robarte tu informaciòn.

-¿Còmo copiar y pegar la clave?

Ctrl+C = Copiar
Ctrl+V = Pegar
Ctrl+X = Cortar
'''

class Ayuda():
    def __init__(self):
        #Configuration of the 'Help' window
        self.ayuda = Tk()
        self.ayuda.geometry('270x320')
        self.ayuda.title('Ayuda')
        self.ayuda.resizable(0, 0)
        self.Ruta_Trabajo = os.getcwd()
        self.ayuda.iconbitmap('{}\\icons\\help.ico'.format(self.Ruta_Trabajo))
        self.ayuda.config(bg='white', cursor='arrow')
        self.Widgets()
    
    def Widgets(self):
        #Label
        self.lblayuda = Label(self.ayuda, text=ayuda)
        self.lblayuda.config(bg='white', fg='black', justify=LEFT, font='Times 10')
        self.lblayuda.grid(row=1, column=1)
        
    def RunApp(self):
        self.ayuda.mainloop()
        
