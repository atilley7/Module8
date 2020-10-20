"""
Avery Tilley
10/19/20
Program Checks if a query is in a dictionary(in_dict)
Program gets test scores and places them in a dictionary(get_test_scores)
Program averages scores
"""


def in_dict(d, element):
    return element in d


def get_test_scores():
    scores_dict = dict()
    num_scores = int(input("Type the number of test scores"))
    i = 0
    while i < num_scores:
        score = input("Type a test score between 0 and 100")
        if score.isdigit() and 0 <= int(score) <= 100:
            i = i + 1
            scores_dict.update({i: int(score)})
        else:
            print("invalid score retype score")
    return scores_dict


def average_scores(dict):
    total = 0

    for x in dict:
        total += dict[x]
    return total / len(dict)


if __name__ == '__main__':
    test_dict = get_test_scores()
    print(test_dict)
    print(average_scores(test_dict))
