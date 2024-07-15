from time import sleep


def timer(time_in_seconds: int):
    while time_in_seconds:
        remaining_minutes = time_in_seconds // 60
        remaining_seconds = time_in_seconds % 60

        if remaining_minutes == 0:
            minutes = "00"
        elif remaining_minutes < 10:
            minutes = f"0{remaining_minutes}"
        elif remaining_minutes > 9:
            minutes = f"{remaining_minutes}"

        if remaining_seconds == 0:
            seconds = "00"
        elif remaining_seconds < 10:
            seconds = f"0{remaining_seconds}"
        elif remaining_seconds > 9:
            seconds = f"{remaining_seconds}"

        timer = f"  Timer: {minutes}:{seconds}"

        print(timer, end="\r")

        sleep(1)
        time_in_seconds -= 1
