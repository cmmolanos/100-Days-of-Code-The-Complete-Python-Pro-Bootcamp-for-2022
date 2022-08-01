##################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

# 2. Check if today matches a birthday in the birthdays.csv

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual
# name from birthdays.csv

# 4. Send the letter generated in step 3 to that person's email address.
import datetime as dt
import random
import smtplib

import pandas as pd

MY_EMAIL = "test@gmail.com"
PASSWORD = "fakepass123"

current_date = dt.datetime.now()

df = pd.read_csv('birthdays.csv')
today_birthdays = df[
    (df['month'] == current_date.month) &
    (df['day'] == current_date.day)
    ]

if today_birthdays.shape[0] != 0:

    for index, row in today_birthdays.iterrows():

        template_idx = random.randint(1, 3)
        template_path = f"./letter_templates/letter_{template_idx}.txt"

        with open(template_path, "r") as file:
            content = file.read()

        body = content.replace("[NAME]", row["name"])

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=row["email"],
                msg=f"Subject:Happy Birthday {row['name']}!"
                    "\n\n"
                    f"{body}",
            )

else:
    print("Nobody is on birthday today.")
