from tkinter import *
import tkinter.messagebox as tmsg
import os
import csv

def submit1(x):

    with open("tkinter_trackRating.csv", 'r') as f:
        reader = csv.reader(f)
        data = list(reader)

    data[x.get()][0] = int(data[x.get()][0]) + 1

    with open("tkinter_trackRating.csv", 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

    x.set(5)

root =Tk()
root.geometry("500x300")
root.title("Give Rating to me --using tkinter_practise")

Label(root, text="How much rating will you give to me?",font=("Arial", 14, "bold"),padx=5,pady=5, height=2,bg="lightblue",justify=CENTER ).pack()
myslider2 = Scale(root, from_=0, to=10, orient=HORIZONTAL, tickinterval=5,width=15,sliderlength=25,length=250,highlightbackground="#B87333",background="#F8F5E1")
myslider2.set(5)
myslider2.pack(pady=35)

Button(root, text="Rate me!", pady=10, command=lambda : submit1(myslider2),bg = "yellow").pack()

root.mainloop()