# string

first_name= "Kaisher"
last_name = "Dev"
my_age = 25
print(first_name)
print(last_name)
print(my_age)

full_name = first_name + " " + last_name
print(full_name)

quote = "I'm team pyhton"
print(quote)

quote2 = 'She said "Hi"'
print(quote2)

# format

template = "Hi, my name is " + first_name + " and last name is " + last_name
print('v1: ',template)

template = "Hi my name is {} and my last name is {}".format(first_name,last_name)
print('v2: ', template)

template = f"Hello my name is {first_name} and last name is {last_name}"
print('v3: ', template)

template = f"Hello my name is {first_name} and last name is {last_name} and i have {my_age} years old"
print('v4: ', template)