slangs = {
    "IDK": "I don't know",
    "TBH": "To be honest",
    "LOL": "Laugh out Loud"
}

print(slangs["IDK"])

restaurant = {}
restaurant["McDonald"] = "Big Mac Burger"
restaurant["KFC"] = "Bucket o Chicken"
restaurant["Subway"] = "12 inch sub"
print(restaurant)
del restaurant["McDonald"]
print(restaurant)
restaurant["KFC"] = "McChicken sandwich"
print(restaurant)
restaurant['Tacobell'] = "hardshell chicken tacos"
zero = restaurant.get("Tacobell")
print(zero)

if zero:
    print("Tacobell is available")
else:
    print('Tacobell is absent')

print(restaurant)
print(restaurant['Tacobell'])