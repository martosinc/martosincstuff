from tkinter import *
import hashlib
from tkinter import messagebox
t = Tk()
t.geometry('275x500')

# Registration
def regdraw():
    reglabel = Label(text='Регистрация:')
    reguserlabel = Label(text='Логин:')
    reguser = Entry()
    regpasswordlabel = Label(text='Пароль')
    regpassword = Entry()
    def save():
        if len(regpassword.get()) >= 8:
            if regpassword.get().count(' ') < 1:
                f = open('/home/martos/Documents/code/python/User/users.txt', 'a')
                hashpass = hashlib.sha1(f'{regpassword.get()}'.encode('utf-8')).hexdigest()
                f.write(f'{reguser.get()}\n{hashpass}\n')
                f.close()
            else:
                messagebox.showerror('Ошибка!', 'Пароль не должен содержать пробелов')
        else:
            messagebox.showerror('Ошибка!', 'Длина пароля должна составлять не меньше 8 цифр')
    regbtn = Button(text='Зарегистрироваться', command=save)
    reglabel.pack()
    reguserlabel.pack()
    reguser.pack()
    regpasswordlabel.pack()
    regpassword.pack()
    regbtn.pack()
# pickle dump
#Login
def logindraw():
    loglabel = Label(text='Вход:')
    loguserlabel = Label(text='Логин:')
    loguser = Entry()
    logpasswordlabel = Label(text='Пароль:')
    logpassword = Entry(show='*')
    def login():
        f = open('/home/martos/Documents/code/python/User/users.txt', 'r')
        lines = f.readlines()
        lindex = 0 # Index of a line
        loginpass = False
        passpass = False
        for i in lines:
            i = i.replace('\n', '')
            if i == loguser.get():
                loginpass = True
                hashpassuser = hashlib.sha1(f'{logpassword.get()}'.encode('utf-8')).hexdigest()
                datapass = (lines[lindex+1]).replace('\n', '')
                if datapass == hashpassuser:
                    passpass = True
                    messagebox.showinfo('', 'Вход прошёл успешно!')
            lindex += 1
        if loginpass == False or passpass == False:
            messagebox.showerror('Error!', 'Неверный логин или пароль!')
        f.close()
    logbutton = Button(text='Войти', command=login)
    loglabel.pack()
    loguserlabel.pack()
    loguser.pack()
    logpasswordlabel.pack()
    logpassword.pack()
    logbutton.pack()
regdraw()
logindraw()
t.mainloop()
