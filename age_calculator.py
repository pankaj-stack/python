#Age calculator
from tkinter import *
from datetime import date
import datetime
import time
win=Tk()
def upcoming_birthdays():
    #button=Button(win,width=50,text='UPCOMING BIRTHDAYS',fg='white',bg='blue')
    #button.grid(row=2,column=8)
    y=date.today()
    year1,month1,day1=str(y).split('-')
    year1=int(year1)
    day_name=['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
    list1=list(range(7))
    for i in range(7):
        button=Button(win,width=50,text=f'{year1} {month1} {day1}----->',bg='red',fg='white')
        button.grid(row=i+9,column=2)
        year1+=1
    for i in range(7):
        year_var=year1
        x=datetime.datetime(year1,int(month1),int(day1)).weekday()
        if x in list1:
            #print(day_name[x])
            button=Button(win,width=50,text=f'---------------------->{day_name[x]}',bg='green',fg='white')
            button.grid(row=i+16,column=3)
            year1+=1
    
def calculate():
    print('hello')
    dobs=dob.get()
    day,month,year=dobs.split()
    #print(day,month,year)
    day,month,year=int(day),int(month),int(year)
    month,year=month*30,year*365
    past_days=day+month+year
    #print(f'past days{past_days}' )
    y,m,d=str(date.today()).split('-')
    d,m,y=int(d),int(m),int(y)
    m,y=m*30,y*365
    current_days=d+m+y
    #print(f'current days {current_days}' )
    days=current_days-past_days
    #print(days)
    #print(days//365)
    years,months,days=int(days/365),int((days%365)/30),((days%365)%30)
    weeks,hours,minutes,seconds=days//7,days*24,days*24*60,days*24*60*60
    print('years :',years,'\nmonth :',months,'\ndays  :',days)
    l=['YEARS : ','MONTHS : ','DAYS : ','WEEKS : ','HOURS : ','MINUTES : '
       ,'SECONDS : ']
    l1=[years,months,days,weeks,hours,minutes,seconds]
    for i in range(7):
        button=Button(win,width=50,bg='red',fg='white',text=f'{l[i]}{l1[i]}' )
        button.grid(row=i+2,column=1)
    upcoming_birthdays()
dob=StringVar()
dob=Entry(win,width=54,textvariable=dob)
dob.grid(row=0,column=0)
button=Button(win,width=50,text='CALCULATE',fg='white',bg='blue',command=calculate)
button.grid(row=1,column=0)
win.geometry('1250x750')
win.configure(background='yellow')
win.mainloop()
