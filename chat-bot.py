from enum import Enum
import prompt
import topics
import calculate

class Command(Enum):
    BACK = "BACK"
    EXIT = "EXIT"
    HELP = "HELP"
    HANDLE = "HANDLE"

state = [0,0]



def handle_user_input():
    user_input = input("Користувач: ")
    if user_input.lower() == "назад":
        return (Command.BACK, False)
    if user_input.lower() == "допомога":
        return (Command.HELP, False)
    if user_input.lower() == "вихід":
        return (Command.EXIT, False)

    return (Command.HANDLE, user_input)




prompt.bot_say("Вітаю, мене звати Кanya.")

while(True):
    if not state[0]:
        topic = topics.show_topics(topics.user_topics)
        (command, user_input) = handle_user_input()

        if command == Command.HANDLE:
            topic_id = topics.get_by_id(user_input, topics.user_topics)
            if topic_id:
                state[0] = topic_id
                prompt.bot_say(f"""Ви обрали тему «{user_input}»""")
            else:
                prompt.bot_say("Я не знаю таку тему!!!!")
                continue
        if command == Command.EXIT:
            break
        if command == Command.BACK:
            continue
        if command == Command.HELP:
            prompt.bot_say("Some help here")


    elif not state[1]:

        match state[0]:
            case 1: #math
                subtopics = topics.math_subtopics
            case _:
                prompt.bot_say("UNKNOWN TOPIC")
                break

        topic = topics.show_subtopics(subtopics)
        (command, user_input) = handle_user_input()
        if command == Command.HANDLE:
            subtopic_id = topics.get_by_id(user_input, subtopics)
            if subtopic_id:
                state[1] = subtopic_id
            else:
                prompt.bot_say("Я не знаю таку тему!!!!")
                continue
        if command == Command.EXIT:
            break
        if command == Command.BACK:
            state = [0,0]
            continue
        if command == Command.HELP:
            prompt.bot_say("Some more help here")
    else:
        calculate.run(state)
        state = [0,0]

