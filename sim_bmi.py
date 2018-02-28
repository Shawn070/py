_DEBUG = True
def debug_bmi(height, weight, gender):
    if _DEBUG == True:
        import pdb
        pdb.set_trace()
    if gender != 'male' and gender != 'female':
        print("input error!")
    elif gender == 'male':
        standard_weight = (height - 100)*0.9
    else:
        standard_weight = (height - 100)*0.9 - 2.5
    if weight <= (standard_weight*0.9):
        print("You BMI is -1")
    elif weight < (standard_weight*1.1):
        print("You BMI is 0")
    elif weight < (standard_weight*1.2):
        print("You BMI is 1")
    elif weight < (standard_weight*1.3):
        print("You BMI is 2")
    elif weight < (standard_weight*1.5):
        print("You BMI is 3")
    else:
        print("You BMI is 4")

if __name__ == "__main__":
    # print("Please input(height, weight, gender):")
    # body_index = input()
    # body_index = body_index.split()
    # body_index[0] = int(body_index[0])
    # body_index[1] = int(body_index[1])
    # debug_bmi(body_index[0], body_index[1], body_index[2])
    debug_bmi(160, 60, 'male')