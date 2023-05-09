import prompt

user_topics = [
        "математика",
        "фізика",
        "філологія",
        "географія",
        "астрономія",
        "загальне"
    ]

math_subtopics = [
    "обчислення довжини дуги кола",
    "обчислення площі трикутника за допомогою векторного добутку",
    "виведення н-того числа фібоначчі",
    "виведення числа π"
]

def show_topics(user_topics):
    greeting = f"""Ви можете задати мені питання з наступних тем: {", ".join(user_topics)}. """
    prompt.bot_say(greeting)

def show_subtopics(subtopics):
    greeting = f"""Ви мо`жете задати мені питання з наступних тем:\n {", ".join(subtopics)}. """
    prompt.bot_say(greeting)

def get_by_id(topic, user_topics):
    try:
        return user_topics.index(topic) + 1
    except:
        return False