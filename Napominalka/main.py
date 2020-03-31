from tkinter import *
from dictionary import words
import random
t = Tk()
t.geometry("225x300")
t.resizable(0,0)
t.title("Learning English")

menu1 = Button(text="Can you translate?\nENG-RUS", width=300, height=7, command=lambda:startLevel('eng'))
menu2 = Button(text="Can you translate?\nRUS-ENG", width=300, height=7, command=lambda:startLevel('rus'))
rus_words = words
eng_words = dict([[f,s] for s, f in words.items()])

def startLevel(lang):
    hidemenu()
    word = chooseword(lang)
    label1 = Label(t, text=word, font='Arial 20')
    label1.grid(columnspan=5,sticky='ew')
    if lang == 'eng':
        randomletters = [random.choice('abcdefghijklmnopqrstuvwxyz') for i in range(25 - len(word))]
    if lang == 'rus':
        randomletters = [random.choice('абвгдеёжзийклмнопрстуфхцчшщъыьэюя') for i in range(25 - len(word))]
    letters = list([i for i in word]) + randomletters
    letters = random.sample(letters, len(letters))
    buttons =[]
    column = 0
    row = 1

    for i in range(0, len(letters)):
        buttons.append(Button(t, text=letters[i],width=5))
        buttons[i].grid(column=column, row=row,sticky='ew')
        column += 1
        if column > 4:
            column = 0
            row += 1
    label2 = Label(t,text='',font='Arial 20')
    label2.grid(columnspan=5,sticky='ewsn')
def chooseword(lang):
    if lang == 'rus':
        global russian
        russian = list(rus_words.values())
        return random.choice(russian)
    if lang == 'eng':
        global english
        english = list(eng_words.values())
        return random.choice(english)
def showmenu():
    menu1.pack()
    menu2.pack()
def hidemenu():
    menu1.pack_forget()
    menu2.pack_forget()

showmenu()    

t.mainloop()