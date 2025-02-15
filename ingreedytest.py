# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import pytest

from ingreedypy import Ingreedy

test_cases = {
    '1.0 cup flour': {
        'quantity': [{
            'amount': 1.0,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '1 1/2 cups flour': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '1 1/2 potatoes': {
        'quantity': [{
            'amount': 1.5,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'potatoes',
    },
    '12345 potatoes': {
        'quantity': [{
            'amount': 12345,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'potatoes',
    },
    '1 2/3 cups flour': {
        'quantity': [{
            'amount': round(float(5.0/3), 3),
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '1 2/3 cup(s) flour': {
        'quantity': [{
            'amount': round(float(5.0/3), 3),
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '1 2/3 C flour': {
        'quantity': [{
            'amount': round(float(5.0/3), 3),
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '1 2/3 C. flour': {
        'quantity': [{
            'amount': round(float(5.0/3), 3),
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '12 (6-ounce) boneless skinless chicken breasts': {
        'quantity': [{
            'amount': 72,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'boneless skinless chicken breasts',
    },
    '1 (28 ounce) can crushed tomatoes': {
        'quantity': [{
            'amount': 28,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'can crushed tomatoes',
    },
    '1/2 cups flour': {
        'quantity': [{
            'amount': 0.5,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '12g potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'gram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '12 gram(s) potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'gram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '12gram(s) potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'gram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '12G. potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'gram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '12G potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'gram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '12oz potatoes': {
        'quantity': [{
            'amount': 12,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'potatoes',
    },
    '12oz tequila': {
        'quantity': [{
            'amount': 12,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'tequila',
    },
    '1/2 potato': {
        'quantity': [{
            'amount': 0.5,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'potato',
    },
    '1.5 cups flour': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '1.5 potatoes': {
        'quantity': [{
            'amount': 1.5,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'potatoes',
    },
    '1 clove garlic, minced': {
        'quantity': [{
            'amount': 1,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'clove garlic, minced',
    },
    '1 cup flour': {
        'quantity': [{
            'amount': 1,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tablespoons flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tablespoon(s) flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tablespoons flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tbspns. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tbspns flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 Tbsp. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 Tbsp flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tbsp. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tbsp flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 TBS. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 TBS flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 Tbs. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 Tbs flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 teaspoons flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 teaspoon(s) flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 teaspoon flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 teasps. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 teasps flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 teasp. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 teasp flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tsp. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 tsp flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 t. flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '6 t flour': {
        'quantity': [{
            'amount': 6,
            'unit': 'teaspoon',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '1 garlic clove, sliced in 1/2': {
        'quantity': [{
            'amount': 1,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'garlic clove, sliced in 1/2',
    },
    '1 tablespoon (3 teaspoons) Sazon seasoning blend (recommended: Goya) with Mexican and Spanish foods in market': {
        'quantity': [{
            'amount': 1,
            'unit': 'tablespoon',
            'unit_type': 'english',
        }],
        'ingredient': 'Sazon seasoning blend (recommended: Goya) with Mexican and Spanish foods in market',
    },
    '2 (28 ounce) can crushed tomatoes': {
        'quantity': [{
            'amount': 56,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'can crushed tomatoes',
    },
    '.25 cups flour': {
        'quantity': [{
            'amount': 0.25,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    '2 cups of potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'potatoes',
    },
    '1 egg': {
        'quantity': [{
            'amount': 1.0,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'egg',
    },
    '2 eggs, beaten': {
        'quantity': [{
            'amount': 2,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'eggs, beaten',
    },
    '3 28 ounce cans of crushed tomatoes': {
        'quantity': [{
            'amount': 84,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'cans of crushed tomatoes',
    },
    '5 3/4 pinches potatoes': {
        'quantity': [{
            'amount': 5.75,
            'unit': 'pinch',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'potatoes',
    },
    '.5 potatoes': {
        'quantity': [{
            'amount': 0.5,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'potatoes',
    },
    'a cup of flour': {
        'quantity': [{
            'amount': 1,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    'ground black pepper to taste': {
        'quantity': [],
        'ingredient': 'ground black pepper to taste',
    },
    'one 28 ounce can crushed tomatoes': {
        'quantity': [{
            'amount': 28,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'can crushed tomatoes',
    },
    'one cup flour': {
        'quantity': [{
            'amount': 1,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': 'flour',
    },
    'three 28 ounce cans crushed tomatoes': {
        'quantity': [{
            'amount': 84,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'cans crushed tomatoes',
    },
    'two 28 ounce cans crushed tomatoes': {
        'quantity': [{
            'amount': 56,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'cans crushed tomatoes',
    },
    'two five ounce can crushed tomatoes': {
        'quantity': [{
            'amount': 10,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'can crushed tomatoes',
    },
    '1kg / 2lb 4oz potatoes': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilogram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '1 kilogram(s) / 2lb 4oz potatoes': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilogram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '1KG. / 2lb 4oz potatoes': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilogram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '1KG / 2lb 4oz potatoes': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilogram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '1Kg. / 2lb 4oz potatoes': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilogram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '1Kg / 2lb 4oz potatoes': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilogram',
            'unit_type': 'metric',
        }],
        'ingredient': 'potatoes',
    },
    '2lb 4oz potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'pound',
            'unit_type': 'english',
        }, {
            'amount': 4,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'potatoes',
    },
    '2 pound(s) potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'pound',
            'unit_type': 'english',
        }],
        'ingredient': 'potatoes',
    },
    '2 # potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'pound',
            'unit_type': 'english',
        }],
        'ingredient': 'potatoes',
    },
    '2 pound. potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'pound',
            'unit_type': 'english',
        }],
        'ingredient': 'potatoes',
    },
    '2lb 4oz (1kg) potatoes': {
        'quantity': [{
            'amount': 2,
            'unit': 'pound',
            'unit_type': 'english',
        }, {
            'amount': 4,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'potatoes',
    },
    '1-1/2 ounce vanilla ice cream': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'vanilla ice cream',
    },
    '1-1/2 ounce(s) vanilla ice cream': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'vanilla ice cream',
    },
        '1-1/2 ounce. vanilla ice cream': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'vanilla ice cream',
    },
    '1-½ ounce vanilla ice cream': {
        'quantity': [{
            'amount': 1.5,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'vanilla ice cream',
    },
    'apple': {
        'quantity': [],
        'ingredient': 'apple',
    },
    '3-⅝ ounces, weight feta cheese, crumbled/diced': {
        'quantity': [{
            'amount': 3.625,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'weight feta cheese, crumbled/diced',
    },
    '16-ounce can of sliced pineapple': {
        'quantity': [{
            'amount': 16,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 'can of sliced pineapple',
    },
    '750ml/1 pint 7fl oz hot vegetable stock': {
        'quantity': [{
            'amount': 750,
            'unit': 'milliliter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '750 milliliters/1 pint 7fl oz hot vegetable stock': {
        'quantity': [{
            'amount': 750,
            'unit': 'milliliter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '750 milliliter(s)/1 pint 7fl oz hot vegetable stock': {
        'quantity': [{
            'amount': 750,
            'unit': 'milliliter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '750mls./1 pint 7fl oz hot vegetable stock': {
        'quantity': [{
            'amount': 750,
            'unit': 'milliliter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '750mls/1 pint 7fl oz hot vegetable stock': {
        'quantity': [{
            'amount': 750,
            'unit': 'milliliter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 liters hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'liter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 liter(s) hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'liter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 L. hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'liter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 L hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'liter',
            'unit_type': 'metric',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 pint hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'pint',
            'unit_type': 'english',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 pint(s) hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'pint',
            'unit_type': 'english',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 pint. hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'pint',
            'unit_type': 'english',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 quarts hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'quart',
            'unit_type': 'english',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 quart(s) hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'quart',
            'unit_type': 'english',
        }],
        'ingredient': 'hot vegetable stock',
    },
    '3 quart. hot vegetable stock': {
        'quantity': [{
            'amount': 3,
            'unit': 'quart',
            'unit_type': 'english',
        }],
        'ingredient': 'hot vegetable stock',
    },
    'pinch salt': {
        'quantity': [{
            'amount': 1,
            'unit': 'pinch',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'salt',
    },
    'stick cinnamon': {
        'quantity': [{
            'amount': 1,
            'unit': 'stick',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'cinnamon',
    },
    '3 sticks cinnamon': {
        'quantity': [{
            'amount': 3,
            'unit': 'stick',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'cinnamon',
    },
    'head lettuce': {
        'quantity': [{
            'amount': 1,
            'unit': 'head',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'lettuce',
    },
    '4 heads lettuce': {
        'quantity': [{
            'amount': 4,
            'unit': 'head',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'lettuce',
    },
    'punnet raspberries': {
        'quantity': [{
            'amount': 1,
            'unit': 'punnet',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'raspberries',
    },
    '2 punnets raspberries': {
        'quantity': [{
            'amount': 2,
            'unit': 'punnet',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'raspberries',
    },
    '3 punnetts raspberries': {
        'quantity': [{
            'amount': 3,
            'unit': 'punnet',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'raspberries',
    },
    '4 punnett raspberries': {
        'quantity': [{
            'amount': 4,
            'unit': 'punnet',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'raspberries',
    },
    '4 heads lettuce': {
        'quantity': [{
            'amount': 4,
            'unit': 'head',
            'unit_type': 'imprecise',
        }],
        'ingredient': 'lettuce',
    },
    '4 (16 ounce) t-bone steaks, at room temperature': {
        'quantity': [{
            'amount': 64,
            'unit': 'ounce',
            'unit_type': 'english',
        }],
        'ingredient': 't-bone steaks, at room temperature',
    },
    '5 g': {
        'quantity': [{
            'amount': 5,
            'unit': 'gram',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '5 milligrams': {
        'quantity': [{
            'amount': 5,
            'unit': 'milligram',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '5 milligram(s)': {
        'quantity': [{
            'amount': 5,
            'unit': 'milligram',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '5 mgs.': {
        'quantity': [{
            'amount': 5,
            'unit': 'milligram',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '5 mgs': {
        'quantity': [{
            'amount': 5,
            'unit': 'milligram',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '30 cal': {
        'quantity': [{
            'amount': 30,
            'unit': 'calorie',
            'unit_type': 'english',
        }],
        'ingredient': None,
    },
    '2.5 kcal': {
        'quantity': [{
            'amount': 2.5,
            'unit': 'calorie',
            'unit_type': 'english',
        }],
        'ingredient': None,
    },
    '50 joules': {
        'quantity': [{
            'amount': 50,
            'unit': 'joule',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '50 joule(s)': {
        'quantity': [{
            'amount': 50,
            'unit': 'joule',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '1 kJ': {
        'quantity': [{
            'amount': 1,
            'unit': 'kilojoule',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '3 kilojoule(s)': {
        'quantity': [{
            'amount': 3,
            'unit': 'kilojoule',
            'unit_type': 'metric',
        }],
        'ingredient': None,
    },
    '20 gallons.': {
        'quantity': [{
            'amount': 20,
            'unit': 'gallon',
            'unit_type': 'english',
        }],
        'ingredient': None,
    },
    '20 gallons. bananas': {
        'quantity': [{
            'amount': 20,
            'unit': 'gallon',
            'unit_type': 'english',
        }],
        'ingredient': 'bananas',
    },
    '20 gallon bananas': {
        'quantity': [{
            'amount': 20,
            'unit': 'gallon',
            'unit_type': 'english',
        }],
        'ingredient': 'bananas',
    },
    '20 gallon. bananas': {
        'quantity': [{
            'amount': 20,
            'unit': 'gallon',
            'unit_type': 'english',
        }],
        'ingredient': 'bananas',
    },
    '20 gallon(s) bananas': {
        'quantity': [{
            'amount': 20,
            'unit': 'gallon',
            'unit_type': 'english',
        }],
        'ingredient': 'bananas',
    },
    '6 (thinly sliced) bananas': {
        'quantity': [{
            'amount': 6,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'bananas',
    },
    '6 (1/2 inch thick) slices Italian bread': {
        'quantity': [{
            'amount': 6,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'slices Italian bread',
    },
    '1⁄2 orange': {
        'quantity': [{
            'amount': 0.5,
            'unit': None,
            'unit_type': None,
        }],
        'ingredient': 'orange',
    },
    '2 cups 1%-fat milk': {
        'quantity': [{
            'amount': 2,
            'unit': 'cup',
            'unit_type': 'english',
        }],
        'ingredient': '1%-fat milk',
    },
    # '2 PL cukr': {
    #     'quantity': [{
    #         'amount': 2,
    #         'unit': 'PL',
    #         'unit_type': 'abbreviated',
    #     }],
    #     'ingredient': 'cukr',
    # },
}


@pytest.mark.parametrize('description,expectation', test_cases.items())
def test_parser(description, expectation):
    result = Ingreedy().parse(description)
    for key in expectation:
        assert result[key] == expectation[key]
