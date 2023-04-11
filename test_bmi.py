from bmi import BMICalculator
from bmi import main
import pytest

def test_weight_input_as_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    prompt = BMICalculator().weight_prompt()
    assert prompt == 1
    
    
def test_weight_input_as_float(monkeypatch):
    with pytest.raises(Exception):
        monkeypatch.setattr('builtins.input', lambda _: 1.1)
        prompt = BMICalculator().weight_prompt()
        assert prompt == 1.1
   
    
def test_weight_input_str_exception(monkeypatch):
    with pytest.raises(SystemExit):
        monkeypatch.setattr('builtins.input', lambda _: "a")
        prompt = BMICalculator().weight_prompt()
        assert prompt == "a"

def test_weight_input_type_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    prompt = BMICalculator().weight_prompt()
    assert prompt == isinstance(prompt, int)
   
    
def test_height_input_as_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    prompt = BMICalculator().height_prompt()
    assert prompt == 1

def test_height_input_as_float(monkeypatch):
    with pytest.raises(Exception):
        monkeypatch.setattr('builtins.input', lambda _: 1.1)
        prompt = BMICalculator().height_prompt()
        assert prompt == 1.1
 
def test_height_input_str_exception(monkeypatch):
    with pytest.raises(SystemExit):
        monkeypatch.setattr('builtins.input', lambda _: "a")
        prompt = BMICalculator().height_prompt()
        assert prompt == "a"

def test_height_input_type_int(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    prompt = BMICalculator().height_prompt()
    assert isinstance(prompt, int) 
      
def test_weight_conversion_true(monkeypatch):
    value = BMICalculator()
    value.weight = 1
    value.weight_conversion()
    assert value.weight == 0.45

def test_weight_conversion_false(monkeypatch):
    with pytest.raises(AssertionError):
        value = BMICalculator()
        value.weight = 0
        value.weight_conversion()
        assert value.weight == 0.45

def test_weight_conversion_type_float(monkeypatch):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    value = BMICalculator().weight_conversion()
    assert isinstance(value, float)

def test_height_conversion_true():
    value = BMICalculator()
    value.height = 1
    value.height_conversion()
    assert value.height == 0.025

def test_height_conversion_false():
    with pytest.raises(AssertionError):
        value = BMICalculator()
        value.height = 0
        value.height_conversion()
        assert value.height == 0.025

def test_height_conversion_type_float():
    value = BMICalculator()
    value.height = 1
    value.height_conversion()
    assert isinstance(value.height, float)

def test_height_squared_true():
    value = BMICalculator()
    value.height = 0.025
    value.height_squared()
    assert value.height == 0.000625

def test_height_squared_false():
    with pytest.raises(AssertionError):
        value = BMICalculator()
        value.height = 0
        value.height_squared()
        assert value.height == 0.000625

def test_height_squared_type_float():
    value = BMICalculator()
    value.height = 0.025
    value.height_squared()
    assert isinstance(value.height, float) 

def test_bmi_calculation_true():
    value = BMICalculator()
    value.weight = 0.45
    value.height = 0.000625
    value.bmi_calculation()
    assert value.bmi == 720

def test_bmi_calculation_false():
    with pytest.raises(AssertionError):
        value = BMICalculator()
        value.weight = 0.45
        value.height = 0.000625
        value.bmi_calculation()
        assert value == 0

def test_bmi_calculation_type_float():
    value = BMICalculator()
    value.weight = 0.45
    value.height = 0.000625
    value.bmi_calculation()
    assert isinstance(value.bmi, float)
    
def test_bmi_catergory_under():
    value = BMICalculator()
    value.bmi = 18.4
    assert value.bmi_category() == "Underweight"

def test_bmi_catergory_under_open():
    value = BMICalculator()
    value.bmi = 5
    assert value.bmi_category() == "Underweight"
        
def test_bmi_catergory_normal_lower_bound():
    value = BMICalculator()
    value.bmi = 18.5
    assert value.bmi_category() == "Normal weight"

    
def test_bmi_catergory_normal_interior():
    value = BMICalculator()
    value.bmi = 22.5
    assert value.bmi_category() == "Normal weight"

def test_bmi_catergory_normal_upper_bound():
    value = BMICalculator()
    value.bmi = 24.9
    assert value.bmi_category() == "Normal weight"

        
def test_bmi_catergory_over_lower_bound():
    value = BMICalculator()
    value.bmi = 25
    assert value.bmi_category() == "Overweight"

    
def test_bmi_catergory_over_interior():
    value = BMICalculator()
    value.bmi = 27.5
    assert value.bmi_category() == "Overweight"
    
def test_bmi_catergory_over_upper_bound():
    value = BMICalculator()
    value.bmi = 29.9
    assert value.bmi_category() == "Overweight"
    
def test_bmi_catergory_obese():
    value = BMICalculator()
    value.bmi = 30
    assert value.bmi_category() == "Obese"

def test_bmi_catergory_obese_open():
    value = BMICalculator()
    value.bmi = 35
    assert value.bmi_category() == "Obese"
    
def test_main(monkeypatch, capsys):
    monkeypatch.setattr('builtins.input', lambda _: 1)
    main()
    captured = capsys.readouterr()
    assert captured.out == "BMI =  720.0\n"