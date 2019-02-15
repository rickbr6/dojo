import random


def randInt(min=0, max=100):

    if min > max:
        print('Min', min, 'is greater than', max)
        return False
    elif max < 0:
        print('Max can not be a negative number')
        return False

    # No args provided, or only Max provided:
    if (min == 0 and max == 100) or (min == 0 and max < 100):
        return round(random.random() * max)

    # Only min provided, or Min and Max both provided
    else:
        return round(random.random() * (max-min) + min)


# print(randInt())
# print(randInt(max=500))
# print(randInt(min=-50))
# print(randInt(min=50, max=150))
# print(randInt(70, 40))


