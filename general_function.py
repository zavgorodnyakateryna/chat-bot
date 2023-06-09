import prompt
import random
def what_time():
    from datetime import datetime
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    prompt.bot_say(f"""Поточний час: {current_time}""")

def what_year():
    import datetime
    today = datetime.date.today()
    year = today.year
    prompt.bot_say(f"""Зараз {year} рік""")

def guess_numb():
    prompt.bot_say("Напишіть число між 1 та 10")
    (command, user_number) = prompt.handle_input_as_int()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    print()
    bot_number = random.randint(1, 10)
    prompt.bot_say(f"""Я загадав {bot_number} """)
    if user_number == bot_number:
        prompt.bot_say("Ви вгадали!!!")
    else:
        prompt.bot_say("Ви не вгадали(")


def game():
    prompt.bot_say("Оберіть: камінь, ножиці чи папір")
    user_choose = prompt.get_user_input()
    options = ["камінь", "ножиці", "папір"]
    bot_choose = random.choice(options)
    prompt.bot_say(f"""{bot_choose}""")
    if user_choose == bot_choose:
        prompt.bot_say("Нічия!!!")
    elif user_choose == "камінь":
        if bot_choose == "ножиці":
            prompt.bot_say("Ви виграли!!!")
        else:
            prompt.bot_say("Ви програли(")
    elif user_choose == "папір":
        if bot_choose == "камінь":
            prompt.bot_say("Ви виграли!!!")
        else:
            prompt.bot_say("Ви програли(")
    elif user_choose == "ножиці":
        if bot_choose == "папір":
            prompt.bot_say("Ви виграли!!!")
        else:
            prompt.bot_say("Ви програли(")
