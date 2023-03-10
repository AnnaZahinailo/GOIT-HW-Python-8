from datetime import date, timedelta
from users import users

TY = date.today().year

def get_birthdays_per_week(users):

    date_in_week = date.today()
    current_weekday = date_in_week.weekday()
    date_in_week = date_in_week + timedelta(days=7 - current_weekday) 

    print("\nTo congratulate with Birthday next week:\n")

    for _ in range(5):
        line = []  
        for user in users:
            bd = user.get("birthday").replace(year=TY)
            user_name = user.get("name")
            if date_in_week.weekday() == 0:
                if bd == date_in_week - timedelta(days=2):
                    line.append(user_name)
                if bd == date_in_week - timedelta(days=1):
                    line.append(user_name)
            if bd == date_in_week:
                line.append(user_name)

        sline = ""
        sline = ",".join(line)
        print(f"{date_in_week.strftime('%A')}: {sline}")       
        date_in_week += timedelta(days=1)
    print("\n")


def main():
    get_birthdays_per_week(users)

if __name__ == "__main__":
    main()