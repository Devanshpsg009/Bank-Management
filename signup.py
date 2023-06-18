import tkinter,customtkinter,csv,sys,subprocess
from PIL import Image
from tkinter import messagebox

def open_another_py_file(file_path):
    with open('count.txt', 'w') as file:
        file.write("2")
    try:
        subprocess.Popen([sys.executable, file_path])
    except Exception as e:
        print(f"Error opening {file_path}: {e}")
    sys.exit()
def add_users(usrnm, psswd):
    with open("database.csv","w",newline='') as file:
        db = csv.writer(file, lineterminator='')
        db.writerow([usrnm,psswd])
def contactus():
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")
    contact_window = customtkinter.CTk()
    contact_window.title("Contact Us")
    contact_window.geometry("800x600")
    contact_window.mainloop()
def signup_ui():
    def get_username_password2():
        username = entry3.get()
        password = entry4.get()
        add_users(username, password)
        import sql_database
        sql_database.signup2()
        def perform_action():
            open_another_py_file("C:\\Users\\laxmi\\Desktop\\My Coding\\school project\\main.py")
        def show_information_dialog():
            answer = messagebox.askquestion("Success", "Do you want to login now?")
            if answer == 'yes':
                perform_action()
            else:
                with open('count.txt', 'w') as file:
                    file.write("2")
                quit()
        show_information_dialog()
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")
    app1 = customtkinter.CTk()
    app1.title("Signup")
    app1.geometry("800x600+300+75")

    img1 = customtkinter.CTkImage(Image.open("C:\\Users\\laxmi\\Desktop\\My Coding\\school project\\background.jpg"),size=(1366,768))
    l1 = customtkinter.CTkLabel(master=app1, image=img1, text="")
    l1.pack()

    frame = customtkinter.CTkFrame(master=l1, corner_radius=15, width=320, height=360, bg_color="black")
    frame.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    l2 = customtkinter.CTkLabel(master=frame, text="Create your account", font=("Bauhaus 93", 30))
    l2.place(relx=0.5, rely=0.10, anchor=tkinter.CENTER)


    entry3 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Username", placeholder_text_color="light green", corner_radius=6)
    entry3.place(relx=0.5, rely=0.35, anchor=tkinter.CENTER)
    entry4 = customtkinter.CTkEntry(master=frame, width=220, placeholder_text="Password", placeholder_text_color="light green", corner_radius=6)
    entry4.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

    signup = customtkinter.CTkButton(master=frame, text="Signup", command=get_username_password2)
    signup.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)

    contact = customtkinter.CTkButton(master=app1, text="Contact Us", command=contactus)
    contact.place(relx=0.1, rely=0.95, anchor=tkinter.CENTER)
    app1.mainloop()