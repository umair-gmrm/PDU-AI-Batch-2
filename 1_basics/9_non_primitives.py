'''
    Non Primitive Data Types:
        * list
        * tuple
        * dictionary
'''

list_1 = [1 , "Hi" , 1.2 ]
tuple_2 = (1, "Hi" , 1.2)

dic_1 = {
    "name": "Umair",
    "phone_no":  "0777",
    "fav_no": [1,2,3],
    "friends": ["A" , "B" , "C"]
}


list_a = [1, 2 , 3]
tuple_b = (5,6,7)

list_a.append(4)

print(list_a)
print(list_a[-1]) # 1
print(list_a[2]) 
print(list_a[1:-1])

list_a[0] = 10

print(list_a) # 

# tuple_b[0] = 12



print(dic_1["name"]) # Umair

dic_1["name"] = "Kasun"

print(dic_1)

