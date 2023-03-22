from sys import exit

class BMICalculator:
    def __init__(self):
        self.weight = 0
        self.height = 0
        self.bmi = 0
    
    #function for weight prompt
    def weight_prompt(self):
        try:
            self.weight = int(input("Enter your weight in pounds: "))
            return self.weight
        except Exception:
            exit("Please enter value a whole value. (example 125)")
            
    #function for height prompt  
    def height_prompt(self):
        try:
            self.height = int(input("Enter your height in inches: "))
            return self.height
        except Exception:
            exit("Please enter value a whole value. (example 70)")
    
    #function to convert weight value using metric conversion factor
    def weight_conversion(self):
        self.weight = self.weight * 0.45
        return self.weight

    #function to convert height value using metric conversion factor
    def height_conversion(self):
        self.height = self.height * 0.025
        return self.height

    #function to square the height value
    def height_squared(self):
        self.height = self.height ** 2
        self.height = round(self.height, 6)
        return self.height
    
    #function for bmi calculation
    def bmi_calculation(self):
        self.bmi = self.weight / self.height
        self.bmi = round(self.bmi, 1)
        return self.bmi
    
    #function for bmi categorization
    def bmi_category(self):
        if self.bmi >= 18.5:
            if self.bmi <= 24.9:
                return "Normal weight"
            if 25 <= self.bmi <= 29.9:
                return "Overweight"
            else:
                return "Obese"
        else:
            return "Underweight"



def main():
   
    #create object
    bmi = BMICalculator()
    #prompt user to input weight
    bmi.weight_prompt()
    #prompt user to input height
    bmi.height_prompt()
    #use metric conversion factor on weight
    bmi.weight_conversion()
    #use metric conversion factor on height
    bmi.height_conversion()
    #square the height value
    bmi.height_squared()
    #calculate bmi using height and weight values
    bmi.bmi_calculation()
    #return bmi categorization
    print("BMI = ", bmi.bmi)
    return bmi.bmi_category()
    
if __name__ == "__main__":
    print("\nSimple BMI Calculator")
    print("-" * 100)
    print(main())
    