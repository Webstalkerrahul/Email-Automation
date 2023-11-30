import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import pandas as pd

# Note Gmail Limit is - 500 emails per day
# Hostinger email - 5000 emails per day


def mail(name, email):
    from_addr = 'Something@gmail.com'
    to_addr = str(email)
    msg = MIMEMultipart()
    msg['From'] = from_addr
    msg['To'] = " ,".join(to_addr)
    msg['subject'] = 'Subject for the mail'

    #Mail body the HTML format
    body = f'''
        <html>
            <body>
                <h1>Hello, {name}</h1>
            </body>
        </html>
    '''

    msg.attach(MIMEText(body, 'html'))

    email = 'Your password'
    password = 'password'

    mail = smtplib.SMTP('smtp.gmail.com', 587)
    mail.ehlo()
    mail.starttls()
    mail.login(email, password)
    text = msg.as_string()
    mail.sendmail(from_addr, to_addr, text)
    mail.quit()

#reading teh csv
testcsv = pd.read_csv("test.csv")

# Getting names and emails in list 
names = testcsv['names'].to_list()
emails = testcsv['emails'].to_list()

#calling/sending mails row by row
for i in range(len(names)):
    mail(names[i], emails[i])

