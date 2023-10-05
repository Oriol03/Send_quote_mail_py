import smtplib
import datetime as dt
import random

my_email= "owen23codeprof@gmail.com"
mot_pass=""

now=dt.datetime.now()
week_day=now.weekday()
if week_day%2==0:
    with open("quotes.txt") as letter :
        list_quotes=letter.readlines()
        quote=random.choice(list_quotes)
        print(quote)
        with smtplib.SMTP("smtp.gmail.com") as connection :
            connection.starttls()
            connection.login(user=my_email, password=mot_pass)
            connection.sendmail(from_addr=my_email,to_addrs="owenorioln@gmail.com",
                                msg=f"Subject:Motivation speech\n\n{quote} ?")
            connection.close()
