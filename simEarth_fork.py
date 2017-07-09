import numpy as np

#state = np.array([100, 200, 130, 1.05, 1.02, 0.75])

    state = {"pop": 100 , "fos"; 200, "fol": 130, "bir": 1.05, "der": 1.02, "fef": 0.75}

def function_food_growth(array):
    food_supply = array[fos]
    fertility_of_land = array[fol]
    population = array[pop]
    fertility_factor = array[fef]
    new_food = (fertility_of_land - fertility_factor * population) + food_supply
    array[fos] = [new_food]
    return array

def function_food_consumption(array):
    food_supply = array[fos]
    population = array[pop]
    new_food = food_supply - population
    array[fos] = [new_food]
    return array

def function_deaths(array):
    population = array[pop]
    death_rate = array[der]
    new_population = round(population / death_rate)
    array[pop] = [new_population]
    return array

def function_births(array):
    population = array[pop]
    birth_rate = array[bir]
    new_population = round(population * birth_rate)
    array[pop] = [new_population]
    return array

# I need to rewrite this
def calculate_average(state1, state2):
    if state1.keys() != state2.keys():
        print('Error')
    else:
        dict = dict.fromkeys(state1.keys())
        for i in state1.keys():
            dict[i] = (state1[i] + state2[i]) / 2
        return dict

def Event_New_Day(array):
    a = function_food_consumption(array)
    b = function_food_growth(array)
    array = calculate_average(a, b)
    a = function_deaths(array)
    b = function_births(array)
    array = calculate_average(a, b)
    return array

