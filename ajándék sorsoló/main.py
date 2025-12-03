import smtplib
import os
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from megoldás import megoldas


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
    m = megoldas()

    parok = m.vegrehajtas_huzas()

    for huzo, huzott in parok:
        recipient = huzo.Tanuló_email
        subject = "Karácsonyi húzás"
        body = f"Szia {huzo.Tanuló_neve}!\nA karácsonyi húzás eredménye: Ő {huzott.Tanuló_neve} húztad!\nKellemes ünnepeket!"
        send_email(recipient, subject, body)
