import tkinter,customtkinter,csv,sys,subprocess
from PIL import Image
from tkinter import messagebox

def check_password(password):
    with open("database.csv","r") as file:
        db = csv.reader(file)
        for row in db:
            pss = row[1]
            if password == pss:
                function()
            else:
                answer = messagebox.showerror("Error", "Password doesn't match, Try again?")
                if answer == "ok":
                    pass
                else:
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
    messagebox.showinfo("Success","You may continue now.")
    open_another_py_file("accmanagement.py")
def check_usr(usrname):
    with open("database.csv","r") as file:
        db = csv.reader(file)
        for row in db:
            usr = row[0]
            if usrname == usr:
                pass
            else:
                answer = messagebox.showerror("Error", "User not found, Sign up instead?")
                if answer == "ok":
                    open_another_py_file("main.py")
                else:
                    quit()
def contactus():
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
        check_usr(username)
        check_password(password)
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")
    app = customtkinter.CTk()
    app.title("Login")
    app.geometry("800x600+300+75")

    img1 = customtkinter.CTkImage(Image.open("background.jpg"),size=(1366,768))
    l1 = customtkinter.CTkLabel(master=app, image=img1, text="")
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, corner_radius=15, width=320, height=360, bg_color="black")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Login to your account", font=("Bauhaus 93", 30))
    l2.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)

    entry1 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username", placeholder_text_color="light green", corner_radius=6)
    entry1.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", placeholder_text_color="light green", corner_radius=6)
    entry2.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    login = customtkinter.CTkButton(master=frame, text="Login", command=get_username_password)
    login.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    contact = customtkinter.CTkButton(master=app, text="Contact Us", command=contactus)
    contact.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)

    app.mainloop()