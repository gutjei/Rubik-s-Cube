import pygame
import numpy as np
import math
import threading

WIN_WIDTH = 800
WIN_HEIGHT = 600
WHITE = (255, 255, 255)
BLACK = (-1, -1, -1)

e1 = threading.Event()
e2 = threading.Event()
e3 = threading.Event()



Vw = 1
Cw = 50
Vh = 1
Ch = 50
O = np.array([0,0,0])

def Mz(az):			   		   
	return np.array([[math.cos(az),-math.sin(az),0],
				  [math.sin(az), math.cos(az),0],
				  [0, 0, 1]])


def My(ay): 
	a = np.array([[math.cos(ay),0,math.sin(ay)],
			   [0,1,0],
			   [-math.sin(ay),0,math.cos(ay)]], float)
	return a
def Mx(ax):
	a =  np.array([[1,0,0],
			   [0,math.cos(ax),-math.sin(ax)],
			   [0,math.sin(ax),math.cos(ax)]], float)
	return a



class light():
	def __init__(self,typee,intensity,coord = (0,0,0),direction = (0,0,0)):
		
		self.intensity = intensity
		self.position = coord
		self.direction = direction
		self.typee = typee
		

def lenght_v(A):
	return math.sqrt(A[0]**2+A[1]**2+A[2]**2)


def sdRoundBox(p, b):
	q = np.abs(p) - b;
	return lenght_v(q) + min(max(q[0],max(q[1],q[2])),0.0) - 0.5
	
def DE(a,b):
	lenght_v(q) + min(max(q[0],max(q[1],q[2])),0.0) - r


Lights = [light("point",0.5,np.array([0,0,0])),
		  light("ambient",0.1),
		  light("directional",0.2, direction = [1,4,4])]
			


def ComputeLighting(P, N):
	i = 0.0
	for light in Lights:
		if light.typee == "ambient":
			i += light.intensity
		elif light.typee == "point":
			L = light.position - P
		else:
			L = light.direction

		n_dot_l = np.dot(N, L)
		if n_dot_l > 0:
			i += light.intensity*n_dot_l/(lenght_v(N)*lenght_v(L))
	return i


class spher():
	def __init__(self,center,radius,color):
		self.center = center
		self.radius = radius
		self.color = color
		self.typee = "sphere"
class cube():
	def __init__(self,center,radius,color):
		self.center = center
		self.radius = radius
		self.color = color
		self.typee = "cube"

scene = [spher(np.array([0, 1, 3]),1,np.array([255, 0, 0])),
		 spher(np.array([-2, 0, 4]),1,np.array([0, 255, 0])),
		 spher(np.array([2, 0, 4]),1,np.array([0, 0, 255])),
		 spher(np.array([0, 5001, 0]),5000,np.array([255, 255, 0]))]
			

def IntersectRaySphere(O, D, sphere):
	C = sphere.center
	r = sphere.radius
	OC = O - C

	k1 = np.dot(D, D)
	k2 = 2*np.dot(OC, D)
	k3 = np.dot(OC, OC) - r*r
	
	discriminant = k2*k2 - 4*k1*k3
	if discriminant < 0:
		return 99999

	t1 = (-k2 + math.sqrt(discriminant)) / (2*k1)
	t2 = (-k2 - math.sqrt(discriminant)) / (2*k1)
	return min(t1, t2)

def ToViewport(x, y):
	return np.array([x*Vw/Cw, y*Vh/Ch, 1])

def TraceRay(O, D, t_min, t_max):
	closest_t = 99999
	closest_sphere = 0
	for i in scene:
		t = IntersectRaySphere(O, D, i)
		if t >= 0 and t<99999 and t < closest_t:
			closest_t = t
			closest_sphere = i
			
			
	if closest_sphere == 0:
		return (0,0,0)
	P = O + closest_t*D
	N = P - closest_sphere.center
	N = N / lenght_v(N)
	#return closest_sphere.color
	#print(closest_sphere.color,ComputeLighting(P, N))
	return closest_sphere.color*ComputeLighting(P, N)

class render():
	def __init__(self, razmer, color):
		self.color = color
		self.razmer = razmer
		self.alpha = -math.pi/5
		

	def render(self):
		global scene
		sf = pygame.Surface (self.razmer)
		ar = pygame.PixelArray(sf)
		
		for x in range(-Cw//2,Ch//2,1):
			for y in range(-Cw//2,Ch//2,1):
				D = np.dot(ToViewport(x, y), My(self.alpha))
				color = TraceRay(O, D, 1, 99999)
				'''
				t1 = threading.Thread(target=TraceRay, args=(O, D, 1, 99999))
				ar[x+400,y+400] = (color[0],color[1],color[2])
				
				D = np.dot(ToViewport(x, y+1), My(self.alpha))
				t2 = threading.Thread(target=TraceRay, args=(O, D, 1, 99999))
				ar[x+400+1,y+400+1] = (color[0],color[1],color[2])
				
				D = np.dot(ToViewport(x, y+2), My(self.alpha))
				t3 = threading.Thread(target=TraceRay, args=(O, D, 1, 99999))
				ar[x+400+1,y+400+1] = (color[0],color[1],color[2])
				'''
				
				#if color != (0,0,0):
					#print(color)
				ar[x+400,y+400] = (color[0],color[1],color[2])
		self.alpha += math.pi/10
		del ar
		return sf
