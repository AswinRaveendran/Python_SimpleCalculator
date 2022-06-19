from tkinter import *


def click(event):
    global Scvalue
    text = event.widget.cget("text")
    if text == "=":
        if Scvalue.get().isdigit():
            value = float(Scvalue.get())
        else:
            try:
                value = eval(Scvalue.get())

            except Exception as e:
                print(e)
                value = "Error"

        Scvalue.set(value)
        display_label.update()

    elif text == "C":
        Scvalue.set("")
        display_label.update()
    elif text == "D\nE\nL":
        numLen = len(display_label.get())
        display_label.delete(numLen - 1, 'end')
        display_label.update()
    elif text == "Sq":
        value = float(Scvalue.get())
        Scvalue.set(value*value)
        display_label.update()
    elif text == "Rt":
        value = float(Scvalue.get())
        Scvalue.set(value**0.5)
        display_label.update()


    else:
        Scvalue.set(Scvalue.get() + text)
        display_label.update()


# creating main window configuration


main_window = Tk()
main_window.geometry("500x500")
main_window.title("Calculator")
main_window.iconbitmap("1.ico")
main_window.config(bg="black")
main_window.minsize(width=400, height=460)
main_window.maxsize(width=400, height=460)

# Set variable

Scvalue = StringVar()
Scvalue.set("")

# Adding frames to the window


display_frame = Frame(main_window, bg="pink", width=400, height=100, borderwidth=10, relief=GROOVE)
button_frame = Frame(main_window, bg="#862d2d", width=400, height=400, borderwidth=10, relief=GROOVE)

# Adding label to the frame

display_label = Entry(display_frame, bg="white", fg="red", borderwidth=10, width=300, justify="left",
                      text=Scvalue,
                      font=("helvetica", 16, "bold"))

# Adding buttons to the frame
button_dlt = Button(display_frame, bg="black", fg="magenta", text="D\nE\nL", relief=FLAT, padx=1, pady=1, width=1,
                    height=50, justify=CENTER,
                    font=("comicsansms", 15, "bold"))
button1 = Button(button_frame, bg="black", fg="white", text="1", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button2 = Button(button_frame, bg="black", fg="white", text="2", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button3 = Button(button_frame, bg="black", fg="white", text="3", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button4 = Button(button_frame, bg="black", fg="white", text="4", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button5 = Button(button_frame, bg="black", fg="white", text="5", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button6 = Button(button_frame, bg="black", fg="white", text="6", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button7 = Button(button_frame, bg="black", fg="white", text="7", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button8 = Button(button_frame, bg="black", fg="white", text="8", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button9 = Button(button_frame, bg="black", fg="white", text="9", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button0 = Button(button_frame, bg="black", fg="white", text="0", padx=10, pady=10, relief=RAISED, borderwidth=10,
                 font=("comicsansms", 19, "bold"))
button_dot = Button(button_frame, bg="black", fg="white", text=".", padx=10, pady=10, relief=RAISED, borderwidth=10,
                    font=("comicsansms", 20, "bold"))
button_clr = Button(button_frame, bg="black", fg="white", text="C", padx=10, pady=10, relief=RAISED, borderwidth=10,
                    font=("comicsansms", 19, "bold"))
button_add = Button(button_frame, bg="black", fg="white", text="+", padx=10, pady=10, relief=RAISED, borderwidth=10,
                    font=("comicsansms", 19, "bold"))
button_minus = Button(button_frame, bg="black", fg="white", text="-", padx=10, pady=10, relief=RAISED, borderwidth=10,
                      font=("comicsansms", 22, "bold"))
button_mult = Button(button_frame, bg="black", fg="white", text="*", padx=10, pady=10, relief=RAISED, borderwidth=10,
                     font=("comicsansms", 19, "bold"))
button_div = Button(button_frame, bg="black", fg="white", text="/", padx=10, pady=10, relief=RAISED, borderwidth=10,
                    font=("comicsansms", 20, "bold"))
button_equal = Button(button_frame, bg="black", fg="white", text="=", padx=10, pady=10, relief=RAISED, borderwidth=10,
                      font=("comicsansms", 20, "bold"))
button_percent = Button(button_frame, bg="black", fg="white", text="%", padx=10, pady=10, relief=RAISED, borderwidth=10,
                        font=("comicsansms", 20, "bold"))
button_squre = Button(button_frame, bg="black", fg="white", text="Sq", padx=10, pady=10, relief=RAISED, borderwidth=10,
                      font=("comicsansms", 20, "bold"))
button_root = Button(button_frame, bg="black", fg="white", text="Rt", padx=10, pady=10, relief=RAISED, borderwidth=10,
                     font=("comicsansms", 20, "bold"))

# Adding components to the main screen

button_dlt.pack(side="right", anchor="ne")
button_dlt.bind("<Button-1>", click)
display_label.pack(side="bottom", fill=Y, ipady=12)
button_frame.pack(side="bottom", fill="x")

button7.grid(row=0, column=0)
button7.bind("<Button-1>", click)
button8.grid(row=0, column=1)
button8.bind("<Button-1>", click)
button9.grid(row=0, column=2)
button9.bind("<Button-1>", click)
button_add.grid(row=0, column=3)
button_add.bind("<Button-1>", click)
button_equal.grid(row=0, column=4)
button_equal.bind("<Button-1>", click)
button4.grid(row=1, column=0)
button4.bind("<Button-1>", click)
button5.grid(row=1, column=1)
button5.bind("<Button-1>", click)
button6.grid(row=1, column=2)
button6.bind("<Button-1>", click)
button_minus.grid(row=1, column=3)
button_minus.bind("<Button-1>", click)
button_percent.grid(row=1, column=4)
button_percent.bind("<Button-1>", click)
button1.grid(row=2, column=0)
button1.bind("<Button-1>", click)
button2.grid(row=2, column=1)
button2.bind("<Button-1>", click)
button3.grid(row=2, column=2)
button3.bind("<Button-1>", click)
button_mult.grid(row=2, column=3)
button_mult.bind("<Button-1>", click)
button_squre.grid(row=2, column=4)
button_squre.bind("<Button-1>", click)
button_dot.grid(row=3, column=0)
button_dot.bind("<Button-1>", click)
button0.grid(row=3, column=1)
button0.bind("<Button-1>", click)
button_clr.grid(row=3, column=2)
button_clr.bind("<Button-1>", click)
button_div.grid(row=3, column=3)
button_div.bind("<Button-1>", click)
button_root.grid(row=3, column=4)
button_root.bind("<Button-1>", click)

display_frame.pack(side=TOP, fill="x")

main_window.mainloop()
