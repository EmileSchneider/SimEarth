import numpy as np

state = np.array = ([100, 200, 130, 1.05, 1.02, 0.75])

def function_food_growth(array):
    food_supplie = int((array[2:3])[0])
    fertility_of_land = int(array[1:2][0])
    population = int(array[0:1][0])
    fertility_factor = int(array[5:6][0])
    new_food = (fertility_of_land - fertility_factor * population) + food_supplie
    array[2:3] = [new_food]
    return array

def function_food_consumption(array):
    food_supplie = int(array[2:3][0])
    population = int(array[0:1][0])
    new_food = food_supplie - population
    array[2:3] = [new_food]
    return array

def function_deaths(array):
    population = int(array[0:1][0])
    death_rate = int(array[4:5][0])
    new_population = round(population / death_rate)
    array[0:1] = [new_population]
    return array

def function_births(array):
    population = int(array[0:1][0])
    birth_rate = int(array[3:4][0])
    new_population = round(population * birth_rate)
    array[0:1] = [new_population]
    return array

def calculate_average(array1, array2):
    if len(array1) != len(array2):
        print('Error')
    else:
        return (np.add(array1, array2) / 2 )

def Event_New_Day(array):
    a = function_food_consumption(array)
    b = function_food_growth(array)
    array = calculate_average(a, b)
    a = function_deaths(array)
    b = function_births(array)
    array = calculate_average(a, b)
    return array


