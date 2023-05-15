
import prompt
import topics
import calculate

state = [0,0]





prompt.bot_say("Вітаю, мене звати Кanya.")

while(True):
    if not state[0]:
        topic = topics.show_topics(topics.user_topics)
        (command, user_input) = prompt.handle_user_input()

        if command == prompt.Command.HANDLE:
            topic_id = topics.get_by_id(user_input, topics.user_topics)
            if topic_id:
                state[0] = topic_id
                prompt.bot_say(f"""Ви обрали тему «{user_input}»""")
            else:
                prompt.bot_say("Я не знаю таку тему(")
                continue
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            break
        if command == prompt.Command.BACK:
            continue
        if command == prompt.Command.HELP:
            prompt.bot_say("Оберіть тему та напишіть мені її! Щоб вийти, напишіть 'вихід'")


    elif not state[1]:

        match state[0]:
            case 1: #math
                subtopics = topics.math_subtopics
            case 2: #physic
                subtopics = topics.physics_subtopics
            case 3: #philology
                subtopics = topics.philology_subtopics
            case 4: #geography
                subtopics = topics.geography_subtopics
            case 5: #astronomy
                subtopics = topics.astronomy_subtopics
            case 6: #general
                subtopics = topics.general_subtopics
            case _:
                prompt.bot_say("UNKNOWN TOPIC")
                break

        topic = topics.show_subtopics(subtopics)
        (command, user_input) = prompt.handle_user_input()
        if command == prompt.Command.HANDLE:
            subtopic_id = topics.get_by_id(user_input, subtopics)
            if subtopic_id:
                state[1] = subtopic_id
            else:
                prompt.bot_say("Я не знаю таку тему")
                continue
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            break
        if command == prompt.Command.BACK:
            state = [0,0]
            continue
        if command == prompt.Command.HELP:
            prompt.bot_say("Оберіть тему та напишіть мені її! Щоб вийти, напишіть 'вихід' \nЩоб повернутись та обрати іншу тему, натисність 'назад'")
    else:
        calculate.run(state)
        state = [0,0]

