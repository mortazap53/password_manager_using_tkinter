from tkinter import *

window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50, bg="white")

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.pack()

window.mainloop()