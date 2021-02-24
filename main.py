from image import Image
from color import Color
from vector import Vector
from point import Point
from sphere import Sphere
from scene import Scene
from light import Light
from material import Material
from time import time
import imageio
from pathlib import Path
from Test import RayTracingTesting
import os
from multiprocessing import cpu_count



if __name__ == "__main__":
    WIDTH = 400
    HEIGHT = 300
    camera = Vector(0,-0.35,-1)
    #0xFF is a hexadecimal constant which is 11111111 in binary.
    objects = [
        Sphere(Point(0.2, -0.1, 1), 0.7, Material(Color.fromHex("#0000FF"))),
        #Sphere(Point(0.1, -0.3, 0), 0.1, Material(Color.fromHex("#0000FF"))),
        Sphere(Point(-1, -0.2, 1), 0.2, Material(Color.fromHex("#00FF00"))),
        #Ground plane next
        Sphere(Point(0, 1000.5, 1), 1000.0, Material(Color.fromHex("#FFFFFF"),diffuse=6.0)),
    ]
    #objects = [Sphere(Point(0,0,0),0.5, Material(Color.fromHex("#FF0000")))]
    lights = [Light(Point(1.5,-0.5,-10.0), Color.fromHex("#FFFFFF"))]
    processCount = cpu_count()
    start = time()
    for i in range(0,4):
        objects[1].center = Point(-1+(i/2),-0.2,-(0+(i/20)))
        scene = Scene(camera, objects, lights, WIDTH, HEIGHT)
        ppmFile = "sourceImages/test" + str(i) + ".ppm"
        with open(ppmFile, "w") as imgFile:
            scene.renderMultipleProcess(processCount,imgFile)

    imagePath = Path('sourceImages')
    images = list(imagePath.glob('*.ppm'))
    imageList = []
    for fileName in images:
        imageList.append(imageio.imread(fileName))
    imageio.mimwrite('sourceImages/rayTracing.gif', imageList)
    #You have to show an absolute path below.
    os.startfile('C:\\Users\\yekta\\PycharmProjects\\RayTracing\\sourceImages\\rayTracing.gif')
    end = time()
    print("Runtime of the program is:  {:.2f} seconds".format(end-start))