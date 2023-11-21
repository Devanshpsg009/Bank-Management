import winreg, webbrowser
from tkinter import messagebox
import os
cwd = os.getcwd()

def start():
    count = 1
    try:
        with open('count.txt', 'r') as file:
            count = int(file.read().strip())
    except FileNotFoundError:
        with open('count.txt', 'w') as file:
            file.write(str(count))

    if count <= 1:
        import signup
        signup.signup_ui()
    else:
        import login
        login.login_ui()

    count += 1
    with open('count.txt', 'w') as file:
        file.write(str(count))

def get_installed_programs():
    try:
        key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Uninstall")
        installed_programs = []
        for i in range(winreg.QueryInfoKey(key)[0]):
            subkey_name = winreg.EnumKey(key, i)
            subkey = winreg.OpenKey(key, subkey_name)
            try:
                program_name = winreg.QueryValueEx(subkey, "DisplayName")[0]
                installed_programs.append(program_name)
            except FileNotFoundError:
                pass
        winreg.CloseKey(key)
        return installed_programs
    except Exception as e:
        # Log the error here
        return None

def open_mysql_download_page():
    import requests
    response = requests.get("https://dev.mysql.com/downloads/file/?id=520406")
    if response.status_code == 200:
        webbrowser.open("https://dev.mysql.com/downloads/file/?id=520406")
    else:
        webbrowser.open("https://dev.mysql.com/downloads/")
        pass

def main():
    installed_programs = get_installed_programs()
    if installed_programs is None:
        # Log the error here
        pass
    elif installed_programs:
        cnt = 0
        for program in installed_programs:
            if "MySQL" in program:
                cnt += 1
        if cnt >= 1:
            start()
    else:
        message = "Sorry, MySQL is not installed on your computer. Do you want to download it?"
        answer = messagebox.askquestion("Error", message)
        if answer == "Yes":
            open_mysql_download_page()
        else:
            quit()

if __name__ == "__main__":
    main()