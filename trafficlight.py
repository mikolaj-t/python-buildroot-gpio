from gpiozero import LED
from enum import Enum

class State(Enum):
    RED = 1
    YELLOW = 2
    GREEN = 3

class TrafficLight:
    def __init__(self, green, yellow, red):
        self.green = LED(green)
        self.yellow = LED(yellow)
        self.red = LED(red)
        self.state = None

    def change_state(self, state):
        if state == State.RED:
            self.red.on()
            self.yellow.off()
            self.green.off()
        elif state == State.YELLOW:
            self.yellow.on()
            self.green.off()
            if self.state == State.RED:
                self.red.on()
            else:
                self.red.off()
        elif state == State.GREEN:
            self.red.off()
            self.yellow.off()
            self.green.on()
        self.state = state

    def change_to_opposite(self, state):
        if state == State.RED:
            self.change_state(State.GREEN)
        elif state == State.GREEN:
            self.change_state(State.RED)