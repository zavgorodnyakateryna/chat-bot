import astronomy_function
import general_function
import geography_function
import math_functions
import philology_function
import physics_function


def run(state):
    user_choice = "".join(map(str, state))
    match user_choice:
        case "11":
            math_functions.circle()
        case "12":
            math_functions.triangle()
        case "13":
            math_functions.calc_feb()
        case "14":
            math_functions.number_pi()
        case "21":
            physics_function.mass_energy()
        case "22":
            physics_function.different_energy()
        case "23":
            physics_function.planc()
        case "31":
            philology_function.diff_noun_adj()
        case "32":
            philology_function.ukr_cases()
        case "33":
            philology_function.what_philology()
        case "34":
            philology_function.branches_philology()
        case "41":
            geography_function.ocean()
        case "42":
            geography_function.sahara()
        case "43":
            geography_function.find_dot()
        case "44":
            geography_function.distance_dots()
        case "45":
            geography_function.climates()
        case "46":
            geography_function.ekvator()
        case "51":
            astronomy_function.earth_to_sun()
        case "52":
            astronomy_function.stars()
        case "53":
            astronomy_function.what_astronomy()
        case "54":
            astronomy_function.comets()
        case "61":
            general_function.what_time()
        case "62":
            general_function.what_year()
        case "63":
            general_function.guess_numb()
        case "64":
            general_function.game()




