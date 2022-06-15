from tkinter import *

window = Tk()
window.geometry("500x500")
window.title("Calculator")
window.maxsize(width=500, height=500)
window.minsize(width=500, height=500)
label = Label(window, width=200, height=10, bg="red", fg="blue", text="Welcome to calculator")
window.config(bg="gray")
display = Entry(window)

label.grid(row=0 )


def hai():
    print("hello")


button1 = Button(text="Hai", width=5, height=2, command=hai)
button2 = Button(text="Hai", width=5, height=2, command=hai, fg="red")
button1.grid(row=5, column=2)
button2.grid(row=5, column=3)

window.mainloop()
