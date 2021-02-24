from color import Color


class Light:

    #For simplicity, we can assume the color light to be white.
    def __init__(self, pos, color=Color.fromHex("#FFFFFF")):
        self.pos = pos
        self.color = color
