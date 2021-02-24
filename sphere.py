from math import sqrt
from vector import Vector

class Sphere:

    def __init__(self, center, radius, material):
        self.center = center
        self.radius = radius
        self.material = material

    def checkIfIntersects(self, ray):
        """
        In this function, we will check if a ray intersects with this sphere.Return distance in case of an intersection.
        Return None if no intersection.
        We will use discriminant formula but in our case "a" is always equal to 1 so i will not define "a".
        """

        sphereToRay = ray.origin.subVector(self.center)
        b = 2 * ray.direction.dotProduct(sphereToRay)
        c = sphereToRay.dotProduct(sphereToRay) - self.radius * self.radius
        discriminant = b * b - 4 * c

        if discriminant >= 0:
            dist = (-b - sqrt(discriminant)) / 2
            if dist > 0:
                return dist
        return None


    def surfaceNormal(self, sfPoint):
        """
        	Return the surface normal to the sphere at `pt`.
        """
        return (sfPoint.subVector(self.center)).normalizeVector()