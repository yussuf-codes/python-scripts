import string
import random
import pyperclip


def generate_random_password(length: int) -> str:
	characters: str = string.ascii_letters + string.digits
	random_password = ''.join(random.sample(characters, length))
	pyperclip.copy(random_password)
	print("Copied!")
	return random_password
