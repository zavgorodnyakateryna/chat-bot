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

physics_subtopics = [
    "рівняння ейнштейна для мас-енергії",
    "закон збереження енергії",
    "стала планка"
]

philology_subtopics = [
    "яка різниця між іменником та прикметником?",
    "які відмінки є в українській мові?",
    "що таке філологія?",
    "які галузі науки включає в себе філологія?"
]

geography_subtopics = [
    "який океан найбільший за площею?",
    "де знаходиться Сахара - найбільша пустеля в світі?",
    "знайти координати т. В (відомо координати т. А; відстань між ними (d); азимут від т. А до т. В)" 
    "знайти відстань між двома точками (відомі їх координати)",
    "назвати головні типи клімату",
    "що таке екватор?"
]

astronomy_subtopics = [
    "яка є відстань між Землею та Сонцем?",
    "які типи зір відомі в астрономії?",
    "що таке астрономія?",
    "що таке комети?"
]

general_subtopics = [
    "котра година?",
    "який зараз рік?",
    "пограти у вгадай число між 1 та 10",
    "пограти у камінь-ножиці-папір"
]


def show_topics(user_topics):
    greeting = f"""Ви можете задати мені питання з наступних тем: {", ".join(user_topics)}. """
    prompt.bot_say(greeting)

def show_subtopics(subtopics):
    greeting = f"""Ви можете задати мені питання з наступних тем:\n {", ".join(subtopics)}. """
    prompt.bot_say(greeting)

def get_by_id(topic, user_topics):
    try:
        return user_topics.index(topic) + 1
    except:
        return False