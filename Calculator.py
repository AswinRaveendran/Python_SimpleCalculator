from tkinter import *

# creating main window configuration


main_window = Tk()
main_window.geometry("500x500")
main_window.title("Calculator")
main_window.config(bg="black")
main_window.minsize(width=300, height=460)
main_window.maxsize(width=300, height=460)

# Adding frames to the window

display_frame = Frame(main_window, bg="gray", width=400, height=100, borderwidth=10, relief=GROOVE)
button_frame = Frame(main_window, bg="black", width=400, height=400, borderwidth=10, relief=GROOVE)

# Adding label to the frame

display_label = Label(display_frame, bg="white", fg="red", borderwidth=10, width=300, height=100, text="welcome",
                      font=("helvetica", 16, "bold"))

# Adding buttons to the frame
button_dlt = Button(display_frame, bg="gray", fg="black", text="D\nE\nL", relief=FLAT, padx=1, pady=1,width=1, height=50, justify=CENTER,
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
                    font=("comicsansms", 19, "bold"))
button_clr = Button(button_frame, bg="black", fg="white", text="C", padx=10, pady=10, relief=RAISED, borderwidth=10,
                    font=("comicsansms", 19, "bold"))
button_add = Button(button_frame, bg="black", fg="white", text="+", padx=10, pady=10, relief=RAISED, borderwidth=10,
                    font=("comicsansms", 19, "bold"))
button_minus = Button(button_frame, bg="black", fg="white", text="-", padx=10, pady=10, relief=RAISED, borderwidth=10,
                      font=("comicsansms", 19, "bold"))
button_mult = Button(button_frame, bg="black", fg="white", text="x", padx=10, pady=10, relief=RAISED, borderwidth=10,
                     font=("comicsansms", 19, "bold"))
button_div = Button(button_frame, bg="black", fg="white", text="/", padx=10, pady=10, relief=RAISED, borderwidth=10,
                    font=("comicsansms", 19, "bold"))

# Adding components to the main screen

button_dlt.pack(side="right", anchor="ne")
display_label.pack(side="bottom", anchor="sw", fill=X)
button_frame.pack(side="bottom", fill="x")

button7.grid(row=0, column=0)
button8.grid(row=0, column=1)
button9.grid(row=0, column=2)
button_add.grid(row=0, column=3)
button4.grid(row=1, column=0)
button5.grid(row=1, column=1)
button6.grid(row=1, column=2)
button_minus.grid(row=1, column=3)
button1.grid(row=2, column=0)
button2.grid(row=2, column=1)
button3.grid(row=2, column=2)
button_mult.grid(row=2, column=3)
button_dot.grid(row=3, column=0)
button0.grid(row=3, column=1)
button_clr.grid(row=3, column=2)
button_div.grid(row=3, column=3)


display_frame.pack(side=TOP, fill="x")

main_window.mainloop()
