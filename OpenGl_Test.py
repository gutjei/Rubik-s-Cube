from OpenGL.GL import * 
from OpenGL.GLU import * 
from pygame.locals import *
import pygame

cubeVertices = ((1,1,1),(1,1,-1),(1,-1,-1),(1,-1,1),(-1,1,1),(-1,-1,-1),(-1,-1,1),(-1,1,-1))
cubeEdges = ((0,1),(0,3),(0,4),(1,2),(1,7),(2,5),(2,3),(3,6),(4,6),(4,7),(5,6),(5,7))
cubeQuads = ((0,3,6,4),(2,5,6,3),(1,2,5,7),(1,0,4,7),(7,4,6,5),(2,3,0,1))

def wireCube():
    glBegin(GL_LINES)
    for cubeEdge in cubeEdges:
        for cubeVertex in cubeEdge:
            glVertex3fv(cubeVertices[cubeVertex])
    glEnd()

pygame.init()
display = (800,800)
screen = pygame.display.set_mode(display,DOUBLEBUF|OPENGL)
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()


pygame.display.set_mode(display, DOUBLEBUF|OPENGL)

gluPerspective(45, (display[0]/display[1]), 0.001, 50.0)
glTranslatef(0.0, 0.0, -10)

running = True
while running:
	for event in pygame.event.get():
        # check for closing window
		if event.type == pygame.QUIT:
			running = False
	
	
	glClear(GL_COLOR_BUFFER_BIT|GL_DEPTH_BUFFER_BIT)
	wireCube()
	pygame.display.flip()
