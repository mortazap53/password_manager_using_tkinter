from tkinter import *

window = Tk()
window.title("Password Manager")
window.configure(padx=50, pady=50, bg="white")

canvas = Canvas(window, width=200, height=200, bg="white", highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
website_entry = Entry(width=46, bg="white")
website_entry.focus_set()
website_entry.grid(row=1, column=1, columnspan=2)

window.mainloop()