import smtplib
import time
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

sender_email = "roborangers0@gmail.com"
receiver_email = "abdulmunemultalha@gmail.com"
app_password = "zkprkmkfnxahwuar"

def send_email():
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = "madari"
    msg.attach(MIMEText("Oi kire... modo modo modo!", 'plain'))

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, app_password)

            for i in range(100):
                server.send_message(msg)
                print(f"Sent email {i + 1}")
                time.sleep(0.001)  # 1ms delay (very aggressive)

    except Exception as e:
        print("Error sending emails:", e)

send_email()
#at first at termial install"pip install pyautogui"
#"app_password" will find on your gmail settings