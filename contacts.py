contacts = {
    'number': 4,
    'students': [
        {'name': 'Ovie Oddiri', 'email': 'oviep@yahoo.com'},
        {'name': 'Bisi Folawiyo', 'email': 'bisi@yahoo.com'},
        {'name': 'Mamemo Ibru', 'email': 'mams@gmail.com'},
        {'name': 'Nathaniel Rothschild', 'email': 'nat@outlook.com'}
    ]
}
for students in contacts['students']:
    print(students['email'])