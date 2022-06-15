from tkinter import *

# creating main window configuration


main_window = Tk()
main_window.geometry("500x500")
main_window.title("Calculator")
main_window.config(bg="black")
main_window.minsize(width=500, height=500)
main_window.maxsize(width=500, height=500)

# Adding frames to the window

display_frame = Frame(main_window, bg="gray", width=400, height=100, borderwidth=10, relief=SUNKEN)
button_frame = Frame(main_window, bg="#261a0d", width=400, height=400, borderwidth=10, relief=SUNKEN)

button_frame.pack(side="bottom", fill="x")
display_frame.pack(side=TOP, fill="x")


main_window.mainloop()
