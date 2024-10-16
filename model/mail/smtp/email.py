from config.config import SENDER_EMAIL,EMAIL_PORT,EMAIL_PASSWORD,EMAIL_HOST
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
def send_email(*,recipient_email="",subject="",body='',body_type = "text"):
    
    msg = MIMEMultipart('alternative')
    msg['From'] = SENDER_EMAIL
    msg['To'] = recipient_email
    msg['Subject'] = subject
    
    
    # Attach the HTML content to the email
    msg.attach(MIMEText(body, body_type))

    # Send the email using SMTP server
    try:
        with smtplib.SMTP(EMAIL_HOST,int(EMAIL_PORT)) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(SENDER_EMAIL, EMAIL_PASSWORD)
            server.sendmail(SENDER_EMAIL, recipient_email, msg.as_string())
            print("Registration email sent successfully.")
    except Exception as e:
        print(f"Failed to send email: {e}")

