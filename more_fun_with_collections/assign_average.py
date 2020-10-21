"""
Author
"""


def deans_list():
    return 'Welcome to the dean\'s list'


def grade():
    return 'Congratulations om receiving your final grade!'


def switch_average(entry):
    my_dict = {'A': deans_list(),
               'B': grade(),
               'C': grade(),
               'D': grade(),
               'F': grade()}
    result = my_dict.get(entry, lambda: 'This is not a valid key')
    return result


if __name__ == '__main__':
    my_function = switch_average('A')
    print(my_function)
