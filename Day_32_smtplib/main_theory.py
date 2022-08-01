import datetime as dt
import smtplib
import random

my_email = "test@gmail.com"
password = "fakepass123"

date = dt.datetime.now()

if date.weekday() == 0:
    with open('quotes.txt', 'r') as file:
        quotes = file.readlines()

    quote = random.choice(quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="kiki@gmail.com",
            msg=f"Subject:Motivational Quotes for Today!"
                "\n\n"
                f"{quote}",
        )

