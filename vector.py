

class Vector():

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self.y = y
        self.z = z

    def magnitudeOfVector(self):
        return (self.x ** 2 + self.y ** 2 + self.z ** 2) ** 0.5

    def normalizeVector(self):
        return self.divideVector(self.magnitudeOfVector())

    def dotProduct(self, secondVector):
        return self.x * secondVector.x + self.y * secondVector.y + self.z * secondVector.z

    def addVector(self, secondVector):
        return Vector(self.x + secondVector.x, self.y + secondVector.y , self.z + secondVector.z)

    def subVector(self, secondVector):
        return Vector(self.x - secondVector.x, self.y - secondVector.y , self.z - secondVector.z)

    def multiplyVector(self, second):
        if(isinstance(second,int) or isinstance(second,float)):
            return Vector(self.x * second , self.y * second, self.z * second)

    def divideVector(self, second):
        if (isinstance(second, int) or isinstance(second, float)):
            return Vector(self.x / second, self.y / second, self.z / second)




