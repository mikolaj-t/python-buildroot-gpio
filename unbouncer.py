from gpiozero import Button
from threading import Timer
import time

class Unbouncer:
    def __init__(self, stable_output_callback, tbmax):
        self.stable_output_callback = stable_output_callback
        self.last_state = None
        self.timer = None
        self.tbmax = tbmax

    def on_clicked(self, state):
        if self.last_state is None:
            print(f"Button pressed first time! {state}")
            self.set_state(state)
        elif state != self.last_state:
            print(f"Button pressed new state! {self.last_state} -> {state}")
            self.set_state(state)

    def set_state(self, state):
        self.last_state = state
        if self.timer is not None:
            self.timer.cancel()
        self.timer = Timer(self.tbmax, self.send_state, args=[state])
        self.timer.start()

    def send_state(self, state):
        self.stable_output_callback(state)
        self.last_state = None