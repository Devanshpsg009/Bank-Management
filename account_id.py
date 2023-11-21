import smtplib,ssl,random
from email.message import EmailMessage

def sendaccount_id(a):
    id = int(100000000*random.random())
    email_of_person = a
    my_email = "psgbankers@gmail.com"
    my_password1 = "PSGBANKERS009"
    my_password = "hlglkojttpcrthxe"
    subject = "Your Account ID for PSG Banks"
    body = f"""
    Your Account ID for PSG Banks is {id}
    This will remain permanent untill you delete your account or you create a new account in PSG Banks.

    With Regards,
    PSG Bankers
    """
    email = EmailMessage()
    email["From"] = my_email
    email["To"] = email_of_person
    email["Subject"] = subject
    email.set_content(body)
    context = ssl.create_default_context()
    try:
        with smtplib.SMTP_SSL("smtp.gmail.com",465,context=context) as smtp:
            smtp.login(my_email,my_password)
            smtp.sendmail(my_email,email_of_person, email.as_string())
    except:
        pass
    return id