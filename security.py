letters_allowed_small = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]
letters_allowed_big = [x.upper() for x in letters_allowed_small]
allowed_letters = letters_allowed_big + letters_allowed_small


def check_name(name):
    name = [str(x) for x in str(name)]
    check = all(letter in allowed_letters for letter in name)
    return check