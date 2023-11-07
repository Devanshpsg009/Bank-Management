import customtkinter as ctk

class PasswordEntry(ctk.CTkEntry):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)
        self.show_password = False

        self.show_password_button = ctk.CTkButton(self, text="Show", command=self.toggle_password)
        self.show_password_button.grid(row=0, column=1, sticky="e")

    def toggle_password(self):
        self.show_password = not self.show_password
        self.update_display()

    def update_display(self):
        if self.show_password:
            self.show_password_button.configure(text="Hide")
            self.configure(show="")
        else:
            self.show_password_button.configure(text="Show")
            self.configure(show="*")

if __name__ == "__main__":
    root = ctk.CTk()
    root.title("Password Entry")

    password_entry_frame = ctk.CTkFrame(root)
    password_entry_frame.grid(padx=10, pady=10)

    password_entry = PasswordEntry(password_entry_frame, show="*")
    password_entry.grid()

    root.mainloop()