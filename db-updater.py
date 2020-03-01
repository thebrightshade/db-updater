"""
A program that stores DEVICE ID, ADB ID, 
CARRIER, PH.NUMBER, 
CALL TO/MT, BUILD ID, 
SCENARIO, MARKET, TESTER NAME
into a database.csv file 

User can:
View, 
Search,
Add,
Modify
and delete records
"""

from tkinter import *
import backend
import pandas


def get_selected_row(event):
    index=list1.curselection()[0]
    global selected_tuple
    selected_tuple=list1.get(index)
    e1.delete(0,END)
    e1.insert(END,selected_tuple[1])
    e2.delete(0,END)
    e2.insert(END,selected_tuple[0])
    e3.delete(0,END)
    e3.insert(END,selected_tuple[2])
    e4.delete(0,END)
    e4.insert(END,selected_tuple[3])
    e5.delete(0,END)
    e5.insert(END,selected_tuple[4])
    e6.delete(0,END)
    e6.insert(END,selected_tuple[5])
    e7.delete(0,END)
    e7.insert(END,selected_tuple[6])
    e8.delete(0,END)
    e8.insert(END,selected_tuple[7])
    e9.delete(0,END)
    e9.insert(END,selected_tuple[8])


def view_command():
    list1.delete(0,END)
    for row in backend.view().reset_index().values:
        list1.insert(END,tuple(row))


def modify_command():
    backend.update(device_text.get(),
                    adb_text.get(),
                    carrier_text.get(),
                    phone_text.get(),
                    callto_text.get(),
                    build_text.get(),
                    scenario_text.get(),
                    market_text.get(),
                    tester_text.get())
    view_command()


def delete_command():
    backend.delete(selected_tuple[0])
    view_command()


window = Tk()
window.title("CRASH PROCESSOR")
l1 = Label(window, text="DEVICE ID")
l1.grid(row=0,column=0,sticky=W)
l2 = Label(window, text="ADB ID")
l2.grid(row=0,column=2,sticky=W)
l3 = Label(window, text="CARRIER")
l3.grid(row=0,column=4,sticky=W)
l4 = Label(window, text="PH. NUMBER")
l4.grid(row=0,column=6,sticky=W)
l5 = Label(window, text="CALL TO NO.")
l5.grid(row=1,column=0,sticky=W)
l6 = Label(window, text="BUILD ID")
l6.grid(row=1,column=2,sticky=W)
l7 = Label(window, text="SCENARIO")
l7.grid(row=2,column=0,sticky=W)
l8 = Label(window, text="MARKET")
l8.grid(row=2,column=2,sticky=W)
l9 = Label(window, text="TESTER NAME")
l9.grid(row=2,column=4,sticky=W)

device_text=StringVar()
e1=Entry(window,textvariable=device_text)
e1.grid(row=0,column=1)

adb_text=StringVar()
e2=Entry(window,textvariable=adb_text)
e2.grid(row=0,column=3)

carrier_text=StringVar()
e3=Entry(window,textvariable=carrier_text)
e3.grid(row=0,column=5)

phone_text=StringVar()
e4=Entry(window,textvariable=phone_text)
e4.grid(row=0,column=7)

callto_text=StringVar()
e5=Entry(window,textvariable=callto_text)
e5.grid(row=1,column=1)

build_text=StringVar()
e6=Entry(window,textvariable=build_text)
e6.grid(row=1,column=3,columnspan=5, sticky=EW)

scenario_text=StringVar()
e7=Entry(window,textvariable=scenario_text)
e7.grid(row=2,column=1)

market_text=StringVar()
e8=Entry(window,textvariable=market_text)
e8.grid(row=2,column=3)

tester_text=StringVar()
e9=Entry(window,textvariable=tester_text)
e9.grid(row=2,column=5)

list1=Listbox(window)
list1.grid(row=4,column=0,rowspan=6,columnspan=8,sticky=EW)

sb1=Scrollbar(window)
sb1.grid(row=4,column=8,rowspan=6)

list1.configure(yscrollcommand=sb1.set)
sb1.configure(command=list1.yview)

list1.bind('<<ListboxSelect>>',get_selected_row)


b1=Button(window,text="View All",width=12,command=view_command)
b1.grid(row=3,column=0)
b2=Button(window,text="Add/Modify",width=12,command=modify_command)
b2.grid(row=3,column=1)
b5=Button(window,text="Delete",width=12,command=delete_command)
b5.grid(row=3,column=7)

l10 = Label(window, text="CRASH FOLDER")
l10.grid(row=10,column=0,sticky=W)

l11 = Label(window, text="MAGIC NUMBER/S")
l11.grid(row=10,column=3,sticky=W)

crash_path=StringVar()
e10=Entry(window,textvariable=crash_path)
e10.grid(row=10,column=1,columnspan=2,sticky=EW)

magic_num=StringVar()
e11=Entry(window,textvariable=magic_num)
e11.grid(row=10,column=4,columnspan=2,sticky=EW)

b6=Button(window,text="Rename Crashes",width=12)
b6.grid(row=10,column=6)

b7=Button(window,text="Crash Signature",width=12)
b7.grid(row=10,column=7)



window.mainloop()
