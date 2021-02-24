from vector import Vector

#Since 3D points and RGB colors are effectively 3-element vectors, we simply
# declare them as  `Vector` class to take advantage of all its defined functions.
class Color(Vector):

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)

    @classmethod
    def fromHex(cls, hexcolor="#000000"):
        x = int(hexcolor[1:3], 16) / 255.0
        y = int(hexcolor[3:5], 16) / 255.0
        z = int(hexcolor[5:7], 16) / 255.0
        return cls(x,y,z)