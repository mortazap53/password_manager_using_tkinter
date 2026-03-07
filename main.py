from tkinter import *
from tkinter import messagebox

Passwords = open("Passwords.txt", "a")

## Functions:
# Generating password:
# saving details to the file:
def saving_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message="These are details entered:\n"
                                                              f"Website: {website} \n Email: {email} \n Password: {password}")
        if is_ok:
            with open("passwords.txt", "a") as file:
                file.write(website + " | " + email + " | " + password + "\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)

## User interface:
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

add_button = Button(text="Add", width=46, bg="white", command=saving_data)
add_button.grid(row=4, column=1, columnspan=2)

generate_button = Button(text="Generate Password", bg="white")
generate_button.grid(row=3, column=2)

window.mainloop()