# for num in range(0, 151):
#     print(num)

# for num in range(5, 1005, 5):
#     print(num)

# for num in range(1, 105):
#     if num % 10 == 0:
#         print(num, 'Coding Dojo')
#     elif num % 5 == 0:
#         print(num, 'Coding')

# total = 0
# for num in range(1, 500000):
#     if not num % 2 == 0:
#         total += num
# print(num)

# for num in range(2018, 0, -4):
#     print(num)

lowNum, highNum, multi = (2, 100, 4)
for num in range(lowNum, highNum):
    if num % multi == 0:
        print(num)


