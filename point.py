from vector import Vector

#Since 3D points and RGB colors are effectively 3-element vectors, we simply
# declare them as  `Vector` class to take advantage of all its defined functions.

class Point(Vector):

    def __init__(self, x=0, y=0, z=0):
        super().__init__(x, y, z)