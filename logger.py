import codecs
from datetime import datetime

today = datetime.now()
today_date = today.strftime("%d-%m-%Y-%H-%M")
file_name = "./logs/dialog-" + today_date + ".txt"
f = codecs.open(file_name, "w+", "utf-16") #w+ open to write (create file if it does not exist)
def log(message):
    f.write(message + "\n")