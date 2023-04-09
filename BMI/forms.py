from django import forms

class BMICalculatorForm(forms.Form):
    weight = forms.FloatField(label="Weight (lbs)", min_value=0)
    height = forms.FloatField(label="Height (in)", min_value=0)
