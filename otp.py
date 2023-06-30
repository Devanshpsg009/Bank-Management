import smtplib,ssl,random
from email.message import EmailMessage

def sendotp(a):
    otp = int(1000000*random.random())
    email_of_person = a
    my_email = "psgbankers@gmail.com"
    my_password1 = "PSGBANKERS009"
    my_password = "hlglkojttpcrthxe"
    subject = "OTP"
    body = f"""
    Your one time password (OTP) for login is {otp}
    Please do not share this OTP to anyone!
    """
    email = EmailMessage()
    email["From"] = my_email
    email["To"] = email_of_person
    email["Subject"] = subject
    email.set_content(body)
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
        smtp.login(my_email,my_password)
        smtp.sendmail(my_email,email_of_person, email.as_string())
    return otp