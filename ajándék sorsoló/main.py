from eredmény import húzó, húzott, Tanuló_email
import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS", "idesz.marcell@students.jedlik.eu")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD", "fteq qaqi hlvo ypto")


def send_email(recipient_email, subject, body):

    try:
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient_email
        msg["Subject"] = subject

        msg.attach(MIMEText(body, "plain"))

        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)

        print("Email sent successfully!")
    except Exception as e:
        print(f"Failed to send email: {e}")


if __name__ == "__main__":
    recipient = Tanuló_email
    subject = "Karácsonyi húzás"
    body = f"Szia {húzó}!\nA karácsonyi húzás eredménye: Te {húzott} húztad!\nKellemes ünnepeket!"
    send_email(recipient, subject, body)

