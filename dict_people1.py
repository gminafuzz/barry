people = {}
print ('Welcome to base of person!')
log = input('You want to add new person or watch base? (a/w):')

#-Input for data of new person ------
def data_input (dictionary_person):

    data_list = ('Lastname', 'Firstname', 'Gender', 'Occupation', 'Home planet')
    new_data = {}

    for data in data_list:
        new_data[data] = input('Input ' + data + ' of new person:')

    dictionary_person [new_data ['Lastname'] ] = new_data
    return dictionary_person
#------------------------------------

if log == 'a':
    while True:
        data_input(people)
        repead_input = input('Add another person? (y/n):')
        if repead_input == 'n':
            for person_name, person_date in people.items():
                print ('----Another person----')
                for parametr, info in person_date.items():
                    print(parametr, '', info)
            break
        else:
            continue
else:
    for person_date in people:
        for parametr, info in reson_date.items():
            print (parametr, '', info)



