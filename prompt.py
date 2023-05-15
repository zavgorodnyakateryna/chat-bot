from enum import Enum
from logger import log

PURPLE = '\033[35m' # Green Text
RESET = '\033[0m' # Reset
BLUE = '\033[34m' # RED

class Command(Enum):
    BACK = "BACK"
    EXIT = "EXIT"
    HELP = "HELP"
    HANDLE = "HANDLE"


def bot_say(message):
    print(PURPLE + "Бот: " + RESET, message)
    log("Бот: " + message)

def get_user_input(message =""):
    user_input = input(BLUE + "Користувач: " + message + RESET)
    log("Користувач: " + user_input)
    return user_input

def handle_user_input(message=""):
    user_input = get_user_input(message)
    if user_input.lower() == "назад":
        return (Command.BACK, False)
    if user_input.lower() == "допомога":
        return (Command.HELP, False)
    if user_input.lower() == "вихід":
        return (Command.EXIT, False)

    return (Command.HANDLE, user_input)

def handle_input_as_float(message =""):
    while True:
        try:
            (command, value) = handle_user_input(message)
            if command == Command.HANDLE:
                return (Command.HANDLE, float(value))
            elif command == Command.HELP:
                raise Exception("Unknown command")
            else:
                return (command, value)
        except:
            print("Введіть число або команду 'назад' / 'вихід'")


def handle_input_as_int(message =""):
    while True:
        try:
            (command, value) = handle_user_input(message)
            if command == Command.HANDLE:
                return (Command.HANDLE, int(value))
            elif command == Command.HELP:
                raise Exception("Unknown command")
            else:
                return (command, value)
        except:
            print("Введіть число або команду 'назад' / 'вихід'")