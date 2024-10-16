from model.mail.smtp import email
email.send_email(recipient_email="info.creationology@gmail.com",subject="Trial",body="This is a trial",body_type="html")