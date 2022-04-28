from tkinter import *

window = Tk()

window.title("Special Midterm Exam in OOP")
window.geometry("500x400+20+10")

btn: Button = Button(window, text='Click to Change Color', command=lambda:a(btn))

def a(btn):
    btn.configure(bg='yellow')

btn.pack()
btn.place(x=180,y=175)

window.mainloop()


