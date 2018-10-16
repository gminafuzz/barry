people = {}
print ('Welcome to base of person!')
log = input('You want to add new person or watch base? (a/w):')

if log == 'a':
    while True:

        lastname = input('Input lastname of new person:')
        firstname = input('Input firstname of new person:')
        gender = input('Input gender of new person:')
        occupation = input('Input occupation of new person:')
        home = input('Input name of home planet this person ')

        name = ('{} {}'.format(firstname, lastname))
        people[lastname] = {'Name': name, 'Gender': gender, 'Occupation': occupation, 'Home planet': home}

        rec = input('Add another person? (y/n):')

        if rec == 'n':
            rec2 = input('You want waches base of person? (y/n):')
            if rec2 == 'y':
                for key, data in people.items():
                    print ('-------------------------')
                    for key, detail in data.items():
                        print (key, '______', detail)
                break
            else:
                break
        else: continue
else:
    print ('Goodbey')
