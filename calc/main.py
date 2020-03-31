from tkinter import *
t = Tk()
t.title('calculator')
t.geometry('350x630')

result = Entry(font='Ubuntu 15', width="27")
result.grid(columnspan=49,row=0)

def clear():
    result.delete(0, END)

def delete():
    result.delete(len(result.get())-1,END)

def execute(digit):
    result.insert(END, digit)

def calculate():
    try:
        calcing = eval(result.get())
        result.delete(0, END)
        if type(calcing) == float:
            if calcing == int(calcing): # Example: if 3.0 == 3
                calcing = int(calcing)
        result.insert(0, calcing)
    except SyntaxError:
        calcingchange = result.get()
        calcingchange = calcingchange.replace('+', ' + ')
        calcingchange = calcingchange.replace('-', ' - ')
        calcingchange = calcingchange.replace('*', ' * ')
        calcingchange = calcingchange.replace('/', ' / ')
        calcingchange = calcingchange.replace('(', ' ( ')
        calcingchange = calcingchange.replace(')', ' ) ')
        calcingchange = calcingchange.split(' ')
        for i in calcingchange:
            if len(i) > 1:
                if i[0:1] == '0' and i[1:2] != '.':
                    if i.count('0') == len(i):
                        calcingchange[calcingchange.index(i)] = '0'
                        continue
                    digit0 = True # if the digit is equal to 0
                    digitindex = 0 # index of the digit
                    count0 = 0 # how many 0 are in the string
                    while digit0 == True:
                        if i[digitindex] == '0':
                            digitindex+=1
                            count0 += 1
                        else:
                            digit0 = False
                    calcingchange[calcingchange.index(i)] = i.replace('0', '', count0)
        calcingchange = ''.join(calcingchange)
        calcingchange = calcingchange.replace(' ', '')
        result.delete(0, END)
        calcingchangecalcing = eval(calcingchange)
        if type(calcingchangecalcing) == float:
            if calcingchangecalcing == int(calcingchangecalcing): # Example: if 3.0 == 3
                calcingchangecalcing = int(calcingchangecalcing)
        result.insert(0, calcingchangecalcing)

def calculatebind(event):
    try:
        calcing = eval(result.get())
        result.delete(0, END)
        if type(calcing) == float:
            if calcing == int(calcing): # Example: if 3.0 == 3
                calcing = int(calcing)
        result.insert(0, calcing)
    except SyntaxError:
        calcingchange = result.get()
        calcingchange = calcingchange.replace('+', ' + ')
        calcingchange = calcingchange.replace('-', ' - ')
        calcingchange = calcingchange.replace('*', ' * ')
        calcingchange = calcingchange.replace('/', ' / ')
        calcingchange = calcingchange.replace('(', ' ( ')
        calcingchange = calcingchange.replace(')', ' ) ')
        calcingchange = calcingchange.split(' ')
        for i in calcingchange:
            if len(i) > 1:
                if i[0:1] == '0' and i[1:2] != '.':
                    if i.count('0') == len(i):
                        calcingchange[calcingchange.index(i)] = '0'
                        continue
                    digit0 = True # if the digit is equal to 0
                    digitindex = 0 # index of the digit
                    count0 = 0 # how many 0 are in the string
                    while digit0 == True:
                        if i[digitindex] == '0':
                            digitindex+=1
                            count0 += 1
                        else:
                            digit0 = False
                    calcingchange[calcingchange.index(i)] = i.replace('0', '', count0)
        calcingchange = ''.join(calcingchange)
        calcingchange = calcingchange.replace(' ', '')
        result.delete(0, END)
        calcingchangecalcing = eval(calcingchange)
        if type(calcingchangecalcing) == float:
            if calcingchangecalcing == int(calcingchangecalcing): # Example: if 3.0 == 3
                calcingchangecalcing = int(calcingchangecalcing)
        result.insert(0, calcingchangecalcing)
symbols = ['0','1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '-', '*', '/', '(', ')'] # labels of buttons ⇐
for i in symbols:
    indexofi = symbols.index(i)
    buttonrow = (indexofi+1)//3+1
    buttoncolumn = (indexofi+1)%3-1
    if (indexofi+1)%3==0:
        buttonrow-=1
        buttoncolumn+=3
    symbols[indexofi] = Button(width='11', height='5',text=symbols[indexofi], bg='#CCCCCC', command=lambda x=symbols[indexofi]: execute(x))
    symbols[indexofi].grid(row=buttonrow, column=buttoncolumn)

clearbutton = Button(text='C', width='11', height='5', command=clear)
clearbutton.grid(row=6, column=1)

deletebutton = Button(text='⇐', width=11, height=5, command=delete)
deletebutton.grid(row=6, column=2)

calculate = Button(text='=', width='40', height=3, command=calculate)
calculate.grid(columnspan=4, row=7)

t.bind('<Return>', calculatebind)

t.mainloop()