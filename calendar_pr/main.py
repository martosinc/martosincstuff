from tkinter import *
import calendar
from calendar import day_abbr,datetime
from datetime import *

t = Tk()
t.title('Calendar')
t.geometry('460x380')
now = datetime.now()
back = Button(text="<",font='Arial 14')
forward = Button(text=">",font='Arial 14')
month = Label(text=calendar.month_name[now.month]+','+str(now.year),font='Arial 20')
week_day,month_days = calendar.monthrange(now.year,now.month)
column = 0
for i in range(0,7):
    day = day_abbr[i]
    btn = Label(text=day,font='Arial 14')
    btn.grid(row=1,column=column,ipadx=5,ipady=5)
    column += 1
days = []
row = 2
column = 0
for i in range(42):
    lab = Label(text="0",font='Arial 12')
    lab.grid(row=row,column=column,ipadx=22,ipady=10)
    days.append(lab)
    column += 1
    if column == 7:
        row+=1
        column=0
for i in range(month_days):
    if len(str(i+1)) == 2:
        days[i+week_day]['text'] = i + 1
    else:
        days[i+week_day]['text'] = '0' + str(i+1) 
    days[i+week_day]['fg'] = 'black'
    days[i+week_day]['bg'] = '#a0a0a0'
    if now.day == i:
        days[i-1+week_day]['bg'] = 'red'
if now.month != 1:
    prew_week_day,prew_month_days = calendar.monthrange(now.year,now.month-1)
else:
    prew_week_day,prew_month_days = calendar.monthrange(now.year-1,1)
for i in range(prew_month_days):
    if len(str(i-1)) == 2:
        days[prew_week_day-i]['text'] = prew_month_days-i
    else:
        days[prew_week_day-i]['text'] = str(prew_month_days-i) 
    days[prew_week_day-i]['fg'] = '#a0a0a0'
    days[prew_week_day-i]['bg'] = '#B9B9B9'
    if now.day == i:
        days[i-1+week_day]['bg'] = 'red'
back.grid(row=0,column=0,sticky='NW',ipadx=5,ipady=5,padx=5,pady=5)
month.grid(row=0,column=1,columnspan=5,sticky='N',ipadx=5,ipady=5,padx=5,pady=5)
forward.grid(row=0,column=6,sticky='NE',ipadx=5,ipady=5,padx=5,pady=5)

t.mainloop()