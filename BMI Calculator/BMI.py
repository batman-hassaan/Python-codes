# BMI Calculator in Python
# Developed by Hassaan

def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100  # Convert cm to meters
    bmi = weight_kg / (height_m ** 2)
    return bmi

def interpret_bmi(bmi):
    if bmi < 16:
        return "Severe Thinness"
    elif 16 <= bmi < 17:
        return "Moderate Thinness"
    elif 17 <= bmi < 18.5:
        return "Mild Thinness"
    elif 18.5 <= bmi < 25:
        return "Normal"
    elif 25 <= bmi < 30:
        return "Overweight"
    elif 30 <= bmi < 35:
        return "Obese Class I"
    elif 35 <= bmi < 40:
        return "Obese Class II"
    else:
        return "Obese Class III"

def main():
    print("=== Welcome to the BMI Calculator ===")
    try:
        height_cm = float(input("Enter your height in centimeters: "))
        weight_kg = float(input("Enter your weight in kilograms: "))

        if height_cm <= 0 or weight_kg <= 0:
            print("Error: Height and weight must be positive numbers.")
            return

        bmi = calculate_bmi(weight_kg, height_cm)
        category = interpret_bmi(bmi)

        print("\n----- Results -----")
        print(f"Your Body Mass Index (BMI) is: {bmi:.2f}")
        print(f"You are categorized as: {category}")
        print("-------------------")

    except ValueError:
        print("Invalid input. Please enter numeric values only.")

if __name__ == "__main__":
    main()
