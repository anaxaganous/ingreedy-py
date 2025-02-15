# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from parsimonious.grammar import Grammar
from parsimonious.nodes import NodeVisitor

number_value = {
    'a': 1,
    'an': 1,
    'zero': 0,
    'one': 1,
    'two': 2,
    'three': 3,
    'four': 4,
    'five': 5,
    'six': 6,
    'seven': 7,
    'eight': 8,
    'nine': 9,
    'ten': 10,
    'eleven': 11,
    'twelve': 12,
    'thirteen': 13,
    'fourteen': 14,
    'fifteen': 15,
    'sixteen': 16,
    'seventeen': 17,
    'eighteen': 18,
    'nineteen': 19,
    'twenty': 20,
    'thirty': 30,
    'forty': 40,
    'fifty': 50,
    'sixty': 60,
    'seventy': 70,
    'eighty': 80,
    'ninety': 90
}

unicode_fraction_value = {
    '¼': 1.0/4,
    '½': 1.0/2,
    '¾': 3.0/4,
    '⅐': 1.0/7,
    '⅑': 1.0/9,
    '⅒': 1.0/10,
    '⅓': 1.0/3,
    '⅔': 2.0/3,
    '⅕': 1.0/5,
    '⅖': 2.0/5,
    '⅗': 3.0/5,
    '⅘': 4.0/5,
    '⅙': 1.0/6,
    '⅚': 5.0/6,
    '⅛': 1.0/8,
    '⅜': 3.0/8,
    '⅝': 5.0/8,
    '⅞': 7.0/8
}


