from src import generate_random_password


def main() -> None:
	random_password = generate_random_password(16)
	print(random_password)


if __name__ == '__main__':
	main()
