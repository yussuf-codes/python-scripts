# from winsound import Beep
from . timer import timer

def focus(time_in_minutes: int):
    time_in_seconds = time_in_minutes * 60
    timer(int(time_in_seconds))
    # Beep(1000, 250)
