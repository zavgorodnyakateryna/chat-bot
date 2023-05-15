import prompt
import math
def ocean():
    prompt.bot_say("Тихий океан є найбільшим за площею серед всіх океанів. \nВін займає більше половини всієї поверхні Землі, його площа становить більше 180 мільйонів квадратних кілометрів")

def sahara():
    prompt.bot_say("Сахара - це найбільша пустеля в світі, яка розташована в Північній Африці. \nВона простирається через 11 країн, включаючи Алжир, Чад, Єгипет, Лівію, Малі, Мавританію, Марокко, Нігер, Західну Сахару, Судан і Туніс")

def find_dot():
    prompt.bot_say("Бот: Введіть координату Х першої точки")
    (command, coordinate_x) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    prompt.bot_say("Введіть координату Y першої точки")
    (command, coordinate_y) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    prompt.bot_say("Введіть чому дорівнює відстань між точками")
    (command, distance_dots) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    prompt.bot_say("Введіть чому дорівнює азимут від першої точки до другої")
    (command, azimuth) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    azimuth_radians = math.radians(azimuth)
    unknown_x = coordinate_x + distance_dots * math.cos(azimuth_radians)
    unknown_y = coordinate_y + distance_dots * math.sin(azimuth_radians)
    prompt.bot_say("{unknown_x}, {unknown_y}")
def distance_dots():
    prompt.bot_say("Введіть координату Х першої точки")
    (command, first_coordinate_x) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    prompt.bot_say("Введіть координату Y першої точки")
    (command, first_coordinate_y) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    prompt.bot_say("Введіть координату X другої точки")
    (command, second_coordinate_x) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    prompt.bot_say("Введіть координату Y другої точки")
    (command, second_coordinate_y) = prompt.handle_input_as_float()
    if command == prompt.Command.BACK:
        return
    if command == prompt.Command.EXIT:
        prompt.bot_say("Бувайте!")
        exit(0)
    distance = math.sqrt((second_coordinate_x - first_coordinate_x) ** 2 + (second_coordinate_y - first_coordinate_y) ** 2)
    prompt.bot_say("Відстань між двома точками: {distance}")

def climates():
    prompt.bot_say("Головні типи клімату: \nТропічний \nСубтропічний \nЕкваторіальний \nСередземноморський \nМусонний \nПрибережний \nКонтинентальний \nАрктичний \nАнтарктичний")

def ekvator():
    prompt.bot_say("Екватор — уявне коло, проведене на поверхні планети на рівній відстані від обох географічних полюсів")