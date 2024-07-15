import signal
from time import sleep, time
from gpiozero import Button

from led_lights import LedLights, LedSection


LED_COUNT = 100  # count of all LEDs in strip
SECTION_SIZE = 12  # count of LEDs used for left and right section

BUTTON_MAIN = 27  # GPIO27 - Button for main LED section
BUTTON_LEFT = 17  # GPIO17 - Button for left LED section
BUTTON_RIGHT = 22  # GPIO22 - Button for left LED section

BUTTON_HOLD_TIME = 1  # hold time for long button press in seconds


class BedControl:
    def __init__(self, led_count, section_size, button_main, button_left, button_right):
        signal.signal(signal.SIGINT, self.cleanup)
        signal.signal(signal.SIGTERM, self.cleanup)
        self.lights = LedLights(led_count, section_size)
        self.buttons = {
            Button(button_main, pull_up=False): LedSection.MAIN,
            Button(button_left, pull_up=False): LedSection.LEFT,
            Button(button_right, pull_up=False): LedSection.RIGHT,
        }

    def run(self):
        self.lights.run()
        for button in self.buttons.keys():
            button.when_pressed = self.handle_button_press
        signal.pause()

    def cleanup(self, *args):
        self.lights.stop()

    def handle_button_press(self, button: Button):
        section = self.buttons[button]
        if self.lights.led_status[section]:
            push_time = time()
            while button.is_pressed:
                if time() - push_time > BUTTON_HOLD_TIME:
                    self.lights.set_section_off(section)
                    return
        self.lights.change_pattern(section)


if __name__ == "__main__":
    ctrl = BedControl(LED_COUNT, SECTION_SIZE, BUTTON_MAIN, BUTTON_LEFT, BUTTON_RIGHT)
    ctrl.run()
