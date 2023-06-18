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