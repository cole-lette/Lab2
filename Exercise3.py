def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")
# def calc_average():
#     print("calc_average")
def get_user_input():
    num= str(input("Enter numbers: "))
    numlist=num.split(",")
    for i in range(0,-1):
        numlist[i]=float(numlist[i])
    return numlist
# def find_min_max():
#     print("find_min_max")
# def sort_temperature():
#     print("sort_temperature")
# def calc_median_temperature():
#     print("calc_median_temperature")
display_main_menu()
get_user_input()

