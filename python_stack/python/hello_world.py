my_dict = {'name': 'Noelle', 'language': 'Python'}

for ke in my_dict:
    print(ke)

print(my_dict['name'])

for key in my_dict.keys():
    print(key)

for val in my_dict.values():
    print(val)

for key, val in my_dict.items():
    print(key, "=", val)


count = 0
while count < 5:
    print("looping -", count)
    count += 1

y = 3
while y > 0:
    print(y)
    y -= 1
else:
    print('Final else statement')
