import matplotlib.pyplot as plt 
import numpy as np

def dicts_to_color_lists(potato_dict):
    potato_num = []
    color_vals = []
    for potato, vals in potato_dict.items():
            potato_num.append(potato)
            color_vals.append(vals[1])

    red_color_vals = []
    green_color_vals = []
    blue_color_vals = []
    for color in color_vals:
            red_color_vals.append(color[0])
            green_color_vals.append(color[1])
            blue_color_vals.append(color[2])
    return potato_num, red_color_vals, green_color_vals, blue_color_vals

def display_color(color, fresh, aged, potatoes):
        """
        color = String that represents the color
        fresh = list of floats that represent the color in fresh potatoes
        aged = list of floats that represent the color in aged potatoes
        potatoes = list of potato IDs (Strings)
        """

        potato_vals = {
        'Fresh': fresh,
        'Aged': aged,
        }

        x = np.arange(len(potatoes))  # the label locations
        width = 0.25 # the width of the bars
        multiplier = 0

        fig, ax = plt.subplots(figsize=(15, 4))

        for attribute, measurement in potato_vals.items():
                offset = width * multiplier
                rects = ax.bar(x + offset, measurement, width, label=attribute)
                multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Color Value')
        ax.set_title(f'{color} Color Value in Potatos')
        ax.set_xticks(x + width/2, potatoes)
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, 250)

        plt.show()

def get_mean_difference(fresh, aged):
        """
        fresh = list of floats that represent the color in fresh potatoes
        aged = list of floats that represent the color in aged potatoes
        """
        
        diffs = []
        for i in range(len(fresh)):
                diffs.append(fresh[i]-aged[i])
        print(np.mean(diffs))

def display_sol_color(color, sol, not_sol, fresh_sol, aged_sol, fresh_not_sol, aged_not_sol):
        """
        color = String that represents the color
        fresh_sol = list of floats that represent the color in fresh potatoes with solanine
        aged_sol = list of floats that represent the color in aged potatoes with solanine
        fresh_not_sol = list of floats that represent the color in fresh potatoes without solanine
        aged_not_sol = list of floats that represent the color in aged potatoes without solanine
        """

        fig, ax = plt.subplots(figsize =(15, 4))
        ax.bar(sol, fresh_sol, label="Solanine")
        ax.bar(not_sol, fresh_not_sol, label="No Solanine")

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Color Value')
        ax.set_title(f'{color} Color Value in Fresh Potatos')
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, 250)
        plt.show()

        fig, ax = plt.subplots(figsize =(15, 4))
        ax.bar(sol, aged_sol, label="Solanine")
        ax.bar(not_sol, aged_not_sol, label="No Solanine")

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Color Value')
        ax.set_title(f'{color} Color Value in Aged Potatos')
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, 250)
        plt.show()

def get_solanine_breakdown(solanine, not_solanine, aged_potatoes, fresh_potatoes):
    """
    solanine: list of Strings that represent potato IDs that have solanine 
    not_solanine: list of Strings that represent potato IDs that do not have solanine 
    aged_potatoes = list of floats that represent the color in aged potatoes
    fresh_potatoes = list of floats that represent the color in fresh potatoes
    """
    aged_red_sol_vals = []
    aged_green_sol_vals = []
    aged_blue_sol_vals = []

    fresh_red_sol_vals = []
    fresh_green_sol_vals = []
    fresh_blue_sol_vals = []
    for item in solanine:
        aged_colors = aged_potatoes[item][1]
        fresh_colors = fresh_potatoes[item][1]
        aged_red_sol_vals.append(aged_colors[0])
        aged_green_sol_vals.append(aged_colors[1])
        aged_blue_sol_vals.append(aged_colors[2])
        fresh_red_sol_vals.append(fresh_colors[0])
        fresh_green_sol_vals.append(fresh_colors[1])
        fresh_blue_sol_vals.append(fresh_colors[2])

    ## non_sol colors
    aged_red_non_sol_vals = []
    aged_green_non_sol_vals = []
    aged_blue_non_sol_vals = []

    fresh_red_non_sol_vals = []
    fresh_green_non_sol_vals = []
    fresh_blue_non_sol_vals = []
    for item in not_solanine:
        aged_colors = aged_potatoes[item][1]
        fresh_colors = fresh_potatoes[item][1]
        aged_red_non_sol_vals.append(aged_colors[0])
        aged_green_non_sol_vals.append(aged_colors[1])
        aged_blue_non_sol_vals.append(aged_colors[2])
        fresh_red_non_sol_vals.append(fresh_colors[0])
        fresh_green_non_sol_vals.append(fresh_colors[1])
        fresh_blue_non_sol_vals.append(fresh_colors[2])

    return aged_red_sol_vals, aged_green_sol_vals, aged_blue_sol_vals, fresh_red_sol_vals, fresh_green_sol_vals, fresh_blue_sol_vals, aged_red_non_sol_vals, aged_green_non_sol_vals, aged_blue_non_sol_vals, fresh_red_non_sol_vals, fresh_green_non_sol_vals, fresh_blue_non_sol_vals