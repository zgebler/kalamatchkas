DORONDIET = {
    "diet_name": "Doron's Diet",
    "meals": [('breakfast',500),('lunch',550),('dinner',750)],
    "calorie_error": .05,
    "nutrient_rules": [
            ('protein_cal_%',.15,.30),
            ('fat_cal_%',0,.25),
            ('carb_cal_%',.45,.60),
            ('sugar_cal_%',0,.10),
            ('fat_saturated_cal_%',0,.06),
            ('fiber',0,15),
            ('folate',400,1000),
            ('sodium',0,1137),
            ('vitamin_b12',3.75,1000000),
            ('riboflavin',1.3,400),
            ('phosphorus',700,4000),
            ('calcium',300,500),
            ('retinol',0,3000),
            ('provitamin_a',900,1000000),
    ],
    "foodgroup_rules": [
            ('vegetables',7,9),
            ('grains',4,8),
            ('proteins',1,6),
            ('fats',3,6),
            ('acids',1,3),
            ('condiments',1,9),

    ],
}

DORONDIET_OLD = {
    "diet_name": "Doron's Diet",
    "meals": [('breakfast',400),('lunch',700),('dinner',700)],
    "calorie_error": .05,
    "nutrient_rules": [
            ('protein_cal_%',.15,.30),
            ('fat_cal_%',.15,.25),
            ('carb_cal_%',.45,.60),
            ('sugar_cal_%',0,.10),
            ('fat_saturated_cal_%',0,.06),
            ('fiber',25,30),
            ('folate',400,1000),
            ('sodium',1000,2300),
            ('vitamin_b12',3.75,1000000),
            ('riboflavin',1.3,400),
            ('phosphorus',700,4000),
            ('calcium',300,800),
            ('retinol',0,3000),
            ('provitamin_a',900,1000000),
    ],
    "foodgroup_rules": [
            ('vegetables',7,9),
            ('grains',4,8),
            ('proteins',1,6),
            ('fats',0,6),
            ('acids',0,3),
    ],
}

TESTDIET = {
    "diet_name": "Test Diet",
    "meals": [('breakfast',400),('lunch',700),('dinner',700)],
    "calorie_error": .05,
    "nutrient_rules": [
            ('protein_cal_%',.15,.30),
            ('fat_cal_%',.15,.25),
            ('carb_cal_%',.45,.60),
            ('sugar_cal_%',0,.10),
            ('fiber',25,30),
    ],
    "foodgroup_rules": [
            ('vegetables',7,9),
            ('grains',4,8),
            ('proteins',1,6),
            ('fats',0,6),
            ('acids',0,3),
    ],
}