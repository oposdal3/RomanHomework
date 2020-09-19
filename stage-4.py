original = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def check(el, line):
    verification = 0
    for i in line:
        if i == el:
            verification += 1
    if verification == 1:
        return True
    else:
        return False


result = [el for el in original if check(el, original)]
print(result)
