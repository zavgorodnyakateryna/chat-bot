PURPLE = '\033[35m' # Green Text
RESET = '\033[0m' # Reset
BLUE = '\033[34m' # RED


def bot_say(message):
    print(PURPLE + "Бот: " + RESET, message)

def user_say(message = ""):
    return input(BLUE + "Користувач: " + message + RESET)
