import pygame as py
import math as m
import numpy as np
from random import randint, choice
import copy

py.init()
screen = py.display.set_mode((1280 * 1.5, 720 * 1.5))
clock = py.time.Clock()
running = True

fov = np.radians(60)
aspect = 16/9
near, far = 0.1, 100
f = 1 / np.tan(fov / 2)

pMatrix = np.array([
    [f/aspect, 0, 0, 0],
    [0, f, 0, 0],
    [0, 0, (far+near)/(near-far), (2*far*near)/(near-far)],
    [0, 0, -1, 0]
])

red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
yellow = (255, 255, 0)
black = (0, 0, 0)
white = (255, 255, 255)
orange  = (255, 102, 0)
purple = (255, 0, 255)

def randomColor():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)

    return (r, g, b)

cameraPos = [0, 0, 0]
cameraRotation = [0, 0, 0]
fov = 30

defaultRenderDistance = 10 # The distance at which an object will be rendered at set size
distanceShrink = 2

class Pixel:
    def __init__(self, x, y, color, layer):
        self.x, self.y, self.color, self.layer = x, y, color, layer

allPixels = []

def renderPixelTest(squares): # this is essentially a lab for me to experiment with pixel rendering
    pixels = py.surfarray.pixels3d(screen)
    squares = sorted(squares, key=lambda s: s[2], reverse=True) #sorts squres by its third value

    for i in squares:
        pixels[i[0] - 100:i[0] + 100, i[1] - 100:i[1] + 100] = i[3]

        i[0] += randint(-5, 5)
        i[1] += randint(-5, 5)

        i[0] = min(i[0], screen.get_width() - 100)
        i[1] = min(i[1], screen.get_height() - 100)
        i[0] = max(i[0], 100)
        i[1] = max(i[1], 100)

    del pixels

class Vertex:
    def __init__(self, x, y, z):
        self.x, self.y, self.z = x, y, z

    def to_array(self):
        return np.array([self.x, self.y, self.z, 1.0])

    def project(self, projection_matrix, width, height):
        clip = projection_matrix @ self.to_array()

        ndc = clip[:3] / clip[3]

        x_screen = (ndc[0] + 1) * 0.5 * width
        y_screen = (1 - ndc[1]) * 0.5 * height
        z_screen = ndc[2]

        return np.array([x_screen, y_screen])
    


class Face:
    def __init__(self, vertOne, vertTwo, vertThree, color):
        self.vertOne = vertOne
        self.vertTwo = vertTwo
        self.vertThree = vertThree
        self.color = color

    def draw(self, projectMatrix, screen, playerpos):
        averageZ = (self.vertOne.z + self.vertTwo.z + self.vertThree.z) / 3

        if averageZ < playerpos.z:
            global allPixels

            pointOne = self.vertOne.project(projectMatrix, screen.get_width(), screen.get_height())
            pointTwo = self.vertTwo.project(projectMatrix, screen.get_width(), screen.get_height())
            pointThree = self.vertThree.project(projectMatrix, screen.get_width(), screen.get_height())
            a = (pointOne[0], pointOne[1])
            b = (pointTwo[0], pointTwo[1])
            c = (pointThree[0], pointThree[1])

            pixels = py.surfarray.pixels3d(screen)

            min_x = int(max(min(a[0], b[0], c[0]), 0))
            max_x = int(min(max(a[0], b[0], c[0]), screen.get_width()))
            min_y = int(max(min(a[1], b[1], c[1]), 0))
            max_y = int(min(max(a[1], b[1], c[1]), screen.get_height()))

            x, y = np.meshgrid(np.arange(min_x, max_x), np.arange(min_y, max_y))

            x1, y1 = a
            x2, y2 = b
            x3, y3 = c

            den = ( (y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3) )
            α = ((y2 - y3)*(x - x3) + (x3 - x2)*(y - y3)) / den
            β = ((y3 - y1)*(x - x3) + (x1 - x3)*(y - y3)) / den
            γ = 1 - α - β

            mask = (α >= 0) & (β >= 0) & (γ >= 0)

            pixels[min_x:max_x, min_y:max_y][mask.T] = self.color

    def drawSimple(self, projectMatrix, screen, playerpos):
        averageZ = (self.vertOne.z + self.vertTwo.z + self.vertThree.z) / 3
        
        if averageZ < playerpos.z:
            pointOne = self.vertOne.project(projectMatrix, screen.get_width(), screen.get_height())
            pointTwo = self.vertTwo.project(projectMatrix, screen.get_width(), screen.get_height())
            pointThree = self.vertThree.project(projectMatrix, screen.get_width(), screen.get_height())
            a = (pointOne[0], pointOne[1])
            b = (pointTwo[0], pointTwo[1])
            c = (pointThree[0], pointThree[1])

            py.draw.polygon(screen, self.color, [a, b, c])


    def retrunZaverage(self):
        vertZ = 0

        vertZ += self.vertOne.z
        vertZ += self.vertTwo.z
        vertZ += self.vertThree.z

        return vertZ / 3

