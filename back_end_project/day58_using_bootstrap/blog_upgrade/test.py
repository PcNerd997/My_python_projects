from smtplib import SMTP


connection = SMTP("smtp.gmail.com")

connection.starttls()