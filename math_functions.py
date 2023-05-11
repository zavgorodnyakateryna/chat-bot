import prompt
import math
def calc_feb():
    prompt.bot_say("Введіть число n")
    n = int(prompt.get_user_input())
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
    prompt.bot_say("Введіть радіус кола")

    circle_radius_respond = int(prompt.get_user_input())
    print()
    prompt.bot_say("Введіть чому дорівнює центральний кут виміряний у радіанах")
    central_corner_respond = float(prompt.get_user_input())
    print()
    arc_length = circle_radius_respond * central_corner_respond
    prompt.bot_say(f"""Довжина дуги кола: {arc_length}""")

def triangle():
        prompt.bot_say("Введіть координату Х першого вектора")
        first_x = float(prompt.get_user_input())
        print()

        prompt.bot_say("Введіть координату Y першого вектора")
        first_y = float(prompt.get_user_input())
        print()

        prompt.bot_say("Введіть координату Z першого вектора")
        first_z = float(prompt.get_user_input())
        print()

        prompt.bot_say("Введіть координату Х другого вектора")
        second_x = float(prompt.get_user_input())
        print()

        prompt.bot_say("Введіть координату Y другого вектора")
        second_y = float(prompt.get_user_input())
        print()

        prompt.bot_say("Бот: Введіть координату Z другого вектора")
        second_z = float(prompt.get_user_input())
        print()

        triangle_s = 1/2 * math.sqrt(
            (first_y * second_z - first_z * second_y)**2 +
            (first_z * second_x - first_x * second_z)**2 +
            (first_x * second_y - first_y * second_x)**2
        )
        prompt.bot_say(f"""Площа трикутника: {triangle_s}""")

def number_pi():
        prompt.bot_say("Число π дорівнює 3.14159265359 \nЗаокруглене значення числа пі дорівнює 3,14")