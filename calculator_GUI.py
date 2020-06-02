from tkinter import *
import math
import statistics
from numpy import mean, absolute
# pi, e has 11 digits after decimal point
"""
def factorial(number):
    if number < 0:
        print("factorial is undefined for negative numbers!")
        return None
    if number == 1 or number == 0:
        return 1
    else:
        return number*factorial(number-1)
"""


def add_num(number):
    current = e.get()
    e.delete(0, END)
    e.insert(0, str(current) + str(number))
def clear():
    e.delete(0, END)
def clearstate():
    global state
    state = 100
    e.delete(0, END)
def plus():
    global prev, state
    state = 1
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    prev = float(cur)
    e2.delete(0, END)
    e2.insert(0, "+")
    e.delete(0, END)
def minus():
    global prev, state
    state = 2
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    prev = float(cur)
    e2.delete(0, END)
    e2.insert(0, "-")
    e.delete(0, END)
def div():
    global prev, state
    state = 3
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    prev = float(cur)
    e2.delete(0, END)
    e2.insert(0, "/")
    e.delete(0, END)
def mult():
    global prev, state
    state = 4
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    prev = float(cur)
    e2.delete(0, END)
    e2.insert(0, "x")
    e.delete(0, END)
def equals():
    cur = float(e.get())
    if state == 1:
        res = cur + prev
    if state == 2:
        res = prev - cur
    if state == 3:
        res = prev / cur
    if state == 4:
        res = prev * cur
    if state == 5:
    ### change this ###
        res = math.pow(prev, cur)
    ###
    if state == 100:   # do nothing if state not changed
        return
    e.delete(0, END)
    res = round(res, 9)
    e2.delete(0, END)
    e2.insert(0, ":)")
    e.insert(0, str(res))

########################## functions ##########################
def sine():
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    cur = float(cur)
    ### change this ###
    res = math.sin(cur)
    ###
    res = round(res, 9)
    e.delete(0, END)
    e2.delete(0, END)
    e2.insert(0, ":)")
    e.insert(0, res)
def power():
    global prev, state
    state = 5
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    prev = float(cur)
    e2.delete(0, END)
    e2.insert(0, "^")
    e.delete(0, END)
def ln():
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    cur = float(cur)
    ### change this ###
    res = math.log(cur)
    ###
    res = round(res, 9)
    e.delete(0, END)
    e2.delete(0, END)
    e2.insert(0, ":)")
    e.insert(0, res)
def cosh():
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a number first")
        return
    cur = float(cur)
    ### change this ###
    res = math.cosh(cur)
    ###
    res = round(res, 9)
    e.delete(0, END)
    e2.delete(0, END)
    e2.insert(0, ":)")
    e.insert(0, res)
def mad():
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a list of number separated by comma")
        return
    string = cur.split(",")
    data = []
    for i in string:
        if i == "":
            continue
        i = float(i)
        data.append(i)
    e.delete(0, END)
    ### change this ###
    ### data is the list of data
    res = mean(absolute(data - mean(data)))
    ###
    e2.delete(0, END)
    e2.insert(0, ":)")
    e.insert(0, res)
def std():
    cur = e.get()
    if cur == "":
        e2.delete(0, END)
        e2.insert(0, "type in a list of number separated by comma")
        return
    res = cur.split(",")
    l = []
    for i in res:
        if i == "":
            continue
        i = float(i)
        l.append(i)
    e.delete(0, END)
    ### change this ###
    ### l is the list of data
    stdev = statistics.stdev(l)
    ###
    e2.delete(0, END)
    e2.insert(0, ":)")
    e.insert(0, stdev)
###############################################################

state = 100
prev = 0
root = Tk()
root.title("Calculator")
root.geometry("570x325")

