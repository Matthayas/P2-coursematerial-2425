class BMICalculator:
    def __init__(self, weight_in_kg, height_in_m):
        self.weight_in_kg = weight_in_kg
        self.height_in_m = height_in_m

    def bmi(self):
        return round(self.weight_in_kg / self.height_in_m**2, 1)

    def category(self):
        if self.bmi() < 18.5:
            return "underweight"
        elif self.bmi() < 25:
            return "normal"
        else:
            return "overweight"