def calculate_bmi(height, weight):
    print("Height = " + height)
    print("Weight = " + weight)
    bmi=weight/(height**2)
    if bmi<18.5:
        return -1
    if bmi>=18.5 and bmi<=25.0:
        return 0
    else:
        return 1
calculate_bmi(weight="57", height="1.73")