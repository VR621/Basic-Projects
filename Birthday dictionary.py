birthdays = {'Vick': 'Apr 28', 'James': 'March 17', 'Jad': 'Feb 13'}

while True:
    print('Enter a name: (blank to quit)')
    name = input().capitalize()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)
    else:
        print('I do not have birthday information for ' + name)
        print('When is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database updated.')
        
