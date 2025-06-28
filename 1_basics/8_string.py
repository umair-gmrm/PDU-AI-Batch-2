
message_1 = "Hi, 'How' are  you doing!"
message_2 = 'Hi, "How" are  you doing!'
message_2 = '''Hi, How are you doing!'''


greeting = "Hi {name}, How are you?".format(name = "Umair")

print(greeting)


def greet(name):
    print("Hi {name}, How are you?".format(name=name))

greet("Kasun")