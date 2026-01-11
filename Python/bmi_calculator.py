"""
BMI (Body Mass Index) Calculator

This script calculates BMI based on weight and height inputs,
and categorizes the result into health categories:
- Underweight: BMI < 18.5
- Normal weight: 18.5 <= BMI < 25
- Overweight: 25 <= BMI < 30
- Obese: BMI >= 30
"""


def calculate_bmi(weight_kg, height_meters):
    """
    Calculates Body Mass Index (BMI).
    
    Args:
        weight_kg: Weight in kilograms
        height_meters: Height in meters
    
    Returns:
        BMI value (float)
    """
    return weight_kg / (height_meters ** 2)


def categorize_bmi(bmi):
    """
    Categorizes BMI into health categories.
    
    Args:
        bmi: BMI value
    
    Returns:
        Health category string
    """
    if bmi < 18.5:
        return "Underweight"
    elif 18.5 <= bmi < 25:
        return "Normal weight"
    elif 25 <= bmi < 30:
        return "Overweight"
    else:
        return "Obese"


def main():
    """Main function to get user input and calculate BMI."""
    print("BMI Calculator")
    print("-" * 30)
    
    try:
        weight = float(input("Enter your weight in kg: "))
        height = float(input("Enter your height in meters: "))
        
        if weight <= 0 or height <= 0:
            print("Error: Weight and height must be positive numbers")
            return
        
        bmi = calculate_bmi(weight, height)
        category = categorize_bmi(bmi)
        
        print(f"\nYour BMI is: {bmi:.1f}")
        print(f"Category: {category}")
    
    except ValueError:
        print("Error: Please enter valid numbers")
    except KeyboardInterrupt:
        print("\n\nProgram interrupted by user")


if __name__ == "__main__":
    main()
