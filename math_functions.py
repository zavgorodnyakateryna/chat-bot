import prompt

def calc_feb():
    prompt.bot_say("Введіть число n")
    n = int(input('Користувач: '))
    feb_list = []
    i = 0
    while i < n:
        if i < 2:
            feb_list.append(1)
        else:
            current = feb_list[i - 1] + feb_list[i - 2]
            feb_list.append(current)

        i = i + 1
    prompt.bot_say(f"""Ваше число {feb_list[-1]}""")

def circle():
    prompt.bot_say("Введіть радіус кола.")
    circle_radius_respond = int(input('Користувач: '))
    print()
    prompt.bot_say("введіть чому дорівнює центральний кут виміряний у радіанах")
    central_corner_respond = float(input('Користувач: '))
    print()
    arc_length = circle_radius_respond * central_corner_respond
    prompt.bot_say(f"""Довжина дуги кола: {arc_length}""")