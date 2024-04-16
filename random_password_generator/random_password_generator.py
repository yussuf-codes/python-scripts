import random


def generate_random_password() -> str:
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['@', '#', '$', '%', '&']

    charList = []

    for _ in range(0, 6):
        charList.append(letters[random.randint(0, len(letters) - 1)])
        charList.append(numbers[random.randint(0, len(numbers) - 1)])
        charList.append(symbols[random.randint(0, len(symbols) - 1)])

    random.shuffle(charList)

    password = ''.join(charList)

    return password
