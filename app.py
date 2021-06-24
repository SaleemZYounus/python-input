name = input('input name: ')
fav_color = input('What is your fav color? ')
print('Hi ' + name)
print(name + ' likes ' + fav_color)

birth_year = input('birthYear: ')
age = 2021 - int(birth_year)

# int() convert string to integer
# float() convert string to float(w/ decimal)
# bool() convert string to boolean value
# str() convert anything to st

print(age)

weight_lbs = input('weight(lbs): ')
weight_kg = float(weight_lbs) * 0.45351473922
weight_kg = str(weight_kg)
print(weight_kg)

print(name + ' is ' + weight_kg + ' kgs ')
