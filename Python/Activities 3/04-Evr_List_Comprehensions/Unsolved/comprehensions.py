# @TODO: Your code here
fish = "halibut"

letters = []
for letter in fish:
    letters.append(letter)

print(letters)

letters = [letter for letter in fish]

print(letters)

capital_letters = []
for letter in fish:
    capital_letters.append(letter.upper())

print(letters)

capital_letters = [letter.upper() for letter in fish]

print(capital_letters)

july_temperatures = [87, 85, 92, 79, 106]
hot_days = []
for temperature in july_temperatures:
    if temperature in july_temperatures:
        if temperature > 90:
            hot_days.append(temperature)
print(hot_days)

hot_days = [temperature for temperature in july_temperatures if temperature > 90]

print(hot_days)