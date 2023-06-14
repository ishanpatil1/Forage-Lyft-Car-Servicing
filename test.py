import datetime
while True:
#     last_date=input("Date:-")
#     print(datetime.datetime.strptime(last_date, "%Y-%m-%d").date())
    last_date=input("Date:- ")
    try:
        last_date = datetime.datetime.strptime(last_date, "%Y-%m-%d").date()
        break
    except ValueError:
        print("Invalid date. ")