class Ingreedy(NodeVisitor):
    """Visitor that turns a parse tree into HTML fragments"""

    grammar = Grammar(
        """
        ingredient_addition = multipart_quantity alternative_quantity? break? ingredient? catch_all

        multipart_quantity
        = (quantity_fragment break?)*

        quantity_fragment
        = quantity
        / amount

        alternative_quantity
        = ~"[/]" break? multipart_quantity

        quantity
        = amount_with_conversion
        / amount_with_attached_units
        / amount_with_multiplier
        / amount_with_property
        / amount_imprecise

        # 4lb (900g)
        amount_with_conversion
        = amount break? unit !letter break parenthesized_quantity

        # 1 kg
        amount_with_attached_units
        = amount break? unit !letter

        # two (five ounce)
        amount_with_multiplier
        = amount break? parenthesized_quantity

        # four (1/2 size)
        amount_with_property
        = amount break? parenthesized_property

        # pinch
        amount_imprecise
        = imprecise_unit !letter

        # two (thinly sliced)
        amount_with_property
        = amount break? parenthesized_property

        parenthesized_quantity
        = open amount_with_attached_units close

        parenthesized_property
        = open amount? break? word (break word)* close

        amount
        = float
        / mixed_number
        / fraction
        / integer
        / number

        break
        = " "
        / comma
        / hyphen
        / ~"[\t]"

        separator
        = break
        / "-"

        ingredient
        = (word (break word)* catch_all)
        / (percentage ~"[- ]" word (break word)* catch_all)

        open = "("
        close = ")"

        word
        = letter+

        float
        = integer? ~"[.]" integer

        mixed_number
        = integer separator fraction

        fraction
        = multicharacter_fraction
        / unicode_fraction

        multicharacter_fraction
        = integer ~"[/⁄]" integer

        integer
        = ~"[0-9]+" !"%"

        percentage
        = ~"[1][0][0][%]"
        / ~"[1-9][0-9][%]"
        / ~"[0-9][%]"

        letter
        = ~"[a-zA-Z]"

        comma
        = ","

        hyphen
        = "-"

        unit
        = english_unit
        / metric_unit
        / imprecise_unit
        # / abbreviated_unit

        english_unit
        = calorie
        / cup
        / fluid_ounce
        / gallon
        / ounce
        / pint
        / pound
        / quart
        / tablespoon
        / teaspoon

        cup
        = "cups"
        / "cup(s)"
        / "cup"
        / "C."
        / "C"
        / "c."
        / "c"

        fluid_ounce
        = fluid break ounce

        fluid
        = "fluid"
        / "fl."
        / "fl"

        gallon
        = "gallons."
        / "gallons"
        / "gallon(s)"
        / "gallon."
        / "gallon"
        / "gal."
        / "gal"

        calorie
        = "calories"
        / "calorie"
        / "cal"
        / "kilocalories"
        / "kilocalorie"
        / "kCal"
        / "kcal"

        ounce
        = "ounces"
        / "ounce(s)"
        / "ounce."
        / "ounce"
        / "oz."
        / "oz"

        pint
        = "pints"
        / "pint(s)"
        / "pint."
        / "pint"
        / "pt."
        / "pt"

        pound
        = "pounds"
        / "pound(s)"
        / "pound."
        / "pound"
        / "lbs."
        / "lbs"
        / "lb."
        / "lb"
        / "#"

        quart
        = "quarts"
        / "quart(s)"
        / "quart."
        / "quart"
        / "qts."
        / "qts"
        / "qt."
        / "qt"

        tablespoon
        = "tablespoons"
        / "tablespoon(s)"
        / "tablespoon."
        / "tablespoon"
        / "tbspns."
        / "tbspns"
        / "Tbsp."
        / "Tbsp"
        / "tbsp."
        / "tbsp"
        / "TBS."
        / "TBS"
        / "Tbs."
        / "Tbs"
        / "tbs."
        / "tbs"
        / "T."
        / "T"

        teaspoon
        = "teaspoons"
        / "teaspoon(s)"
        / "teaspoon"
        / "teasps."
        / "teasps"
        / "teasp."
        / "teasp"
        / "tsp."
        / "tsp"
        / "t."
        / "t"

        metric_unit
        = gram
        / joule
        / kilogram
        / kilojoule
        / liter
        / milligram
        / milliliter

        gram
        = "grams"
        / "gram(s)"
        / "gram"
        / "gr."
        / "gr"
        / "G."
        / "G"
        / "g."
        / "g"

        joule
        = "joules"
        / "joule(s)"
        / "joule"
        / "j"

        kilogram
        = "kilograms"
        / "kilogram(s)"
        / "kilogram"
        / "KG."
        / "KG"
        / "Kg."
        / "Kg"
        / "kg."
        / "kg"

        kilojoule
        = "kilojoules"
        / "kilojoule(s)"
        / "kilojoule"
        / "kJ"
        / "kj"

        liter
        = "liters"
        / "liter(s)"
        / "liter"
        / "L."
        / "L"
        / "l."
        / "l"

        milligram
        = "milligrams"
        / "milligram(s)"
        / "milligram"
        / "mgs."
        / "mgs"
        / "mg."
        / "mg"

        milliliter
        = "milliliters"
        / "milliliter(s)"
        / "milliliter"
        / "mls."
        / "mls"
        / "ml."
        / "ml"

        imprecise_unit
        = dash
        / handful
        / pinch
        / touch
        / stick
        / punnet
        / head
        
        head
        = "heads"
        / "head"

        # abbreviated_unit
        # = letter letter letter?

        dash
        = "dashes"
        / "dash"

        handful
        = "handfuls"
        / "handful"

        pinch
        = "pinches"
        / "pinch"

        touch
        = "touches"
        / "touch"

        stick
        = "sticks"
        / "stick(s)"
        / "stick"

        punnet
        = "punnetts"
        / "punnett"
        / "punnets"
        / "punnet"

        number = written_number break

        written_number
        = "a"
        / "an"
        / "zero"
        / "one"
        / "two"
        / "three"
        / "four"
        / "five"
        / "six"
        / "seven"
        / "eight"
        / "nine"
        / "ten"
        / "eleven"
        / "twelve"
        / "thirteen"
        / "fourteen"
        / "fifteen"
        / "sixteen"
        / "seventeen"
        / "eighteen"
        / "nineteen"
        / "twenty"
        / "thirty"
        / "forty"
        / "fifty"
        / "sixty"
        / "seventy"
        / "eighty"
        / "ninety"

        unicode_fraction
        = ~"[¼]"u
        / ~"[½]"u
        / ~"[¾]"u
        / ~"[⅐]"u
        / ~"[⅑]"u
        / ~"[⅒]"u
        / ~"[⅓]"u
        / ~"[⅔]"u
        / ~"[⅕]"u
        / ~"[⅖]"u
        / ~"[⅗]"u
        / ~"[⅘]"u
        / ~"[⅙]"u
        / ~"[⅚]"u
        / ~"[⅛]"u
        / ~"[⅜]"u
        / ~"[⅝]"u
        / ~"[⅞]"u

        catch_all
        = ~".*"
        """)

    def visit_ingredient(self, node, visited_children):
        text = node.text
        if node.text.startswith('of '):
            text = text[3:]
        return text

    def visit_imprecise_unit(self, node, visited_children):
        return node.children[0].expr_name, 'imprecise'

    def visit_metric_unit(self, node, visited_children):
        return node.children[0].expr_name, 'metric'

    def visit_english_unit(self, node, visited_children):
        return node.children[0].expr_name, 'english'

    # def visit_abbreviated_unit(self, node, visited_children):
    #     return node.text, 'abbreviated'

    def visit_integer(self, node, visited_children):
        return int(node.text)

    def visit_multicharacter_fraction(self, node, visited_children):
        return float(visited_children[0]) / float(visited_children[2])

    def visit_unicode_fraction(self, node, visited_children):
        return unicode_fraction_value[node.text]

    def visit_fraction(self, node, visited_children):
        return round(visited_children[0], 3)

    def visit_mixed_number(self, node, visited_children):
        return float(visited_children[0]) + float(visited_children[2])

    def visit_float(self, node, visited_children):
        return float(node.text)

    def visit_multipart_quantity(self, node, visited_children):
        results = []
        for child in visited_children:
            unit, system, amount = child
            if results and not results[0]['unit']:
                amount *= results[0]['amount']
                results = []
            results.append({
                'unit': unit,
                'unit_type': system,
                'amount': amount
            })
        return results

    def visit_quantity_fragment(self, node, visited_children):
        return visited_children[0]

    def visit_amount(self, node, visited_children):
        return None, None, sum(visited_children)

    def visit_quantity(self, node, visited_children):
        return visited_children[0]

    def visit_amount_with_conversion(self, node, visited_children):
        _, _, amount = visited_children[0]
        unit, system, _ = visited_children[2]
        return unit, system, amount

    def visit_amount_with_attached_units(self, node, visited_children):
        _, _, amount = visited_children[0]
        unit, system, _ = visited_children[2]
        return unit, system, amount

    def visit_amount_with_multiplier(self, node, visited_children):
        _, _, multiplier = visited_children[0]
        unit, system, amount = visited_children[2]
        return unit, system, amount * multiplier

    def visit_amount_imprecise(self, node, visited_children):
        unit, system = visited_children[0]
        return unit, system, 1

    def visit_unit(self, node, visited_children):
        unit, system = visited_children[0]
        return unit, system, 1

    def visit_parenthesized_quantity(self, node, visited_children):
        unit, system, amount = visited_children[1]
        return unit, system, amount

    def visit_ingredient_addition(self, node, visited_children):
        return {
            'quantity': visited_children[0],
            'ingredient': visited_children[3]
        }

    def visit_number(self, node, visited_children):
        return visited_children[0]

    def visit_written_number(self, node, visited_children):
        return number_value[node.text]

    def generic_visit(self, node, visited_children):
        return visited_children[0] if visited_children else None
