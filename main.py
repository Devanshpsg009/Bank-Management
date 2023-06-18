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