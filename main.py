from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip

WHITE = "white"
BLACK = "black"
BLUE = "#DAFFFB"

window = Tk()
window.title("Password Manager")
window.config(padx=40, pady=50, bg=WHITE)


# ---------------------------- PASSWORD GENERATOR ------------------------------- #
# Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_entry.delete(0, END)
    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(password) == 0:
        return messagebox.showwarning(message="Do not leave any field empty!")

    is_ok = messagebox.askokcancel(title=website, message=f"These are the entered details: \nEmail: {email}"
                                                          f"\nPassword: {password} \n Is it ok to save?")
    if is_ok:
        with open("data.txt", mode="a") as data_file:
            data_file.write(f"{website} | {email} | {password}\n")
            website_entry.delete(0, END)
            password_entry.delete(0, END)
            messagebox.showinfo(message="Password added to manager")


# ---------------------------- UI SETUP ------------------------------- #
canvas = Canvas(width=200, height=200, bg=WHITE, highlightthickness=0)
image = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=image)
canvas.grid(row=0, column=1)

Label(text="Website:", bg=WHITE, fg=BLACK).grid(row=1, column=0)
website_entry = Entry(bg=WHITE, fg=BLACK, highlightthickness=1, highlightcolor=BLUE, width=35)
website_entry.grid(row=1, column=1, columnspan=2)

Label(text="Email/Username:", bg=WHITE, fg=BLACK).grid(row=2, column=0)
email_entry = Entry(bg=WHITE, fg=BLACK, highlightthickness=1, highlightcolor=BLUE, width=35)
email_entry.insert(0, "example@mail.com")  # pre-populate email
email_entry.grid(row=2, column=1, columnspan=2)

Label(text="Password:", bg=WHITE, fg=BLACK).grid(row=3, column=0)
password_entry = Entry(bg=WHITE, fg=BLACK, highlightthickness=1, highlightcolor=BLUE, width=21)
password_entry.grid(row=3, column=1)

generate_password_button = Button(text="Generate Password", highlightbackground=WHITE, width=10,
                                  command=generate_password)
generate_password_button.grid(row=3, column=2)

add_button = Button(text="Add", highlightbackground=WHITE, width=32, command=save)
add_button.grid(row=4, column=1, columnspan=2)

window.mainloop()
