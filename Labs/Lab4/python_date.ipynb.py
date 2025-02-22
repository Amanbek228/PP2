#1
from datetime import datetime

first_date = datetime.strptime(input("Введите первую дату (ГГГГ-ММ-ДД ЧЧ:ММ:СС): "), "%Y-%m-%d %H:%M:%S")
second_date = datetime.strptime(input("Введите вторую дату (ГГГГ-ММ-ДД ЧЧ:ММ:СС): "), "%Y-%m-%d %H:%M:%S")


difference = abs((second_date - first_date).total_seconds())


print("Разница в секундах:", int(difference))

#2
from datetime import datetime

now = datetime.now().replace(microsecond=0)
print("Дата и время без микросекунд:", now.strftime("%Y-%m-%d %H:%M:%S"))

#3
from datetime import datetime, timedelta

today = datetime.today()
yesterday = today - timedelta(days=1)
tomorrow = today + timedelta(days=1)

print("Вчера:", yesterday.strftime("%Y-%m-%d"))
print("Сегодня:", today.strftime("%Y-%m-%d"))
print("Завтра:", tomorrow.strftime("%Y-%m-%d"))

#4
from datetime import datetime, timedelta

print((datetime.today() - timedelta(days=5)).strftime("%Y-%m-%d"))