from color import Color
class Image:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        #!!Change this
        self.pixels = [
            [None for _ in range(self.width)] for _ in range(self.height)
        ]

    def setPixel(self, x, y, color):
        self.pixels[y][x] = color

    def wholePpm(self, imgFile):
        Image.pixelsToPpmHeader(imgFile,self.width,self.height)
        self.pixelsToPpmActual(imgFile)

    @staticmethod
    def pixelsToPpmHeader(imgFile, width=None, height=None):
        imgFile.write("P3 {} {}\n255\n".format(width, height))


    def pixelsToPpmActual(self, imgFile):
        def rgbValues(value):
            return round(max(min(value * 255, 255), 0))

        #backup: imgFile.write("P3 {} {}\n255\n".format(self.width, self.height))
        for row in self.pixels:
            for color in row:
                #Whitespace is very important. If you do not add this you will experience an error.
                imgFile.write(
                    "{} {} {} ".format(
                        rgbValues(color.x), rgbValues(color.y), rgbValues(color.z)
                    )
                )
            imgFile.write("\n")