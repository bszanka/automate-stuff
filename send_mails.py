import smtplib

# E-mail us!
conn = smtplib.SMTP('smtp.gmail.com', 587)
conn.ehlo()  # ehlo = hello
conn.starttls()
# Username, Password
conn.login('simplifybanking@gmail.com', 'password')
# From, To, Message Body
conn.sendmail('simplifybanking@gmail.com', 'simplifybanking@gmail.com', 'Subject: Test Mail...\n\nHello World!')
conn.quit()
