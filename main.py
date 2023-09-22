import winreg,webbrowser
from tkinter import messagebox
def start():
    count = 1
    try:
        with open('C:\\Users\\laxmi\\Desktop\\My Coding\\school project\\Bank-Management\\count.txt', 'r') as file:
            count = int(file.read().strip())
    except FileNotFoundError:
        with open('C:\\Users\\laxmi\\Desktop\\My Coding\\school project\\Bank-Management\\count.txt', 'w') as file:
            file.write(str(count))

    if count <= 1:
        import signup
        signup.signup_ui()
    else:
        import login
        login.login_ui()

    count += 1
    with open('C:\\Users\\laxmi\\Desktop\\My Coding\\school project\\Bank-Management\\count.txt', 'w') as file:
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
        return []

installed_programs = get_installed_programs()
if installed_programs:
        cnt = 0
        for program in installed_programs:
            if "MySQL" in program:
              cnt += 1
        if cnt >= 1:
            start()
else:
    a = messagebox.askquestion("Error","Sorry, Latest version or Mysql is not installed in your computer.Do you want to download Mysql?")
    if a == "yes":
        webbrowser.open("https://dev.mysql.com/downloads/file/?id=520406")
    else:
        quit()