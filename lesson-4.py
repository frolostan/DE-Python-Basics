# Основы Python. GU_Data_Engineering_1542 (31.01.2022)
# Выполнил: Фролов Виктор Сергеевич;
# Урок 4.


"""
1.Проверить,
установлен ли пакет pillow в глобальном окружении.Если да — зафиксировать версию.Установить самую свежую версию pillow,
если ранее она не была установлена.Сделать подтверждающий скриншот.Создать и активировать виртуальное окружение.Убедиться,
что в нем нет пакета pillow.Сделать подтверждающий скриншот.Установить в виртуальное окружение pillow версии 7.1.1 (или другой, отличной от самой свежей).Сделать подтверждающий скриншот.Деактивировать виртуальное окружение.Сделать подтверждающий скриншот.Скрины нумеровать двухразрядными числами,
например: « 01.jpg »,
« 02.jpg ».Если будут проблемы с pillow - можно поработать с другим пакетом: например,
requests.

"""


# pip install


"""
2.Написать функцию currency_rates(),
принимающую в качестве аргумента код валюты (например, USD, EUR, GBP,...) и возвращающую курс этой валюты по отношению к рублю.Использовать библиотеку requests.В качестве API можно использовать http: / / www.cbr.ru / scripts / XML_daily.asp.Рекомендация: выполнить предварительно запрос к API в обычном браузере,
посмотреть содержимое ответа.Можно ли,
используя только методы класса str,
решить поставленную задачу ? Функция должна возвращать результат числового типа,
например float.Подумайте: есть ли смысл для работы с денежными величинами использовать вместо float тип Decimal ? Сильно ли усложняется код функции при этом ? Если в качестве аргумента передали код валюты,
которого нет в ответе,
вернуть None.Можно ли сделать работу функции не зависящей от того,
в каком регистре был передан аргумент ? В качестве примера выведите курсы доллара и евро.

"""
"""
2.1.Доработать функцию currency_rates(): теперь она должна возвращать кроме курса дату,
которая передаётся в ответе сервера.Дата должна быть в виде объекта date.Подумайте,
как извлечь дату из ответа,
какой тип данных лучше использовать в ответе функции ?
"""

import requests
from decimal import *
from datetime import datetime


getcontext().prec = 4

def currency_rates(val):
    val = val.upper()
    response = requests.get('http://www.cbr.ru/scripts/XML_daily.asp').text
    if val not in response:
        return None
    rub = response[response.find('<Value>', response.find(val)) + 7:response.find('</Value>', response.find(val))]
    day_raw = response[response.find('Date="') + 6:response.find('"', response.find('Date="') + 6)].split('.')
    day, month, year = map(int, day_raw)
    return f"{Decimal(rub.replace(',', '.'))}, {datetime(day=day, month=month, year=year)}"


print(currency_rates('USD'))
print(currency_rates('EUR'))
print(currency_rates('eur'))

# Другой способ

import requests
from datetime import datetime

def cur_rate(cur_code='', url="http://www.cbr.ru/scripts/XML_daily.asp"):
    cur_code = cur_code.upper()
    res=requests.get(url)
    if res.ok:
        cur = res.text.split(cur_code)
        if len(cur) == 1:
            return None
        value = cur[1].split('</Value>')[0].split('<Value>')[1]
        value = float(value.replace(',', '.'))
        date = res.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        return value, date
    else:
        return None


print(cur_rate('USD'))
print(cur_rate('eUR'))


"""
3. Написать свой модуль utils и перенести в него функцию currency_rates() 
из предыдущего задания. Создать скрипт, в котором импортировать этот модуль 
и выполнить несколько вызовов функции currency_rates(). Убедиться, что ничего 
лишнего не происходит.
"""


from datetime import datetime
import requests

def cur_rate(cur_code='', url="http://www.cbr.ru/scripts/XML_daily.asp"):
    cur_code = cur_code.upper()
    res=requests.get(url)
    if res.ok:
        cur = res.text.split(cur_code)
        if len(cur) == 1:
            return None
        value = cur[1].split('</Value>')[0].split('<Value>')[1]
        value = float(value.replace(',', '.'))
        date = res.headers["Date"]
        date = datetime.strptime(date, "%a, %d %b %Y %H:%M:%S GMT").date()
        return value, date
    else:
        return None

# from utils import cur_rate
print(cur_rate('USD'))


"""
*(вместо 4) Доработать скрипт из предыдущего задания: теперь он должен работать и из консоли.Например: > python task_4_5.py USD 75.18,
2020 -09 -05

"""

# import utils
import sys

# print(utils.cur_rate(sys.argv[1]))
