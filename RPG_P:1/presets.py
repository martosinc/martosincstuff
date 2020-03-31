from tkinter import *
t = Tk()
t.title('Загатовка')
t.geometry('250x250')
t.resizable(0,0)
job = ''
class Hero:
    def __init__(self):
        self.health = 50
        self.mana = 100
        self.strength = 25
hero = Hero()
t.mainloop()