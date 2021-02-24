import unittest
from vector import Vector

class RayTracingTesting(unittest.TestCase):

    def setUp(self):
       self.v1 = Vector(2.0,2.0,1.0)
       self.inputs = {
           "dotProduct": Vector(3.0,1.0,2.0),
           "addOrSub": Vector(1.0, 2.0, 3.0),
           "multiply": 3
       }
       self.expectedResults = {
           "magnitudeVector": 3.0,
           "dotProduct": 10.0,
           "vecAddition": [3.0,4.0,4.0],
           "vecSubstraction": [1.0,0.0,-2.0],
           "vecMultiply": [6.0,6.0,3.0],
           "vecNormalize": [0.6666666666666666,0.6666666666666666,0.3333333333333333]
       }

    def testVectorMagnitude(self):
        self.assertEqual(self.v1.magnitudeOfVector(),self.expectedResults["magnitudeVector"])

    def testVectorDotProduct(self):
        self.assertEqual(self.v1.dotProduct(self.inputs["dotProduct"]),self.expectedResults["dotProduct"])

    def testVectorAddition(self):
        newVector = self.v1.addVector(self.inputs["addOrSub"])
        self.assertEqual([getattr(newVector,"x"),getattr(newVector,"y"),getattr(newVector,"z")],self.expectedResults["vecAddition"])

    def testVectorSubstraction(self):
        newVector = self.v1.subVector(self.inputs["addOrSub"])
        self.assertEqual([getattr(newVector,"x"),getattr(newVector,"y"),getattr(newVector,"z")],self.expectedResults["vecSubstraction"])

    def testVectorMultiply(self):
        newVector = self.v1.multiplyVector(self.inputs["multiply"])
        self.assertEqual([getattr(newVector,"x"),getattr(newVector,"y"),getattr(newVector,"z")],self.expectedResults["vecMultiply"])

    #By testing testVectorNormalize function,we already test a vector divided by a float so we don't need to test that in the coming lines.
    def testVectorNormalize(self):
        normalizedVector = self.v1.normalizeVector()
        self.assertEqual([getattr(normalizedVector,"x"),getattr(normalizedVector,"y"),getattr(normalizedVector,"z")],self.expectedResults["vecNormalize"])


if __name__ == "__main__":
    unittest.main()
