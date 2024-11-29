import secrets
import pyperclip


def generate_random_password() -> None:
	random_password = secrets.token_urlsafe(18)
	pyperclip.copy(random_password)
	print("Copied!")
