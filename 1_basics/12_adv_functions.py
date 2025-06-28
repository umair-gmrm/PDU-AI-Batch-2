
def greet_many_times(name:str , times:int):
    message = f"Hi {name}, How are you?"
    for i in range(times):
        print(i , message , sep=") ")

greet_many_times(times=20 , name="Umair")

def add_these_numbers(*numbers):
    total = 0
    for v in numbers:
        total = total + v

    return total


my_total = add_these_numbers(1,2,3,4)
print(my_total)



def key_word_arge(**kwarg):
    print(kwarg)


key_word_arge(hi=1 , test= 2)