e = Entry(root, width=31, font=("helvetica", 32), justify=RIGHT)
e.grid(row=0, columnspan=7)
e2 = Entry(root, width=62, font=("helvetica", 15), justify=RIGHT)
e2.grid(row=1, columnspan=7)
e2.insert(0, ":)")
# buttons
# row 1
button1_1 = Button(root, text="sin", padx=30, pady=20, command=sine)
button1_1.grid(row=2, column=0)
button1_2 = Button(root, text="x^y", padx=30, pady=20, command=power)
button1_2.grid(row=2, column=1)
button1_3 = Button(root, text="1", padx=30, pady=20, command=lambda: add_num("1"))
button1_3.grid(row=2, column=2)
button1_4 = Button(root, text="2", padx=30, pady=20, command=lambda: add_num("2"))
button1_4.grid(row=2, column=3)
button1_5 = Button(root, text="3", padx=30, pady=20, command=lambda: add_num("3"))
button1_5.grid(row=2, column=4)
button1_6 = Button(root, text="+", padx=30, pady=20, command=plus)
button1_6.grid(row=2, column=5)
button1_7 = Button(root, text="nf", padx=30, pady=20)
button1_7.grid(row=2, column=6)
# row 2
button2_1 = Button(root, text="ln", padx=30, pady=20, command=ln)
button2_1.grid(row=3, column=0)
button2_2 = Button(root, text="MAD", padx=30, pady=20, command=mad)
button2_2.grid(row=3, column=1)
button2_3 = Button(root, text="4", padx=30, pady=20, command=lambda: add_num("4"))
button2_3.grid(row=3, column=2)
button2_4 = Button(root, text="5", padx=30, pady=20, command=lambda: add_num("5"))
button2_4.grid(row=3, column=3)
button2_5 = Button(root, text="6", padx=30, pady=20, command=lambda: add_num("6"))
button2_5.grid(row=3, column=4)
button2_6 = Button(root, text="-", padx=30, pady=20, command=minus)
button2_6.grid(row=3, column=5)
button2_7 = Button(root, text=",", padx=30, pady=20, command=lambda: add_num(","))
button2_7.grid(row=3, column=6)
# row 3
button3_1 = Button(root, text="StD", padx=30, pady=20, command=std)
button3_1.grid(row=4, column=0)
button3_2 = Button(root, text="cosh", padx=30, pady=20, command=cosh)
button3_2.grid(row=4, column=1)
button3_3 = Button(root, text="7", padx=30, pady=20, command=lambda: add_num("7"))
button3_3.grid(row=4, column=2)
button3_4 = Button(root, text="8", padx=30, pady=20, command=lambda: add_num("8"))
button3_4.grid(row=4, column=3)
button3_5 = Button(root, text="9", padx=30, pady=20, command=lambda: add_num("9"))
button3_5.grid(row=4, column=4)
button3_6 = Button(root, text="x", padx=30, pady=20, command=mult)
button3_6.grid(row=4, column=5)
button3_7 = Button(root, text="CE", padx=30, pady=20, command=clearstate)
button3_7.grid(row=4, column=6)
# row 4
button4_1 = Button(root, text="pi", padx=30, pady=20, command=lambda: add_num(3.14159265359))
button4_1.grid(row=5, column=0)
button4_2 = Button(root, text="e", padx=30, pady=20, command=lambda: add_num(2.71828182846))
button4_2.grid(row=5, column=1)
button4_3 = Button(root, text="0", padx=30, pady=20, command=lambda: add_num("0"))
button4_3.grid(row=5, column=2)
button4_4 = Button(root, text="=", padx=30, pady=20, command=equals)
button4_4.grid(row=5, column=3)
button4_5 = Button(root, text="C", padx=30, pady=20, command=clear)
button4_5.grid(row=5, column=4)
button4_6 = Button(root, text="/", padx=30, pady=20, command=div)
button4_6.grid(row=5, column=5)
button4_7 = Button(root, text=".", padx=30, pady=20, command=lambda: add_num("."))
button4_7.grid(row=5, column=6)

root.mainloop()
