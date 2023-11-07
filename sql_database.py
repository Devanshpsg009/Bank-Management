import mysql.connector
import tkinter
import customtkinter
import csv
from tkinter import messagebox

mydb = mysql.connector.connect(host="localhost", user="root", passwd="1234")
mycursor = mydb.cursor()

with open('C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\count.txt', 'w') as file:
    file.write("2")

def run(a):
    mycursor.execute(a)
    for i in mycursor:
        print(i)

run("create database if not exists bank")
run("use bank")
run("create table if not exists signup(username varchar(30),password varchar(30))")

def signup2():
    with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\database.csv", "r") as file:
        db = csv.reader(file)
        for row in db:
            usr = row[0]
            pss = row[1]
            mycursor.execute("insert into signup values(%s,%s)", [usr, pss])
            mydb.commit()

def open_account():
    def ok():
        a = entry1.get()
        b = entry2.get()
        c = entry3.get()
        d = entry4.get()
        run("create table if not exists account(username varchar(30),account_id varchar(30),contact_no varchar(20),balance varchar(10))")
        mycursor.execute("insert into account values(%s,%s,%s,%s)", [a, b, c, d])
        mydb.commit()
        with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv", "a",newline="") as file:
            db = csv.writer(file,lineterminator="\r\n")
            db.writerow([a, b, c, d])
        messagebox.showinfo("Success", "Account Created")
        app.destroy()

    app = customtkinter.CTk()
    app.geometry("400x300+300+75")
    entry1 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Username", placeholder_text_color="white")
    entry1.place(rely=0.1, relx=0.5, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Account No.", placeholder_text_color="white")
    entry2.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
    entry3 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Mobile No.", placeholder_text_color="white")
    entry3.place(rely=0.5, relx=0.5, anchor=tkinter.CENTER)
    entry4 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Money", placeholder_text_color="white")
    entry4.place(rely=0.7, relx=0.5, anchor=tkinter.CENTER)
    Ok = customtkinter.CTkButton(app, text="Done", command=ok)
    Ok.place(relx=0.5, rely=0.9, anchor=tkinter.CENTER)
    app.mainloop()

def deposite_money():
    def ok():
        try:
            a = entry1.get()
            b = entry2.get()
            account_exists = False
            username_correct = False
            with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv", "r") as file:
                db = csv.reader(file)
                for row in db:
                    usrnm = row[0]
                    accno = row[1]
                    if usrnm == a:
                        username_correct = True
                        if accno == b:
                            c = entry3.get()
                            mycursor.execute("UPDATE account SET balance = balance + %s WHERE account_id = %s", [int(c), b])
                            mydb.commit()
                            messagebox.showinfo("Success", "Money Deposited")
                            account_exists = True
                            break
            if not account_exists:
                if username_correct:
                    messagebox.showerror("Error", "Account number is incorrect. Please try again.")
                else:
                    messagebox.showerror("Error", "Account does not exist. Please create a new account")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        app.destroy()

    app = customtkinter.CTk()
    app.geometry("400x300+300+75")
    entry1 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Username", placeholder_text_color="white")
    entry1.place(rely=0.1, relx=0.5, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Account No.", placeholder_text_color="white")
    entry2.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
    entry3 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Money", placeholder_text_color="white")
    entry3.place(rely=0.5, relx=0.5, anchor=tkinter.CENTER)
    done = customtkinter.CTkButton(app, text="Done", command=ok)
    done.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    app.mainloop()

def withdraw():
    def ok():
        try:
            a = entry1.get()
            b = entry2.get()
            account_exists = False
            username_correct = False
            with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv", "r") as file:
                db = csv.reader(file)
                for row in db:
                    usrnm = row[0]
                    accno = row[1]
                    if usrnm == a:
                        username_correct = True
                        if accno == b:
                            c = entry3.get()
                            mycursor.execute("UPDATE account SET balance = balance - %s WHERE account_id = %s", [int(c), b])
                            mydb.commit()
                            messagebox.showinfo("Success", "Money Withdrew")
                            account_exists = True
                            break
            if not account_exists:
                if username_correct:
                    messagebox.showerror("Error", "Account number is incorrect. Please try again.")
                else:
                    messagebox.showerror("Error", "Account does not exist. Please create a new account")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        app.destroy()

    app = customtkinter.CTk()
    app.geometry("400x300+300+75")
    entry1 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Username", placeholder_text_color="white")
    entry1.place(rely=0.1, relx=0.5, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Account No.", placeholder_text_color="white")
    entry2.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
    entry3 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Money", placeholder_text_color="white")
    entry3.place(rely=0.5, relx=0.5, anchor=tkinter.CENTER)
    done = customtkinter.CTkButton(app, text="Done", command=ok)
    done.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    app.mainloop()

def details():
    def ok():
        def gui():
            gui = customtkinter.CTk()
            gui.geometry("400x300+300+75")
            t1=""
            t2=""
            t3=""
            t4=""
            with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\details.csv","r") as file:
                db = csv.reader(file)
                for row in db:
                    t1 = f"Username: {row[0]}"
                    t2 = f"Account No.: {row[1]}"
                    t3 = f"Mobile No.: {row[2]}"
                    t4 = f"Balance: {row[3]}"
            label1 = customtkinter.CTkLabel(gui,text=t1,font=("Bauhaus 93", 20))
            label1.place(relx=0.3,rely=0.1)
            label2 = customtkinter.CTkLabel(gui,text=t2,font=("Bauhaus 93", 20))
            label2.place(relx=0.3,rely=0.3)
            label3 = customtkinter.CTkLabel(gui,text=t3,font=("Bauhaus 93", 20))
            label3.place(relx=0.3,rely=0.5)
            label4 = customtkinter.CTkLabel(gui,text=t4+" Rs",font=("Bauhaus 93", 20))
            label4.place(relx=0.3,rely=0.7)
            quit_button = customtkinter.CTkButton(gui,text="Done",command=gui.destroy)
            quit_button.place(relx=0.5,rely=0.9,anchor=tkinter.CENTER)
            app.destroy()
            gui.mainloop()
        a = entry1.get()
        b = entry2.get()
        account_exists = False
        username_correct = False
        with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv", "r") as file:
            db = csv.reader(file)
            for row in db:
                usrnm = row[0]
                accno = row[1]
                if usrnm == a:
                    username_correct = True
                    if accno == b:
                        mycursor.execute("select * from account where account_id=%s",[b])
                        row = mycursor.fetchall()
                        with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\details.csv","w") as file:
                            db = csv.writer(file,lineterminator="")
                            db.writerows(row)
                        gui()
            if not account_exists:
                if username_correct:
                    messagebox.showerror("Error", "Account number is incorrect. Please try again.")
                else:
                    messagebox.showerror("Error", "Account does not exist. Please create a new account")
    app = customtkinter.CTk()
    app.geometry("400x300+300+75")
    entry1 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Username", placeholder_text_color="white")
    entry1.place(rely=0.2, relx=0.5, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Account No.", placeholder_text_color="white")
    entry2.place(rely=0.5, relx=0.5, anchor=tkinter.CENTER)
    done = customtkinter.CTkButton(app,text="Ok",command=ok)
    done.place(rely=0.8, relx = 0.5, anchor=tkinter.CENTER)
    app.mainloop()

def update():
    def ok():
        try:
            a = entry1.get()
            b = entry2.get()
            account_exists = False
            username_correct = False
            with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv", "r") as file:
                db = csv.reader(file)
                for row in db:
                    usrnm = row[0]
                    accno = row[1]
                    if usrnm == a:
                        username_correct = True
                        if accno == b:
                            def gui():
                                USERNAME = entry3.get()
                                MOBILE = entry4.get()
                                mycursor.execute("UPDATE account SET username = %s WHERE account_id = %s",[USERNAME,b])
                                mycursor.execute("UPDATE account SET contact_no = %s WHERE account_id = %s",[MOBILE,b])
                                mydb.commit()
                                mycursor.execute("select * from account where account_id=%s",[b])
                                row = mycursor.fetchall()
                                with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv","w") as file:
                                    db = csv.writer(file,lineterminator="\r\n")
                                    db.writerows(row)
                                messagebox.showinfo("Success", "Information Updated")
                                new.destroy()
                            new = customtkinter.CTk()
                            new.geometry("400x300+300+75")
                            entry3 = customtkinter.CTkEntry(new, width=200, height=30, placeholder_text="Enter New Username", placeholder_text_color="white")
                            entry3.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
                            entry4 = customtkinter.CTkEntry(new, width=200, height=30, placeholder_text="Enter New Mobile No.", placeholder_text_color="white")
                            entry4.place(rely=0.5, relx=0.5, anchor=tkinter.CENTER)
                            button = customtkinter.CTkButton(new,text="Confirm",command=gui)
                            button.place(rely=0.7, relx=0.5, anchor=tkinter.CENTER)
                            account_exists = True
                            new.mainloop()
                            break
            if not account_exists:
                if username_correct:
                    messagebox.showerror("Error", "Account number is incorrect. Please try again.")
                else:
                    messagebox.showerror("Error", "Account does not exist. Please create a new account")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        app.destroy()

    app = customtkinter.CTk()
    app.geometry("400x300+300+75")
    entry1 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Username", placeholder_text_color="white")
    entry1.place(rely=0.1, relx=0.5, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Account No.", placeholder_text_color="white")
    entry2.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
    done = customtkinter.CTkButton(app, text="Done", command=ok)
    done.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    app.mainloop()

def delete():
    def ok():
        try:
            a = entry1.get()
            b = entry2.get()
            account_exists = False
            username_correct = False
            with open("C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv", "r") as file:
                db = csv.reader(file)
                for row in db:
                    usrnm = row[0]
                    accno = row[1]
                    if usrnm == a:
                        username_correct = True
                        if accno == b:
                            mycursor.execute("DELETE from account WHERE account_id = %s", [b])
                            mydb.commit()
                            with open('C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\account.csv',"w") as file:
                                db = csv.writer(file)
                                db.writerow("")
                            with open('C:\\Users\\Devansh Gahlot\\Desktop\\My Coding\\Bank-Management\\details.csv',"w") as file:
                                db = csv.writer(file)
                                db.writerow("")
                            messagebox.showinfo("Success", "Account Deleted")
                            account_exists = True
                            break
            if not account_exists:
                if username_correct:
                    messagebox.showerror("Error", "Account number is incorrect. Please try again.")
                else:
                    messagebox.showerror("Error", "Account does not exist. Please create a new account")
        except Exception as e:
            messagebox.showerror("Error", str(e))
        app.destroy()

    app = customtkinter.CTk()
    app.geometry("400x300+300+75")
    entry1 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Username", placeholder_text_color="white")
    entry1.place(rely=0.1, relx=0.5, anchor=tkinter.CENTER)
    entry2 = customtkinter.CTkEntry(app, width=200, height=30, placeholder_text="Enter Account No.", placeholder_text_color="white")
    entry2.place(rely=0.3, relx=0.5, anchor=tkinter.CENTER)
    done = customtkinter.CTkButton(app, text="Done", command=ok)
    done.place(relx=0.5, rely=0.7, anchor=tkinter.CENTER)
    app.mainloop()