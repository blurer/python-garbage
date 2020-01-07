#!/usr/bin/env python3

# BMI = (weight in kg / height in meters squared)
# LBS = BMI * 703

def gather_info():
    system = input("Are your measurements in metric or imperial units? ").lower().strip()
    height = float(input("What is your height? (inches or meters) "))
    weight = float(input("What is your weight? (pounds or kilograms) "))
    return (height, weight, system)

def calculate_bmi(weight, height, system='metric'):
    """
    Return the BMI for the given weight,
    height, and measurement system.
    """
    if system == 'metric':
        bmi = (weight / (height ** 2))
    else:
        bmi = 703 * (weight / (height ** 2))
    return bmi

while True:
    height, weight, system = gather_info()
    if system.startswith('i'):
         bmi = calculate_bmi(weight, system=system, height=height)
         print(f"Your BMI is {bmi}")
         break
    elif system.startswith('m'):
         bmi = calculate_bmi(weight, height)
         print(f"Your BMI is {bmi}")
    else:
         print("Error: Unknown measurement system.")
