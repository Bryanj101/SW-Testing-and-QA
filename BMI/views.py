from django.shortcuts import render
from django.views import View
from .forms import BMICalculatorForm
from .models import BMICalculator
from django.http import JsonResponse
from django.template.loader import render_to_string

def bmi(request):
    if request.method == "POST":
        form = BMICalculatorForm(request.POST)
        if form.is_valid():
            weight = form.cleaned_data["weight"]
            height = form.cleaned_data["height"]
            bmi_calculator = BMICalculator(weight=weight, height=height)
            bmi_calculator.save()
            context = {
                'bmi': bmi_calculator.calculate_bmi(),
                'category': bmi_calculator.bmi_category(),
                "form": form,
            }
            return render(request, "BMI/index.html", context)
    else:
        form = BMICalculatorForm()
    return render(request, "BMI/index.html", {"form": form})
    