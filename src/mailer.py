import os
import smtplib

from dotenv import load_dotenv

load_dotenv()

from_email = os.environ.get('FROM_EMAIL')
password = os.environ.get('FROM_EMAIL_PASSWORD')


def send_email(to: str, subject: str, body: str = ""):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=from_email, password=password)
        connection.sendmail(
            from_addr=from_email,
            to_addrs=to,
            msg=f"Subject: {subject}\n\n{body}".encode('utf-8')
        )
