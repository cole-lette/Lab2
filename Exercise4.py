def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def calc_average(temp_list):
    print("calc_average")
    count=0
    for i in range (0,-1):
        sum=sum+temp_list[1]
        count=count+1

    avg=sum/count
    return avg
    
def get_user_input():
    print("get_user_input")
    num= str(input("Enter numbers: "))
    numlist=num.split(",")
    for i in range(0,-1):
        numlist[i]=float(temp_list[i])
    return temp_list

def find_min_max(temp_list):
    print("find_min_max")
    min_temp=min(temp_list)
    max_temp=max(temp_list)
    min_max=[min_temp,max_temp]
    return min_max


def sort_temperature(temp_list):
    print("sort_temperature")
    sort_list= temp_list.sort()
    return sort_list

def calc_median_temperature(temp_list):
    sort_temperature()
    print("calc_median_temperature")
    median=len((temp_list)+1)/2
    median_temp=templist[median]
    return median_temp
def calc_average_temperature(temp_list):
    count=0
    for i in range (0,-1):
        sum=sum+temp_list[1]
        count=count+1

    avg=sum/count
    return avg
def calc_min_max_temperature(temp_list):
    temp_list.sort()
    min_num= temp_list[0]
    max_num=temp_list[-1]
    return min_num, max_num
#------------------------------------------------
display_main_menu()
temp_list=[]
temp_list=get_user_input()
find_min_max(temp_list)
sort_temperature(temp_list)
calc_median_temperature(temp_list)



