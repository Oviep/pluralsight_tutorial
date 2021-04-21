days_meal = [['eggs and bread', 'baked beans', 'hash browns'],
             ['beans and dodo', 'yam and fish stew', 'jollof rice and chicken'],
             ['steak and kidney beans', 'fish and chips', 'pizza']]
# print('The options for breakfast are:\t', days_meal[0], '\n The options for lunch are:\t',
#       days_meal[1], '\n and the options for dinner are:\t', days_meal[2])
# print(days_meal[0][0])

meals = {'Breakfast':['eggs and bread', 'baked beans', 'hash browns'],
             'Lunch':['beans and dodo', 'yam and fish stew', 'jollof rice and chicken'],
             'Dinner': ['steak and kidney beans', 'fish and chips', 'pizza']}
# print('The items on the breakfast list are: \t', meals['Breakfast'])
#
# for food in meals:
#     print(food)

for name, menu in meals.items():
    print(name, ':', menu)

person = {
    'name' : 'Jane Seymour',
    'age': 35,
    'city': 'Geneva',
    'job': 'sales girl'
}

print(person.get('name'), 'is', person.get('age'), 'years old, lives in ', person.get('city'), 'and works as a',
      person.get('job'))

