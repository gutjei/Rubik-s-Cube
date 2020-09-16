import pygame
import random
import math as math
import numpy as np

MAX_DIST = 500000;
ITERATIONS = 50;
Cw = 400
Ch = 400

_Object1 = np.array([50.,50.,50.,49.])
_Object2 = np.array([0.,0.,50.,49.])
_Object3 = np.array([0.,0.,50.,49.])

def normalize(A):
	B = np.array([0,0,0])
	c = 0.0000001
	B[0] = A[0]/math.sqrt((A[0]+c)**2+(A[1]+c)**2+(A[2]+c)**2)
	B[1] = A[1]/math.sqrt((A[0]+c)**2+(A[1]+c)**2+(A[2]+c)**2)
	B[2] = A[2]/math.sqrt((A[0]+c)**2+(A[1]+c)**2+(A[2]+c)**2)
	
	return B

def length_v(A):
	return math.sqrt(A[0]**2+A[1]**2+A[2]**2)

def clamp(num, min_value, max_value):
   return max(min(num, max_value), min_value)

def lerp(start, end, t):
    return start * (1 - t) + end * t


def smin(a, b, k):

	h = clamp(0.5 + 0.5 * (b - a) / k, 0.0, 1.0);
	return lerp(b, a, h) - k * h * (1.0 - h);


def plane(p):
            
	return p[1];
            

def sphere(s,  p):
	return length_v(p - np.array([s[0],s[1],s[2]])) - s[3];


def cube(s, p):
	q = np.abs(p - np.array([s[0],s[1],s[2]],float)) - s[2];
	
	#length(max(abs(pos)-b, 0.0))-r;
	if q[0]>0 and q[1] > 0 and q[2] > 0:
		return length_v(q)
	return 99999

def getDist(p):

	dist1 = sphere(_Object1, p);
	dist2 = sphere(_Object3, p);
	#dist2 = cube(_Object2, p);
	#dist3 = plane(p);
	#dist3 = 9999;
	#return smin(smin(dist1, dist2, 0.5), dist3, 0.5);
	return min(dist1, dist2)
	#return dist2

def getNormal(p):
            
	d = getDist(p);
	e = np.array([0.001, 0],float);
	n = d - np.array([getDist(p - np.array([e[0],e[1],e[1]])), getDist(p - np.array([e[1],e[0],e[1]])), getDist(p - np.array([e[1],e[1],e[0]]))]);
	return normalize(n);
            

def raymarchLight(ro, rd):
            
	dO = 0;
	md = 1;
	for i in range(20):
		p = ro + rd * dO;
		dS = getDist(p);
		md = min(md, dS);
		dO += dS;
		if(dO > 50 or dS < 0.1):
			break;
	return md;

def getLight(p, ro, i, lightPos):
	
	l = normalize(lightPos - p);
	n = getNormal(p);
	dif = clamp(np.dot(n, l) * 0.5 + 0.5, 0, 1);
	d = raymarchLight(p + n, l);
	d += 1;
	d = clamp(d, 0, 1);
	dif *= d;
	col = np.array([dif, dif, dif, 1]);
	occ = (float(i) / ITERATIONS * 2);
	occ = (1 - occ)**2;
	col = col*occ
	#print(col)
	#col[0] *=  (1 - fog) + 0.28 * fog;
	#col[1] *=  (1 - fog) + 0.28 * fog;
	#col[2] *=  (1 - fog) + 0.28 * fog;
	return col;


def raymarch(ro, rd):

	p = rd;
	for i in range(ITERATIONS):
		d = getDist(p);
		#print(d,p,i)
		if(d > MAX_DIST):
			return (0,255,0);
		p[2] +=d;
	#print(d)
	if(abs(d) < 0.1):
		return (255,0,0)
		#return [255,255,255,2]*getLight(p, ro, i, [0, 100, 0]);
	return (0,255,0)

class render():
	def __init__(self, razmer, color):
		self.color = color
		self.razmer = razmer

	def render(self):
		global scene
		sf = pygame.Surface (self.razmer)
		ar = pygame.PixelArray(sf)
		
		for x in range(-Cw//2,Ch//2,1):
		#for x in range(Cw):
			print(x)
			for y in range(-Cw//2,Ch//2,1):
			#for y in range(Ch):
				D = np.array([x,y,1],float)
				color = raymarch([0.,0.,0.], D)
				#print(color)
				ar[x+400,y+400] = (color[0],color[1],color[2])
		#print(ar)
		del ar
		return sf
	