class Shape:
    def __init__(self, faces):
        self.faces = faces

    def move(self, moveVertex):
        for i in self.faces:
            moveFace(i, moveVertex)

    def rotate(self, rotationType, centerVertex, angle):
        for i in self.faces:
            rotateFace(i, rotationType, centerVertex, angle)
    
    def draw(self, screen, projectMatrix):
        zPositions = []
        zConnections = {}

        for i in self.faces:
            zPositions.append(i.retrunZaverage())
            zConnections[i.retrunZaverage()] = i

        zPositions.sort()

        for i in zPositions:
            zConnections[i].drawSimple(projectMatrix, screen, )

    def returnZAverage(self):
        vertZ = 0
        count = 0

        for i in self.faces:
            vertZ += i.vertOne.z
            vertZ += i.vertTwo.z
            vertZ += i.vertThree.z

            count += 3

        return vertZ / count

class AllShapes:
    def __init__(self, shapes):
        self.shapes = shapes

    def draw(self, screen, projMatrix):
        averages = []
        aConnects = {}
        for i in self.shapes: 
            averages.append(i.returnZAverage())
            aConnects[i.returnZAverage()] = i

        averages.sort()

        for i in averages:
            aConnects[i].draw(screen, projMatrix)
            

def drawNoProjection(vertex):
    x = vertex.x
    y = vertex.y

    return [x,y]

def mapZ(vertOne, vertTwo, VertThree, x, y):
    return 50

def drawFace(face, screen, projectMatrix):
    vert1 = face.vertOne.project(projectMatrix, screen.get_width(), screen.get_height())
    vert2 = face.vertTwo.project(projectMatrix, screen.get_width(), screen.get_height())
    vert3 = face.vertThree.project(projectMatrix, screen.get_width(), screen.get_height())

    py.draw.polygon(screen, face.color, [vert1, vert2, vert3])

def barycentric_weights(px, py, A, B, C):
    (x1, y1), (x2, y2), (x3, y3) = A, B, C

    denom = (y2 - y3)*(x1 - x3) + (x3 - x2)*(y1 - y3)

    w1 = ((y2 - y3)*(px - x3) + (x3 - x2)*(py - y3)) / denom
    w2 = ((y3 - y1)*(px - x3) + (x1 - x3)*(py - y3)) / denom
    w3 = 1 - w1 - w2

    return w1, w2, w3


def interpolate_xyz(px, py, A, B, C, XYZ1, XYZ2, XYZ3):
    w1, w2, w3 = barycentric_weights(px, py, A, B, C)

    X = w1*XYZ1[0] + w2*XYZ2[0] + w3*XYZ3[0]
    Y = w1*XYZ1[1] + w2*XYZ2[1] + w3*XYZ3[1]
    Z = w1*XYZ1[2] + w2*XYZ2[2] + w3*XYZ3[2]

    return (X, Y, Z)

def moveVertex(vertex, movementVertex):
    vertex.x += movementVertex.x
    vertex.y += movementVertex.y
    vertex.z += movementVertex.z

    return(Vertex(vertex.x, vertex.y, vertex.z))

def moveFace(face, movementVertex):
    face.vertOne = moveVertex(face.vertOne, movementVertex)
    face.vertTwo = moveVertex(face.vertTwo, movementVertex)
    face.vertThree = moveVertex(face.vertThree, movementVertex)

