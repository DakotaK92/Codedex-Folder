import datetime, birthday_messages

today = datetime.date.today()

my_next_birthday = datetime.date(2026, 12, 4)

days_away = my_next_birthday - today

if my_next_birthday == today:
  print(birthday_messages.random_message)
else:
  print(f'My next birthday is {days_away.days} days away!')