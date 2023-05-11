from logger import log

PURPLE = '\033[35m' # Green Text
RESET = '\033[0m' # Reset
BLUE = '\033[34m' # RED

def bot_say(message):
    print(PURPLE + "Бот: " + RESET, message)
    log("Бот: " + message)

def user_say(message = ""):
    user_input = input(BLUE + "Користувач: " + message + RESET)
    log("Користувач: " + user_input)
    return user_input
