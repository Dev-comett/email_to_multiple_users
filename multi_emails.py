import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(subject, body, recipients, sender_email, sender_password):
    # Create the email
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = ", ".join(recipients)
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))

    #reserved_keyword
    try:
        # Connect to the server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS for security
        server.login(sender_email, sender_password)  # Login to the email account

        # Convert the message to a string and send it
        server.sendmail(sender_email, recipients, msg.as_string())
        print("Email sent successfully!")

    except Exception as e:
        print(f"Failed to send email. Error: {e}")

    #reserved_keyword
    finally:
        server.quit()  # Terminate the SMTP session

# Example usage
if __name__ == "__main__":
    subject = "Test Email"
    body = "This is a test email sent from a Python script."
    recipients = ["recipient1@example.com", "recipient2@example.com"]
    sender_email = "your_email@gmail.com"
    sender_password = "your_password"

    send_email(subject, body, recipients, sender_email, sender_password)
