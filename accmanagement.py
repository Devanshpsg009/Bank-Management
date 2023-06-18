import tkinter,customtkinter,sql_database
from PIL import Image,ImageTk

def acmanage():
    customtkinter.set_appearance_mode("Dark")
    customtkinter.set_default_color_theme("green")
    root = customtkinter.CTk()
    root.title("Account Management")
    root.geometry("800x600+300+75")
    img = Image.open("background.jpg")
    img = img.resize((1366, 768))
    img1 = ImageTk.PhotoImage(img)
    l1 = customtkinter.CTkLabel(master=root, image=img1,text="")
    l1.image = img1
    l1.pack()
    frame1 = customtkinter.CTkFrame(master=l1, corner_radius=15, width=320, height=400, bg_color="black")
    frame2 = customtkinter.CTkFrame(master=l1, corner_radius=15, width=320, height=400, bg_color="black")
    frame1.place(relx=0.05, rely=0.6, anchor=tkinter.W)
    frame2.place(relx=0.95, rely=0.6, anchor=tkinter.E)

    open_account = customtkinter.CTkButton(master=frame1, text="Open new account",width=240,height=50,font=("Bauhaus 93", 25),corner_radius=8,command=sql_database.open_account)
    open_account.place(rely=0.2,relx=0.5,anchor = tkinter.CENTER)

    Deposite = customtkinter.CTkButton(master=frame1, text="Deposite Money",width=240,height=50,font=("Bauhaus 93", 25),corner_radius=8,command=sql_database.deposite_money)
    Deposite.place(rely=0.5,relx=0.5,anchor = tkinter.CENTER)

    Withdraw = customtkinter.CTkButton(master=frame1, text="Withdrow Money",width=240,height=50,font=("Bauhaus 93", 25),corner_radius=8,command=sql_database.withdraw)
    Withdraw.place(rely=0.8,relx=0.5,anchor = tkinter.CENTER)

    Details = customtkinter.CTkButton(master=frame2, text="Your Details",width=240,height=50,font=("Bauhaus 93", 25),corner_radius=8,command=sql_database.details)
    Details.place(rely=0.2,relx=0.5,anchor = tkinter.CENTER)

    Update = customtkinter.CTkButton(master=frame2, text="Update info",width=240,height=50,font=("Bauhaus 93", 25),corner_radius=8)
    Update.place(rely=0.5,relx=0.5,anchor = tkinter.CENTER)

    Delete = customtkinter.CTkButton(master=frame2, text="Delete Your account",width=240,height=50,font=("Bauhaus 93", 25),corner_radius=8)
    Delete.place(rely=0.8,relx=0.5,anchor = tkinter.CENTER)

    label1 = customtkinter.CTkLabel(l1,text="Welcome, What do you want to do?",fg_color="transparent",font=("Bauhaus 93", 30))
    label1.place(relx=0.5,rely=0.1,anchor=tkinter.N)
    root.mainloop()
acmanage()