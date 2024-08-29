
import smtplib 
from email.message import EmailMessage 

def send_email(subject: str, body: str, to_email: str):
    from_email = "notificaciones.appadm@gmail.com" 
    email_smtp = "smtp.gmail.com" 
    password = "yuwz tecf hjcz typf" 

    # Create an email message object 
    message = EmailMessage() 
    message.set_content(body)
    # Configure email headers 
    message['Subject'] = subject 
    message['From'] = from_email 
    message['To'] = to_email 

    # Set smtp server and port 
    server = smtplib.SMTP(email_smtp, '587') 

    # Identify this client to the SMTP server 
    server.ehlo() 
    # Secure the SMTP connection 
    server.starttls() 

    # Login to email account 
    server.login(from_email, password) 
    # Send email 
    server.send_message(message) 
    # Close connection to server 
    server.quit()


