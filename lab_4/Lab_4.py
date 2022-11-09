import tkinter as tk
from genErator import give_a_cell
import time
from playsound import playsound
from tkinter.ttk import *
from tkinter import *


def gen_key():
    key_frame.delete(0, 100)
    Progress_Bar['value'] = 20
    window.update_idletasks()
    key_frame.insert(20, give_a_cell())
    time.sleep(1)
    Progress_Bar['value'] = 50
    key_frame.insert(20, '-')
    window.update_idletasks()
    time.sleep(1)
    key_frame.insert(20, give_a_cell())
    Progress_Bar['value'] = 80
    window.update_idletasks()
    time.sleep(1)
    Progress_Bar['value'] = 90
    key_frame.insert(20, '-')
    window.update_idletasks()
    time.sleep(1)
    key_frame.insert(20, give_a_cell())
    Progress_Bar['value'] = 100
    for i in range(4):
        Progress_Bar['value'] = 100
        window.update_idletasks()
        time.sleep(0.5)
        Progress_Bar['value'] = 0
        window.update_idletasks()
        time.sleep(0.5)


def close():
    window.destroy()


def play():
    playsound("amb.mp3")


window = tk.Tk()
window.title('Генератор ключей SCII')
window.geometry('500x170')
bg = tk.PhotoImage(file='bg_4.png')

frame = tk.Frame(window)
frame.place(relx=0.5, rely=0.5, anchor='c')

lab_bg = tk.Label(frame, image=bg)
lab_bg.place(x=0, y=0)

play()

lbl_title = tk.Label(frame, text='Генератор ключей SCII', font=('Times new Roman', 17))
lbl_title.grid(column=1, row=0, padx=10, pady=20)
key_frame = tk.Entry(frame, width=30, font=('Times new Roman', 17))
key_frame.insert(0, '')
key_frame.grid(column=1, row=1, padx=10, pady=20)
Progress_Bar = Progressbar(frame, orient=HORIZONTAL, length=250, mode='determinate')
Progress_Bar.place(anchor="c")
Progress_Bar.grid(row=3, column=1)

btn = tk.Button(frame, text='Generate', font=('Times new Roman', 15), command=gen_key)
btn.grid(column=0, row=3)
ex = tk.Button(frame, text='Cancel', font=('Times new Roman', 15), command=close)
ex.grid(column=2, row=3)

window.mainloop()