def rotateVertex(vertex, centerPoint, rotationType, angle):
    angle = m.radians(angle)
    relativeVertex = [vertex.x - centerPoint.x, vertex.y - centerPoint.y, vertex.z - centerPoint.z]
    newVertexLocal = [0, 0, 0]

    if rotationType == "x":
        newVertexLocal[0] = relativeVertex[0]
        newVertexLocal[1] = (relativeVertex[1] * m.cos(angle)) - (relativeVertex[2] * m.sin(angle))
        newVertexLocal[2] = (relativeVertex[1] * m.sin(angle)) + (relativeVertex[2] * m.cos(angle))
    elif rotationType == "y":
        newVertexLocal[1] = relativeVertex[1]
        newVertexLocal[0] = (relativeVertex[0] * m.cos(angle)) + (relativeVertex[2] * m.sin(angle))
        newVertexLocal[2] = (-relativeVertex[0] * m.sin(angle)) + (relativeVertex[2] * m.cos(angle))
    elif rotationType == "z":
        newVertexLocal[0]  =  (newVertexLocal[0] * (m.cos(angle)) - newVertexLocal[1] * m.sin(angle))
        newVertexLocal[1] =  (newVertexLocal[0] * m.sin(angle)) + (newVertexLocal[1] * m.cos(angle))
        newVertexLocal[2] = newVertexLocal[2]
    else:
        raise Exception(f"{rotationType} is not a valid rotation")
    
    newVertexLocal[0] += centerPoint.x
    newVertexLocal[1] += centerPoint.y
    newVertexLocal[2] += centerPoint.z

    return Vertex(newVertexLocal[0], newVertexLocal[1], newVertexLocal[2])

def rotateFace(face, rotationType, centerPoint, angle):
    face.vertOne = rotateVertex(face.vertOne, centerPoint, rotationType, angle)
    face.vertTwo = rotateVertex(face.vertTwo, centerPoint, rotationType, angle)
    face.vertThree = rotateVertex(face.vertThree, centerPoint, rotationType, angle)

    return face

def drawSquare(vertOne, vertTwo, vertThree, vertFour, color, projectMatrix, screen):
    faceOne = Face(vertOne, vertTwo, vertThree, color)
    faceTwo = Face(vertFour, vertTwo, vertThree, color)

    faceOne.draw(projectMatrix, screen)
    faceTwo.draw(projectMatrix, screen)

    return [faceOne, faceTwo]

def drawRect(projMatrix, screen, centerPoint, width, hight, volume, topColor = white, bottomColor = white, frontColor = white, backColor = white, leftColor = white, rightColor = white):
    moveWidth = width / 2
    moveHight = hight / 2
    moveVolume = volume / 2

    # Create independent vertices
    v = [Vertex(centerPoint.x - moveWidth, centerPoint.y + moveHight, centerPoint.z + moveVolume), # top left front
         Vertex(centerPoint.x + moveWidth, centerPoint.y + moveHight, centerPoint.z + moveVolume), # top right front
         Vertex(centerPoint.x - moveWidth, centerPoint.y - moveHight, centerPoint.z + moveVolume), # bottom left front
         Vertex(centerPoint.x + moveWidth, centerPoint.y - moveHight, centerPoint.z + moveVolume), # bottom right front
         Vertex(centerPoint.x - moveWidth, centerPoint.y + moveHight, centerPoint.z - moveVolume), # top left back
         Vertex(centerPoint.x + moveWidth, centerPoint.y + moveHight, centerPoint.z - moveVolume), # top right back
         Vertex(centerPoint.x - moveWidth, centerPoint.y - moveHight, centerPoint.z - moveVolume), # bottom left back
         Vertex(centerPoint.x + moveWidth, centerPoint.y - moveHight, centerPoint.z - moveVolume)] # bottom right back

    front  = drawSquare(v[0], v[1], v[2], v[3], frontColor, projMatrix, screen)
    back   = drawSquare(v[4], v[5], v[6], v[7], backColor, projMatrix, screen)
    top    = drawSquare(v[2], v[3], v[6], v[7], topColor, projMatrix, screen)
    bottom = drawSquare(v[0], v[1], v[4], v[5], bottomColor, projMatrix, screen)
    left   = drawSquare(v[0], v[2], v[4], v[6], leftColor, projMatrix, screen)
    right  = drawSquare(v[1], v[3], v[5], v[7], rightColor, projMatrix, screen)

    faces = front + back + top + bottom + left + right

    faces = copy.deepcopy(faces)

    return Shape(faces)