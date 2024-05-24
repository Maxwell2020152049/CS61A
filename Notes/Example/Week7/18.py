class Lamb:
    species_name = "Lamb"
    scientific_name = "Ovis aries"

    def __init__(self, name):
        self.name = name

    def play(self):
        self.happy = True
        
    def __str__(self):
        return "🐑 : " + self.name
    def __repr__(self):
        return f"Lamb({repr(self.name)})"

lamb = Lamb("Lil")
owner = "Mary"
had_a_lamb = True
fleece = {"color": "white", "fluffiness": 100}
kids_at_school = ["Billy", "Tilly", "Jilly"]
day = 1

from fractions import Fraction

one_third = 1/3
one_half = Fraction(1, 2)

