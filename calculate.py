import math_functions

def run(state):
    user_choice = "".join(map(str, state))
    match user_choice:
        case "11":
            math_functions.circle()
        case "13":
            math_functions.calc_feb()
