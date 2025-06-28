# alpha numbric ,contains _
# cannot start with number
# cannot contain space

def check_age(age:int):
    if age < 10:
        print("You are too young!")
    elif age < 30:
        print("You are okay!")
    else:
        print("You are too old!!")


check_age(10)
check_age(21)
check_age(50)