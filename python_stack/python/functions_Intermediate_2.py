
# x = [[5, 2, 3], [10, 8, 9]]
# students = [
#      {'first_name':  'Michael', 'last_name': 'Jordan'},
#      {'first_name': 'John', 'last_name': 'Rosales'}
# ]
# sports_directory = {
#     'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
#     'soccer': ['Messi', 'Ronaldo', 'Rooney']
# }
# z = [{'x': 10, 'y': 20}]
#

# 1) Change the value 10 in x to 15. Once you're done, x should now be [ [5,2,3], [15,8,9] ].

# x[1][0] = 15
# print(x)

# 2) Change the last_name of the first student from 'Jordan' to 'Bryant'

# students[0]['last_name'] = 'Bryant'
# print(students)

# 3) In the sports_directory, change 'Messi' to 'Andres'

# sports_directory['soccer'][0] = 'Andres'
# print(sports_directory['soccer'])

# 4) Change the value 20 in z to 30

# z[0]['y'] = 30

# print(z)


students = [
         {'first_name':  'Michael', 'last_name': 'Jordan'},
         {'first_name': 'John', 'last_name': 'Rosales'},
         {'first_name': 'Mark', 'last_name': 'Guillen'},
         {'first_name': 'KB', 'last_name': 'Tonel'}
]


def iterateDictionary(student_list):

    # should output: (it's okay if each key-value pair ends up on 2 separate lines;
    # bonus to get them to appear exactly as below!)

    # Why does this method not return the last element (KB)?
    for i in range(0, len(student_list)-1):
        print("%s: first_name - %s, last_name - %s " % (i, student_list[i]['first_name'], student_list[i]['last_name']))

    # Why does this return None at the end?
    for x, student in enumerate(student_list):
        print("%s: first_name - %s, last_name - %s " % (x, student_list[x]['first_name'], student_list[x]['last_name']))


# 0: first_name - Michael, last_name - Jordan
# 1: first_name - John, last_name - Rosales
# 2: first_name - Mark, last_name - Guillen

# 0: first_name - Michael, last_name - Jordan
# 1: first_name - John, last_name - Rosales
# 2: first_name - Mark, last_name - Guillen
# 3: first_name - KB, last_name - Tonel
#None


# print(iterateDictionary(students))

def iterate_dictionary2(key_name, student_list):

    # Why does this return None at the end?
    for student in student_list:
        print(student[key_name])


# print(iterate_dictionary2('first_name', students))
# print(iterate_dictionary2('last_name', students))


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}


def print_info(list_info):

    location_count = len(list_info['locations'])
    instructors_count = len(list_info['instructors'])

    print(location_count, 'LOCATIONS:')
    for locations in list_info['locations']:
        print(locations)

    print()
    print(instructors_count, 'INSTRUCTORS:')
    for intructors in list_info['instructors']:
        print(intructors)


print_info(dojo)


# # output:
# 7 LOCATIONS
# San
# Jose
# Seattle
# Dallas
# Chicago
# Tulsa
# DC
# Burbank
#
# 8 INSTRUCTORS
# Michael
# Amy
# Eduardo
# Josh
# Graham
# Patrick
# Minh
# Devon




