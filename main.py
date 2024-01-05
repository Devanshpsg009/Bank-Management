import winreg
import webbrowser
from tkinter import messagebox

def start():
    try:
        with open('count.txt', 'r') as file:
            count = int(file.read().strip())
    except FileNotFoundError:
        with open('count.txt', 'w') as file:
            file.write("1")
        count = 1

    print(f"Count before increment: {count}")

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
        print(f"Error in get_installed_programs: {e}")
        return None

def main():
    installed_programs = get_installed_programs()

    if installed_programs is not None:
        cnt = sum("MySQL" in program for program in installed_programs)

        if cnt >= 1:
            start()
        else:
            message = "MySQL is not installed on your computer. Do you want to download it?"
            answer = messagebox.askquestion("Error", message)
            if answer == "yes":
                webbrowser.open("https://dev.mysql.com/downloads/file/?id=520406")
            else:
                quit()
    else:
        print("Error getting installed programs. Please check for any issues.")

if __name__ == "__main__":
    main()
