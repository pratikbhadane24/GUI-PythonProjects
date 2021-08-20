from tkinter import *
from tkinter import messagebox
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


# ---------------------------- SAVE PASSWORD ------------------------------- #

def savedata():
    website = website_entry.get()
    email = email_entry.get()
    password = password_entry.get()

    if len(website)==0 or len(email)==0 or len(password)==0:
        messagebox.showinfo(title="Oops!", message="Please make sure you haven't left any field empty!")
    else:
        is_ok = messagebox.askokcancel(
            title=website, message=f"Please Confirm Your details\nEmail: {email}\nPassword: {password}\nPress OK to Save.")

        if is_ok:
            with open("data.txt", "a") as data_file:
                data_file.write(
                    f"Website: {website}\n    Email: {email}\n    Password: {password}\n\n")
                website_entry.delete(0, END)
                email_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="black")


canvas = Canvas(width=200, height=200, bg="black", highlightthickness=0)
bg_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=bg_img)
canvas.grid(row=0, column=1)


# Labels
website_label = Label(text="Website:", bg="black", fg="white",
                      highlightthickness=0, font=("Fira Code", 10, "bold"))
website_label.grid(row=1, column=0)

email_label = Label(text="Email/Username:", bg="black", fg="white",
                    highlightthickness=0, font=("Fira Code", 10, "bold"))
email_label.grid(row=2, column=0)

password_label = Label(text="Password:", bg="black", fg="white",
                       highlightthickness=0, font=("Fira Code", 10, "bold"))
password_label.grid(row=3, column=0)


# Entry Inputs
website_entry = Entry(width=40, bg="white", font=('calibre', 10, 'normal'))
website_entry.grid(row=1, column=1, columnspan=2, pady=3)
website_entry.focus()

email_entry = Entry(width=40, bg="white", font=('calibre', 10, 'normal'))
email_entry.grid(row=2, column=1, columnspan=2, pady=3)

password_entry = Entry(width=27, bg="white", font=('calibre', 10, 'normal'))
password_entry.grid(row=3, column=1, pady=3)


# Buttons
genpass = Button(text="Generate Password", font=('calibre', 7, 'normal'))
genpass.grid(row=3, column=2)

add = Button(text="Add", width=39, command=savedata)
add.grid(row=4, column=1, columnspan=2, pady=3)


canvas.mainloop()
