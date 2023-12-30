"""
File: solution_day_2.py
Author: Aloysio de Medeiros Winter
Date: 2023-12-30
Description: Solution of day two of Advent Of Code 2023.
"""
#The bag contain only this cubes
LOADED_BAG = {"red" : 12 , "green" : 13 , "blue" : 14}
COLORS = ["red","green","blue"]

INPUT_FILE_NAME = "advent_input.txt"

with open(INPUT_FILE_NAME) as input_file:
    
    sum_part_1 = 0
    sum_part_2 = 0

    # Each line of the file represent a game
    for line in input_file:
        posible_game = True

        # Separate game and ID
        id_game = line.split(":")

        # Separate the number ID
        id = int(id_game[0].split(" ")[1])
        
        # Separate the list of subsets of cubes that were revealed from the bag
        game_sets = id_game[1].split(";")

        # The fewest number of cubes of each color that could have been in the bag to make the game possible
        game_min = {color: 1 for color in COLORS}

        # For each subset revealed from the bag in a game
        for subset in game_sets:

            # Separate each number and color in a subset of the game
            colors = subset.split(",")

            for color_quantity in colors:
                quantity, color = color_quantity.strip().split(" ")
                quantity = int(quantity)

                # Check if the game is posible for part 1
                if quantity > LOADED_BAG[color]:
                    posible_game = False

                # Check if has a great color number in the bag for part 2
                if quantity > game_min[color]:
                     game_min[color] = quantity
    
        if posible_game:
            sum_part_1+=id

        sum_part_2+= game_min['red']*game_min['green']*game_min['blue']

    print(f"part 1 = {sum_part_1}")
    print(f"part 2 = {sum_part_2}")