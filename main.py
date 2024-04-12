
import threading
import time
from trafficlight import State, TrafficLight
from gpiozero import LED, Button
from unbouncer import Unbouncer
from pins import NORTH_GREEN, NORTH_YELLOW, NORTH_RED, SOUTH_GREEN, SOUTH_YELLOW, SOUTH_RED, EAST_GREEN, EAST_YELLOW, EAST_RED, WEST_GREEN, WEST_YELLOW, WEST_RED, BUTTON


def toggle_lights(north, south, east, west):
    north_south_state = north.state
    east_west_state = west.state

    north.change_state(State.YELLOW)
    south.change_state(State.YELLOW)
    east.change_state(State.YELLOW)
    west.change_state(State.YELLOW)

    time.sleep(2)

    north.change_to_opposite(north_south_state)
    south.change_to_opposite(north_south_state)
    east.change_to_opposite(east_west_state)
    west.change_to_opposite(east_west_state)


north = TrafficLight(NORTH_GREEN, NORTH_YELLOW, NORTH_RED)
south = TrafficLight(SOUTH_GREEN, SOUTH_YELLOW, SOUTH_RED)
east = TrafficLight(EAST_GREEN, EAST_YELLOW, EAST_RED)
west = TrafficLight(WEST_GREEN, WEST_YELLOW, WEST_RED)

north.change_state(State.GREEN)
south.change_state(State.GREEN)
east.change_state(State.RED)
west.change_state(State.RED)

button = Button(BUTTON)



# # Create an event for stopping the thread
# stop = threading.Event()
# # Create an event for the stable state
# stable_state = threading.Event()

# Create a timer
timer = None

def reset_timer():
    global timer
    timer.cancel()
    toggle_lights(north, south, east, west)
    timer = threading.Timer(5.0, reset_timer)
    timer.start()

timer = threading.Timer(5.0, reset_timer)
timer.start()

def on_stable_click(state: bool):
    global timer
    if state == True:
        return
    reset_timer()


unbouncer = Unbouncer(on_stable_click, 0.1)

button.when_pressed = unbouncer.on_clicked
button.when_released = unbouncer.on_clicked


# def worker():
#     while not stop.is_set():
#         # If the stable state is set, continue
#         if stable_state.is_set():
#             continue

#         # If the timer is done, toggle the lights and reset the timer
#         if not timer.is_alive():
#             print("Button pressed stable!", stable_state.is_set())
#             toggle_lights(north, south, east, west)
#             timer.cancel()
#             timer = threading.Timer(5.0, toggle_lights, args=[north, south, east, west])
#             timer.start()

#         # Sleep for a bit to prevent this loop from running too fast
#         sleep(0.1)


# Start the worker in a new thread
# thread = threading.Thread(target=worker)
# thread.start()

try:
    while True:
        pass
except KeyboardInterrupt:
    print("Application stopped by user.")