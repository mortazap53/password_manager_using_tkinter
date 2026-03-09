from json import JSONDecodeError
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json

## Functions:
# Searching for the perviously saved passwords:
def searching():
    website = website_entry.get()
    try:
        with open("passwords.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showerror("Error",
                             message="There is no saved passwords file yet!")
    else:
        if website in data:
            email = data.get(website)["email"]
            password = data.get(website)["password"]
            messagebox.showinfo(title=website, message=f"Email: {email} \n Password: {password}")
        else:
            messagebox.showerror("Error", f"There is no saved passwords attached to this website: {website}")

# Generating password:
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
               'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '@', '#', '$', '%', '^', '&', '*']

    l_num = random.randint(8,10)
    n_num = random.randint(3,4)
    s_num = random.randint(3,4)

    password = ([random.choice(letters) for _ in range(l_num)]
                + [random.choice(numbers) for _ in range(n_num)]
                + [random.choice(symbols) for _ in range(s_num)])

    random.shuffle(password)
    password = "".join(password)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# saving details to the file:
def saving_data():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    new_data = {website: {"email": email, "password": password}}

    if len(website) == 0 or len(email) == 0 or len(password) == 0:
        messagebox.showerror("Error", "Please fill all fields")
    else:
        is_ok = messagebox.askokcancel(title=website, message="These are details entered:\n"
                                                              f"Website: {website} \n Email: {email} \n Password: {password}")
        if is_ok:
            try:
                with open("passwords.json", "r") as file:
                    data = json.load(file)

            except FileNotFoundError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            except JSONDecodeError:
                with open("passwords.json", "w") as file:
                    json.dump(new_data, file, indent=4)
            else:
                data.update(new_data)
                with open("passwords.json", "w") as file:
                    json.dump(data, file, indent=4)
            finally:
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

generate_button = Button(text="Generate Password", bg="white", command=generate_password)
generate_button.grid(row=3, column=2)

search_button = Button(text= "Search", bg="white", width=16, command=searching)
search_button.grid(row=1, column=2)

window.mainloop()