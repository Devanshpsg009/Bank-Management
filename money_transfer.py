import tkinter,customtkinter
from PIL import Image,ImageTk

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("green")
root = customtkinter.CTk()
root.title("Account Management")
root.geometry("800x600+300+75")
img = Image.open("C:\\Users\\laxmi\\Desktop\\My Coding\\school project\\Bank-Management\\money.jpg")
img = img.resize((1366, 768))
img1 = ImageTk.PhotoImage(img)
l1 = customtkinter.CTkLabel(master=root, image=img1,text="")
l1.image = img1
l1.pack()
frame1 = customtkinter.CTkFrame(master=l1, corner_radius=15, width=320, height=400, bg_color="black")
frame1.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)
root.mainloop()