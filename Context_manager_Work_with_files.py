#***********TASK_1*****************************

# Створити логер який дозволяє працювати з файлами як звичайний open,
# але разом з тим в файл logs.txt записує:
# коли був відкритий файл, назва файла, коли закритий файл
# для інформації про час можемо використати datetime.now()
# приклад відпрацювання
# with my_custom_manager('file.txt', 'r') as f:
#     f.read()
# В файл буде записано
# 2022-07-11 22:17:59.782551 file.txt OPEN
# 2022-07-11 22:18:00.782551 file.txt CLOSE

import logging
from datetime import datetime

logging.basicConfig(filename="logs.txt", encoding="UTF-8", level=logging.DEBUG)

class my_custom_manager:

    def __init__(self, filename, mode='r'):
        self.filename = filename
        self.file = open(filename, mode)
        logging.info(f"{datetime.now()}  {filename}  OPEN")

    def __enter__(self):
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()
        logging.info(f"{datetime.now()}  {self.filename}  CLOSE")

with my_custom_manager('readd.txt') as f:
    f.read()

#********************TASK_2*********************
# Написати ф-цію яка переводить файл logs.txt в logs.csv
# Приклад такого файлу
# 2022-07-11 22:17:59.782551, file.txt, OPEN
# 2022-07-11 22:18:00.782551, file.txt, CLOSE

def reformat(file):
    with open(file, "r") as file_txt:
        context = file_txt.read()

    with open("file.csv", "w") as file_csv:
        file_csv.write(context)


reformat('logs.txt')

#*******************TASK_3******************
# Написати ф-цію, яка обраховує з файла logs.csv скільки раз був відкритий файл і його остання дата відкриття.
# Цю інформацію записати в logs.json. Приклад:
# {
#     "file.txt": {
#         "count": 2,
#         "last_time_opened": "2022-07-11 22:17:59.782551"
#     }
# }


import csv
import json


def qty_open(file):
    with open(file, newline='') as csv_file:
        count = 0  # к-ть повторень
        time = 0  # останній рядок
        reader = csv.reader(csv_file, delimiter=',')
        for row in reader:
            if 'OPEN' in (", ".join(row)):
                count += 1  # рахую к-ть 'OPEN'
                time = row

    last_time = str(time)[23:36]  # дістаю час останнього відкриття

    info = {file: {"count": count, "last_time_opened": last_time}}

    with open('file.json', 'w') as f:
        f.write(json.dumps(info))


qty_open('file.csv')

with open('file.json') as f:
    print(f.read())