from color import Color


class Material:

    def __init__(self, color=Color(0xFF, 0xFF, 0xFF), specular=1.0, diffuse=1.0, ambient=0.05, reflection=0.5):
        self.color = color
        self.specular = specular
        self.diffuse = diffuse
        self.ambient = ambient
        self.reflection = reflection

    def colorAt(self, pos):
        return self.color
