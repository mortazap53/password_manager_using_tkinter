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

email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0)
email_entry = Entry(width=46, bg="white")
email_entry.insert(0, "mortazap53@gmail.com")
email_entry.grid(row=2, column=1, columnspan=2)

password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)
password_entry = Entry(width=28, bg="white")
password_entry.grid(row=3, column=1)

add_button = Button(text="Add", width=46, bg="white")
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate Password", bg="white")
generate_button.grid(row=3, column=2)

window.mainloop()