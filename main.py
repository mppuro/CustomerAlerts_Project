import smtplib
from email.mime.text import MIMEText  # importes modules required to send email

subject = "Hello mehul"  # arguments defined
body = "Please see details"
sender = "mehulpurohit000@gmail.com"
recipients = ["mehulpurohit23@gmail.com"]
password = "rixicyjmafejyfbi"


# function to send email
def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:

        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


# function call takes four parameter and pass to above function
send_email(subject, body, sender, recipients, password)
