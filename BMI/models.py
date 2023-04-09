from django.db import models

class BMICalculator(models.Model):
    weight = models.FloatField()
    height = models.FloatField()

    @property
    def weight_conversion(self):
        weight = self.weight * 0.45
        return weight

    @property
    #function to convert height value using metric conversion factor
    def height_conversion(self):
        height = self.height * 0.025
        return height
    
    @property
    #function to square the height value
    def height_squared(self):
        height = self.height_conversion ** 2
        height = round(height, 6)
        return height
    
    def calculate_bmi(self):
        bmi = self.weight_conversion / self.height_squared
        bmi = round(bmi, 1)
        return bmi

    def bmi_category(self):
        bmi = self.calculate_bmi()
        if bmi >= 18.5:
            if bmi <= 24.9:
                return "Normal weight"
            if 25 <= bmi <= 29.9:
                return "Overweight"
            else:
                return "Obese"
        else:
            return "Underweight"
    
    def __str__(self):
        return f"{self.weight} kg, {self.height} cm"
