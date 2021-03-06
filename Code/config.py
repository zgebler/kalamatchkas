"""
kalamatchkas.config
saba pilots
description:  configuration file for kalamatchkas program
"""


# file of foods to load
FOOD_PATH = "C:/Users/zgebl/Documents/dsi/GitHub/Kalamatchkas/Assets/ingredient_doron v21.xlsx"

# file to output recipes
OUT_DIREC = "C:/Users/zgebl/Documents/dsi/GitHub/Kalamatchkas/Output"

# file for food list
FOOD_LIST = "C:/Users/Doron/Desktop/Rehab/kalamatchkas/kalamachkas_project_files/meal_creation_files/food_list individual meals.csv"

# string used to begin each printed line
LINE_BEGIN = ">*~@~*> "

# basic fields to compare/display for any diet
BASE_FIELDS = ["protein_cal_%","carb_cal_%","fat_cal_%","total_cal"]

# fields to update in recipe making file
FIELDS_DONT_UPDATE = ['food_id','serving_size','max_grams_meal','max_grams_day']

# api key for searching usda database
API_KEY = "NzigPCefzEU9ewreg7xHSR5E1oW9xWVZQlX5vNEs"

# debug mode
DEBUG = False
