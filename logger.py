import codecs
from datetime import datetime
import os

dir = "./logs"

isDirExist = os.path.exists(dir)
if not isDirExist:
    os.makedirs(dir)

today = datetime.now()
today_date = today.strftime("%d-%m-%Y-%H-%M")
file_name = dir + "/dialog-" + today_date + ".txt"
f = codecs.open(file_name, "w+", "utf-16") #w+ open to write (create file if it does not exist)
def log(message):
    f.write(message + "\n")