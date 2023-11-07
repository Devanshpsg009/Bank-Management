import tkinter
from tkinter import messagebox
import csv
import sys
import subprocess
from PIL import Image
import otp  # Ensure you have the 'otp' module installed
import customtkinter

def check_password(password, stored_password):
    if password == stored_password:
        function()
    else:
        answer = messagebox.askquestion("Error", "Password doesn't match, Try again?")
        if answer == "no":
            quit()

def open_another_py_file(file_path):
    with open('count.txt', 'w') as file:
        file.write("1")
    try:
        subprocess.Popen([sys.executable, file_path])
    except Exception as e:
        print(f"Error opening {file_path}: {e}")
        sys.exit()

def function():
    messagebox.showinfo("Verify", "In order to continue, you need to verify yourself.")

    def process_email():
        email = email_entry.get()
        try:
            otp_value = otp.sendotp(email)

            def check_otp():
                entered_otp = email_entry2.get()
                if otp_value == int(entered_otp):
                    messagebox.showinfo("Success", "You may continue now.")
                    open_another_py_file("accmanagement.py")
                else:
                    messagebox.showerror("Error", "Wrong OTP, please try again!")

            window2 = customtkinter.CTk()
            window2.title("Email Processing")
            window2.geometry("300x150")
            email_entry2 = customtkinter.CTkEntry(window2, placeholder_text="OTP")
            email_entry2.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
            ok_button2 = customtkinter.CTkButton(window2, text="Verify", command=check_otp)
            ok_button2.place(rely=0.6, relx=0.5, anchor=tkinter.CENTER)
            window2.mainloop()
        except Exception as e:
            messagebox.showerror("Error", str(e))

    window = customtkinter.CTk()
    window.title("Email Processing")
    window.geometry("300x150")
    email_entry = customtkinter.CTkEntry(window, placeholder_text="Email")
    email_entry.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
    ok_button = customtkinter.CTkButton(window, text="Send OTP", command=process_email)
    ok_button.place(rely=0.6, relx=0.5, anchor=tkinter.CENTER)
    window.mainloop()

def check_usr(usrname, password):
    if usrname == "psgbankersadmin":
        if password == "psgbankersroot":
            messagebox.showinfo("Welcome", "Admin mode activated!")
        else:
            answer = messagebox.askquestion("Error", "Password doesn't match, Try again?")
            if answer == "no":
                quit()
    else:
        with open("database.csv", "r") as file:
            db = csv.reader(file)
            for row in db:
                username = row[0]
                stored_password = row[1]
                if usrname == username:
                    check_password(password, stored_password)
                    return
            answer = messagebox.askquestion("Error", "User not found, Sign up instead?")
            if answer == "yes":
                open_another_py_file("main.py")
            else:
                quit()

def contact_us():
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")
    contact_window = customtkinter.CTk()
    contact_window.title("Contact Us")
    contact_window.geometry("800x600")
    contact_window.mainloop()

def login_ui():
    def get_username_password():
        username = entry1.get()
        password = entry2.get()
        check_usr(username, password)

    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")
    app = customtkinter.CTk()
    app.title("Login")
    app.geometry("800x600+300+75")

    img1 = customtkinter.CTkImage(Image.open("background.jpg"), size=(1366, 768))
    l1 = customtkinter.CTkLabel(master=app, image=img1, text="")
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, corner_radius=15, width=320, height=360, bg_color="black")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Login to your account", font=("Bauhaus 93", 30))
    l2.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username", placeholder_text_color="light green", corner_radius=6)
    entry1.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", placeholder_text_color="light green", corner_radius=6, show = "*")
    entry2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    login = customtkinter.CTkButton(master=frame, text="Login", command=get_username_password)
    login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    contact = customtkinter.CTkButton(master=app, text="Contact Us", command=contact_us)
    contact.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)

    app.mainloop()

if __name__ == "__main__":
    login_ui()
