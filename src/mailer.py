import smtplib

my_email = "joshuamilton2207@gmail.com"
password = "eluzzwjnbxdwsvwq"


def send_email(to: str, subject: str, body: str = ""):
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=to,
            msg=f"Subject: {subject}\n\n{body}"
        )
