from math import ceil
from rpi_ws281x import Color


class Pattern:
    name = "unnamed pattern"
    pattern = []
    dynamic = False

    def get_frame(self, led_count):
        return self.pattern * ceil(led_count / len(self.pattern))


class SolidWhite(Pattern):
    name = "white 100%"
    pattern = [Color(0, 0, 0, 255)]


class SolidWhite50(Pattern):
    name = "white 50%"
    pattern = [Color(0, 0, 0, 128)]


class SolidWhite25(Pattern):
    name = "white 25%"
    pattern = [Color(0, 0, 0, 64)]


class SolidOrange(Pattern):
    name = "orange"
    pattern = [Color(128, 43, 0, 0)]


class SolidBlue(Pattern):
    name = "blue"
    pattern = [Color(0, 0, 255, 0)]


class SolidRedOrange(Pattern):
    name = "red/orange"
    pattern = [Color(255, 0, 0, 0), Color(255, 86, 0, 0)]


class SolidGreen(Pattern):
    name = "green"
    pattern = [Color(0, 255, 0, 0)]


class SolidRGB(Pattern):
    name = "RGB"
    pattern = [Color(255, 0, 0, 0), Color(0, 255, 0, 0), Color(0, 0, 255, 0)]


class SolidFire(Pattern):
    name = "Fire"
    pattern = [
        Color(11, 0, 0),
        Color(22, 0, 0),
        Color(86, 0, 0),
        Color(81, 5, 0),
        Color(75, 11, 0),
        Color(69, 17, 0),
        Color(64, 22, 0),
        Color(69, 17, 0),
        Color(75, 11, 0),
        Color(81, 5, 0),
        Color(86, 0, 0),
        Color(22, 0, 0),
    ]


class SolidAurora(Pattern):
    name = "Aurora"
    pattern = [
        Color(5, 0, 37),
        Color(0, 0, 42),
        Color(0, 10, 32),
        Color(0, 21, 21),
        Color(0, 32, 10),
        Color(0, 37, 5),
        Color(0, 32, 10),
        Color(0, 21, 21),
        Color(0, 10, 32),
        Color(0, 0, 42),
    ]


patterns_main = (
    SolidFire(),
    SolidAurora(),
    SolidOrange(),
    # SolidRedOrange(),
    # SolidBlue(),
    # SolidGreen(),
    # SolidRGB(),
)

patterns_section = (
    SolidWhite25(),
    SolidWhite50(),
    SolidWhite(),
)
