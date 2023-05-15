import prompt
import math
def calc_feb():
    prompt.bot_say("Введіть число n")
    (command, n) = prompt.handle_input_as_int()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
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

    (command, circle_radius_respond) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    print()
    prompt.bot_say("Введіть чому дорівнює центральний кут виміряний у радіанах")
    (command, central_corner_respond) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    print()
    arc_length = circle_radius_respond * central_corner_respond
    prompt.bot_say(f"""Довжина дуги кола: {arc_length}""")

def triangle():
        prompt.bot_say("Введіть координату Х першого вектора")
        (command, first_x) = prompt.handle_input_as_float()
        if command == prompt.Command.BACK:
            return
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            exit(0)
        print()

        prompt.bot_say("Введіть координату Y першого вектора")
        (command, first_y) = prompt.handle_input_as_float()
        if command == prompt.Command.BACK:
            return
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            exit(0)
        print()

        prompt.bot_say("Введіть координату Z першого вектора")
        (command, first_z) = prompt.handle_input_as_float()
        if command == prompt.Command.BACK:
            return
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            exit(0)
        print()

        prompt.bot_say("Введіть координату Х другого вектора")
        (command, second_x) = prompt.handle_input_as_float()
        if command == prompt.Command.BACK:
            return
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            exit(0)
        print()

        prompt.bot_say("Введіть координату Y другого вектора")
        (command, second_y) = prompt.handle_input_as_float()
        if command == prompt.Command.BACK:
            return
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            exit(0)
        print()

        prompt.bot_say("Бот: Введіть координату Z другого вектора")
        (command, second_z) = prompt.handle_input_as_float()
        if command == prompt.Command.BACK:
            return
        if command == prompt.Command.EXIT:
            prompt.bot_say("Бувайте!")
            exit(0)
        print()

        triangle_s = 1/2 * math.sqrt(
            (first_y * second_z - first_z * second_y)**2 +
            (first_z * second_x - first_x * second_z)**2 +
            (first_x * second_y - first_y * second_x)**2
        )
        prompt.bot_say(f"""Площа трикутника: {triangle_s}""")

def number_pi():
        prompt.bot_say("Число π дорівнює 3.14159265359 \nЗаокруглене значення числа пі дорівнює 3,14")