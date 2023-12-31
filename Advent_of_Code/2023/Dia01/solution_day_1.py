"""
File: solution_day_1.py
Author: Aloysio de Medeiros Winter
Date: 2023-12-20
Description: Solution of day one of Advent Of Code 2023.
"""

import re

word_to_number = {"one": 1 , "two" : 2 , "three" : 3 , "four" : 4 , "five" : 5 , "six" : 6 , "seven" : 7 , "eight" : 8 , "nine" : 9}

def transform_to_number(num):
    """
    Converts a numeric or string representation of a number into an integer.

    Parameters:
    - num (str or int): A numeric or string representation of a number.

    Returns:
    int: The integer representation of the input number.
    """
    global word_to_number

    return int(num) if num.isnumeric() else word_to_number[num]
   

def get_solution(pattern,input_file_name):
    """
    Solution of Advent of Code Day 1 part 1 and part 2 

    Parameters:
    - pattern (re.Pattern): The regular experssion to find digits in each line
    - input_file_name (str): The name of the input file to read

    Returns:
    - int: The solution of Advent of Code Day 1 
    """

    # Open the input file
    with open(input_file_name) as input_file:
        
        calibration_value_list = [] # List to store the calibration value of each line

        # Iterate over each line in the file
        for line in input_file:  
            line_digits = [digit.group() for digit in pattern.finditer(line)]#list of each digit in the line

            # Combining the first digit and the last digit to form a single two-digit number
            calibration_value_list.append((transform_to_number(line_digits[0])*10)+transform_to_number(line_digits[-1]))

        #return the sum of each calibration value
        return sum(calibration_value_list)


pattern_part_1 = re.compile(r'(\d)')
pattern_part_2 = re.compile(r'(one|two|three|four|five|six|seven|eight|nine|\d)')

input_file_name = 'input.txt'

print(f"part one: {get_solution(pattern_part_1,input_file_name)}")
print(f"part two: {get_solution(pattern_part_2,input_file_name)}")

    