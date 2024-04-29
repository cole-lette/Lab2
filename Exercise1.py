def calculate_bmi(height, weight):
    print("Height = " + height)
    print("Weight = " + weight)
    bmi=weight/(height**2)
    if bmi<18.5:
        print("Underweight")
    if bmi>=18.5 and bmi<=25.0:
        print("Normal Weight")
    else:
        print ("Overweight")

calculate_bmi(weight="57", height="1.73")