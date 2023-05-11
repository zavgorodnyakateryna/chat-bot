import prompt

def mass_energy():
        prompt.bot_say("Введіть масу тіла")
        mass_respond = float(prompt.user_say())
        print()
        energy_mass = mass_respond * 299792458 ** 2
        prompt.bot_say(f"""Бот: E = {energy_mass} дж/кг""")

def different_energy ():
        prompt.bot_say("Яку енергію ви хочете знайти? (кінетичну/потенціальну/внутрішню")
        energy_respond = prompt.user_say()
        if energy_respond.lower() == "кінетичну":
                prompt.bot_say("Введіть константу")
                for_kinetic_const = float(prompt.user_say())

                prompt.bot_say("Введіть значення потенціальної енергії")
                for_kinetic_potentional = float(prompt.user_say())

                prompt.bot_say("Введіть значення внутрішньої енергії")
                for_kinetic_internal = float(prompt.user_say())

                kinetic = for_kinetic_const - for_kinetic_internal - for_kinetic_potentional
                prompt.bot_say(f"""Екін = {kinetic} дж""")

        if energy_respond.lower() == "потенціальну":
                prompt.bot_say("Бот: Введіть константу")
                for_potentional_const = float(prompt.user_say())

                prompt.bot_say("Бот: Введіть значення кінетичної енергії")
                for_potentional_kinetic = float(prompt.user_say())

                prompt.bot_say("Введіть значення внутрішньої енергії")
                for_potentional_internal = float(prompt.user_say())

                potentional = for_potentional_const - for_potentional_kinetic - for_potentional_internal
                prompt.bot_say(f"""Епот = {potentional} дж""")

        if energy_respond.lower() == "внутрішню":
                prompt.bot_say("Введіть константу")
                for_internal_const = float(prompt.user_say())

                prompt.bot_say("Введіть значення кінетичної енергії")
                for_internal_kinetic = float(prompt.user_say())

                prompt.bot_say("Введіть значення потенціальної енергії")
                for_internal_potentional = float(prompt.user_say())

                internal = for_internal_const - for_internal_kinetic - for_internal_potentional
                prompt.bot_say(f"""Евнутр = {internal} дж""")

def planc():
        prompt.bot_say("Cтала Планка - це фундаментальна константа, яка визначає співвідношення між енергією кванту та частотою світла. \nЇї значення становить 6,62607015 × 10^-34 Дж/с.")
