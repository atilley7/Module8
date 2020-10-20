def switch_average(key_val):
    switch = {
        'A': "one",
        'a': "one",
        'B': "two",
        'b': "two",
        'C':"three",
        'c':"three",
        'D':"four",
        'd':"four"

    }
    return switch.get(key_val)
