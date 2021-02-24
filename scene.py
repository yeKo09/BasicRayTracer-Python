from image import Image
from point import Point
from ray import Ray
from color import Color

import shutil
import tempfile
from multiprocessing import Process, Value
from pathlib import Path


class Scene:
    """
    	The scene that gets rendered. Contains information like the camera
    	position, the different objects present, etc.
    """
    def __init__(self, camera, objects, lights, width, height):
        self.camera = camera
        self.objects = objects
        self.lights = lights
        self.width = width
        self.height = height

    def renderMultipleProcess(self, processCount, imgFile):
        def splitRange(count, parts):
            d, r = divmod(count, parts)
            return [
                (i * d + min(i, r), (i + 1) * d + min(i + 1, r)) for i in range(parts)
            ]

        ranges = splitRange(self.height, processCount)
        tempDir = Path(tempfile.mkdtemp())
        tempFileTmpl = "yeko-part-{}.temp"
        processes = []
        try:
            for hmin, hmax in ranges:
                partFile = tempDir / tempFileTmpl.format(hmin)
                processes.append(
                    Process(
                        target=self.render,
                        args=(hmin, hmax, partFile),
                    )
                )
            # Start all the processes
            for process in processes:
                process.start()
            # Wait for all the processes to finish
            for process in processes:
                process.join()
            # Construct the image by joining all the parts
            Image.pixelsToPpmHeader(imgFile, width=self.width, height=self.height)
            for hmin, _ in ranges:
                partFile = tempDir / tempFileTmpl.format(hmin)
                imgFile.write(open(partFile, "r").read())
        finally:
            shutil.rmtree(tempDir)


    def render(self, hmin, hmax, partFile):
        aspectRatio = self.width / float(self.height)
        screen = (-1, -1 / aspectRatio, 1, 1 / aspectRatio)  # left, bottom, right, top
        xStep = (screen[2] - screen[0]) / (self.width - 1) # -1 is because for example we have 320 width pixels.But there will be 319 steps logically.4
        yStep = (screen[3] - screen[1]) / (self.height - 1)
        pixels = Image(self.width, hmax - hmin)

        for j in range(hmin,hmax):
            y = screen[1] + j * yStep
            for i in range(self.width):
                x = screen[0] + i * xStep
                ray = Ray(self.camera, Point(x,y).subVector(self.camera))
                pixels.setPixel(i, j - hmin, self.traceRay(ray))

        with open(partFile, "w") as partFileObj:
            pixels.pixelsToPpmActual(partFileObj)

    def traceRay(self, ray, depth=0, maxDepth= 5):
        color = Color()
        # Find the nearest object hit by the ray in the scene
        distHit, objHit = self.findNearest(ray)
        if objHit is None:
            return color
        hitPos = ray.direction.multiplyVector(distHit).addVector(ray.origin)
        hitNormal = objHit.surfaceNormal(hitPos)
        color = color.addVector(self.colorAt(objHit, hitPos, hitNormal))
        if depth < maxDepth:
            #The value of 0.0001 is the minimum displace
            newRayPos = hitNormal.multiplyVector(0.0001).addVector(hitPos)
            """Then we implement the reflection formula
                R = V - 2(V . N) * N
                where,
                R is the normalized reflected ray,
                L is a direction unit vector of the ray to be reflected,
                N is the direction unit vector normal to the surface the ray stroke
            """
            newRayDirection = ray.direction.subVector(hitNormal.multiplyVector(ray.direction.dotProduct(hitNormal) * 2))
            newRay = Ray(newRayPos, newRayDirection)
            #Attenuation phase
            color = color.addVector((self.traceRay(newRay, depth+1).multiplyVector(objHit.material.reflection)))
        return color

    def findNearest(self, ray):
        minimumDistance = None
        objHit = None
        for obj in self.objects:
            dist = obj.checkIfIntersects(ray)
            if dist is not None and (objHit is None or dist < minimumDistance):
                minimumDistance = dist
                objHit = obj
        return (minimumDistance, objHit)

    def colorAt(self, objHit, hitPos, hitNormal):
        material = objHit.material
        objColor = material.colorAt(hitPos)
        toCamera = self.camera.subVector(hitPos)
        specularCoef = 80
        color = Color(0,0,0).multiplyVector(material.ambient)
        for light in self.lights:
            toTheLight = Ray(hitPos, light.pos.subVector(hitPos))
            # Diffuse shading (Lambert)
            mtrl1 = objColor.multiplyVector(material.diffuse)
            mtrl2 = mtrl1.multiplyVector(max(hitNormal.dotProduct(toTheLight.direction), 0))
            color = color.addVector(mtrl2)
            # Specular shading (Blinn-Phong)
            halfVector = (toTheLight.direction.addVector(toCamera)).normalizeVector()
            mtrl3 = light.color.multiplyVector(material.specular)
            mtrl4 = mtrl3.multiplyVector(max(hitNormal.dotProduct(halfVector), 0) ** specularCoef)
            color = color.addVector(mtrl4)
        return color

