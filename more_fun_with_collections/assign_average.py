"""
Avery Tilley
10/19/20
Python switch case program
"""
def switch_average(key_val):
    switch = {
        'A': "one",
        'a': "one",
        'B': "two",
        'b': "two",
        'C': "three",
        'c': "three",
        'D': "four",
        'd': "four",
        'E': "five",
        'e': "five"

    }
    return switch.get(key_val, "invalid key")
