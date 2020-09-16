import pygame
import random
import math as math
import numpy as np
import cube
import pixelarrey_test
import RayMarching
#from numba import jit, cuda



WIDTH = 800
HEIGHT = 800
FPS = 60
# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
ORANGE = (255, 165, 0)
YELLOW = (255, 225, 53)
ShowZ =  0
ShowX = 0
ShowY = 0
def rangl():
	global ShowZ,ShowX,ShowY
	if moutionAZ_:
			ShowZ += az
	elif moutionAZ:
			ShowZ += az
	if moutionAx_:
			ShowX += ax
	elif moutionAx:
			ShowX += ax
	if moutionAy_:
			ShowY += ay
	elif moutionAy:
			ShowY += ay
 
def toFixed(numObj, digits=3):
    return f"{numObj:.{digits}f}"
def show_fps(window, clock,d1,d2,Mx,My):
    fps_overlay = FPS_FONT.render(str(clock.get_fps()), True, GOLDENROD)
    lines = FPS_FONT.render(str(toFixed(d1)+' '+str(toFixed(d2))), True, GOLDENROD)
    rr = FPS_FONT.render("x="+str(Mx)+"y="+str(My)+"z="+str(toFixed(math.asin(math.sin(ShowZ)))), True, GOLDENROD)
    window.blit(fps_overlay, (0, 0))
    window.blit(rr, (300, 0))
    #window.blit(lines, (Mx+50, My-50))

a = 0
ay = math.pi/300
ax = math.pi/300
az = math.pi/300
R = np.array([[math.cos(a),-math.sin(a)],
			[math.sin(a),math.cos(a)]], float)
  			
def My(ay): 
	a = np.array([[math.cos(ay),0,math.sin(ay),0],
			   [0,1,0,0],
			   [-math.sin(ay),0,math.cos(ay),0],
			   [0,0,0,1]], float)

	return a
def Mx(ax):
	a =  np.array([[1,0,0,0],
			   [0,math.cos(ax),-math.sin(ax),0],
			   [0,math.sin(ax),math.cos(ax),0],
			   [0,0,0,1]], float)
	return a
def Mz(az):			   		   
	a = np.array([[math.cos(az),-math.sin(az),0,0],
			   [math.sin(az),math.cos(az),0,0],
			   [0,0,1,0],
			   [0,0,0,1]], float)
			 
	return a

cord = np.array([[100,-100,100,-100,100,-100,100,-100],
				 [100,100,-100,-100,100,100,-100,-100],
				 [100,100,100,100,-100,-100,-100,-100]], float)

MatrixProection_ = np.array([[math.sqrt(3)/2,math.sqrt(2)/4,0,0],
							[0,math.sqrt(2)/2,0,0],
							[1/2,-math.sqrt(6)/4,0,0],
							[0,0,0,1]])


MatrixProection = np.array([[1,0,0,0],
							[0,1,0,0],
							[0,0,1,0],
							[0,0,0,1]])
							



class segment():
	def __init__(self,x,y,z):
		self.C = y
		Cx,Cy,Cz = x*2-100,y*2-100,z*2-100
		self.vec = np.array([.0,.0,.0])
		self.depth = 0
		size = 49
		self.coord = np.array([[size+Cx,-size+Cx,size+Cx,-size+Cx,size+Cx,-size+Cx,size+Cx,-size+Cx],
							   [size+Cy,size+Cy,-size+Cy,-size+Cy,size+Cy,size+Cy,-size+Cy,-size+Cy],
							   [size+Cz,size+Cz,size+Cz,size+Cz,-size+Cz,-size+Cz,-size+Cz,-size+Cz],
							   [1,1,1,1,1,1,1,1]], float)
		self.coordP = np.array([[size+Cx,-size+Cx,size+Cx,-size+Cx,size+Cx,-size+Cx,size+Cx,-size+Cx],
							   [size+Cy,size+Cy,-size+Cy,-size+Cy,size+Cy,size+Cy,-size+Cy,-size+Cy],
							   [size+Cz,size+Cz,size+Cz,size+Cz,-size+Cz,-size+Cz,-size+Cz,-size+Cz],
					 		   [1,1,1,1,1,1,1,1]], float)
					 		   
	
	def getCoordP(self,coord):
		self.coordP = coord
	
	def centerCube(self):
		CenterX = (self.coord[0][0] + self.coord[0][7])/2
		CenterY = (self.coord[1][0] + self.coord[1][7])/2
		CenterZ = (self.coord[2][0] + self.coord[2][7])/2
		a = (CenterX,CenterY,CenterZ)
		return a
	def depthF(self):
		self.depth = 1000-(self.coord[2][0] + self.coord[2][7])/2
		'''
		depth =  [0,0,0,0,0,0,0,0]
		depth[0] = 1000-self.coord[2][0]
		depth[1] = 1000-self.coord[2][1]
		depth[2] = 1000-self.coord[2][2]
		depth[3] = 1000-self.coord[2][3]
		depth[4] = 1000-self.coord[2][4]
		depth[5] = 1000-self.coord[2][5]
		depth[6] = 1000-self.coord[2][6]
		depth[7] = 1000-self.coord[2][7]
		depth = np.sort(depth)
		self.depth = depth[0]
		'''
	def proection(self):
		self.coord = np.dot(np.transpose(self.coordP),MatrixProection)
		self.coord = np.transpose(self.coord)
		self.coord = self.coord / abs(self.coord[3])
		#print(self.coord)
	def normal_vectore(self,V1,V2):
		sol = np.cross(V1,V2)
		drawplace = False
		if sol[0]<=0 and sol[1]<=0 and sol[2]>=0 or \
		sol[0]>=0 and sol[1]<=0 and sol[2]>=0 or \
		sol[0]>=0 and sol[1]>=0 and sol[2]>=0 or \
		sol[0]<=0 and sol[1]<=0 and sol[2]>=0 or \
		sol[0]<=0 and sol[1]>=0 and sol[2]>=0:
			drawplace = True
		#print(sol)
		return drawplace  
	def normal(self,cord):
		  
		V1 = [cord[0][1]-cord[0][0],cord[1][1]-cord[1][0],cord[2][1]-cord[2][0]]
		V2 = [cord[0][2]-cord[0][0],cord[1][2]-cord[1][0],cord[2][2]-cord[2][0]]
	
		V3 = [cord[0][1]-cord[0][0],cord[1][1]-cord[1][0],cord[2][1]-cord[2][0]]
		V4 = [cord[0][4]-cord[0][0],cord[1][4]-cord[1][0],cord[2][4]-cord[2][0]]
	
		V5 = [cord[0][2]-cord[0][6],cord[1][2]-cord[1][6],cord[2][2]-cord[2][6]]
		V6 = [cord[0][7]-cord[0][6],cord[1][7]-cord[1][6],cord[2][7]-cord[2][6]]
	
		V7 = [cord[0][4]-cord[0][6],cord[1][4]-cord[1][6],cord[2][4]-cord[2][6]]
		V8 = [cord[0][2]-cord[0][6],cord[1][2]-cord[1][6],cord[2][2]-cord[2][6]]
	
		V9 = [cord[0][1]-cord[0][0],cord[1][1]-cord[1][0],cord[2][1]-cord[2][0]]
		V10 = [cord[0][2]-cord[0][0],cord[1][2]-cord[1][0],cord[2][2]-cord[2][0]]
	
		V11 = [cord[0][1]-cord[0][0],cord[1][1]-cord[1][0],cord[2][1]-cord[2][0]]
		V12 = [cord[0][2]-cord[0][0],cord[1][2]-cord[1][0],cord[2][2]-cord[2][0]]

		#sol = np.cross(V3,V4)
		#sol1 = np.cross(V4,V3)
		drawplace = [False,False,False,False,False]
		drawplace[0] = self.normal_vectore(V1,V2)
		drawplace[1] = self.normal_vectore(V3,V4)
		drawplace[2] = self.normal_vectore(V5,V6)
		drawplace[3] = self.normal_vectore(V7,V8)
		#normal_vectore(V7,V8)
		#print(sol)
	
		#pygame.draw.aalines(screen, RED, True, [[400, 400], [sol[0]+400, sol[1]+400]])
		#pygame.draw.aalines(screen, BLUE, True, [[sol1[ 0]+400, sol1[1]+400], [400, 400]])
		return drawplace
	
	def Rotate_Z(self,az,temp):
		self.coordP = np.dot(Mz(az),self.coordP)
		self.depthF()
	def Rotate_Y(self,ay,temp):
		self.coordP = np.dot(My(ay),self.coordP)
		self.depthF()
	def Rotate_X(self,ax,temp):
		self.coordP = np.dot(Mx(ax),self.coordP)
		self.depthF()
	
	
	def update1(self,Mx,My):
		#Mx = 350
		#My = 350
		drawPlace = self.normal(self.coord)
		#print(drawPlace)
		if drawPlace[0]:
			pygame.draw.polygon(screen, GREEN, [[self.coord[0][0]+Mx, self.coord[1][0]+My], 
											 [self.coord[0][2]+Mx, self.coord[1][2]+My], 
											 [self.coord[0][3]+Mx, self.coord[1][3]+My], 
											 [self.coord[0][1]+Mx, self.coord[1][1]+My]])
	
		if not(drawPlace[0]):								 
			pygame.draw.polygon(screen, BLUE, [[self.coord[0][4]+Mx, self.coord[1][4]+My], 
											 [self.coord[0][5]+Mx, self.coord[1][5]+My], 
											 [self.coord[0][7]+Mx, self.coord[1][7]+My], 
											 [self.coord[0][6]+Mx, self.coord[1][6]+My]])
	
		if not(drawPlace[1]):
			pygame.draw.polygon(screen, YELLOW, [[self.coord[0][5]+Mx, self.coord[1][5]+My], 
												[self.coord[0][4]+Mx, self.coord[1][4]+My], 
											 [self.coord[0][0]+Mx, self.coord[1][0]+My], 
										     [self.coord[0][1]+Mx, self.coord[1][1]+My]])
		if drawPlace[1]:
			pygame.draw.polygon(screen, WHITE, [[self.coord[0][2]+Mx, self.coord[1][2]+My], 
							 				[self.coord[0][6]+Mx, self.coord[1][6]+My], 
											 [self.coord[0][7]+Mx, self.coord[1][7]+My], 
											 [self.coord[0][3]+Mx, self.coord[1][3]+My]])
											 
		if drawPlace[3]:
			pygame.draw.polygon(screen, RED, [[self.coord[0][0]+Mx, self.coord[1][0]+My], 
											 [self.coord[0][2]+Mx, self.coord[1][2]+My], 
											 [self.coord[0][6]+Mx, self.coord[1][6]+My], 
											 [self.coord[0][4]+Mx, self.coord[1][4]+My]])
		if not(drawPlace[3]):									 
			pygame.draw.polygon(screen, ORANGE, [[self.coord[0][3]+Mx, self.coord[1][3]+My], 
											 [self.coord[0][1]+Mx, self.coord[1][1]+My], 
											 [self.coord[0][5]+Mx, self.coord[1][5]+My], 
											 [self.coord[0][7]+Mx, self.coord[1][7]+My]])
	def update(self):
		#cube
		
		pygame.draw.aalines(screen, RED, True, [[self.coord[0][0]+400, self.coord[1][0]+400], [self.coord[0][1]+400, self.coord[1][1]+400]])
		pygame.draw.aalines(screen, RED, True, [[self.coord[0][0]+400, self.coord[1][0]+400], [self.coord[0][2]+400, self.coord[1][2]+400]])
		pygame.draw.aalines(screen, RED, True, [[self.coord[0][2]+400, self.coord[1][2]+400], [self.coord[0][3]+400, self.coord[1][3]+400]])
		pygame.draw.aalines(screen, RED, True, [[self.coord[0][3]+400, self.coord[1][3]+400], [self.coord[0][1]+400, self.coord[1][1]+400]])
    
		pygame.draw.aalines(screen, GREEN, True, [[self.coord[0][5]+400, self.coord[1][5]+400], [self.coord[0][4]+400, self.coord[1][4]+400]])
		pygame.draw.aalines(screen, GREEN, True, [[self.coord[0][6]+400, self.coord[1][6]+400], [self.coord[0][4]+400, self.coord[1][4]+400]])
		pygame.draw.aalines(screen, GREEN, True, [[self.coord[0][7]+400, self.coord[1][7]+400], [self.coord[0][5]+400, self.coord[1][5]+400]])
		pygame.draw.aalines(screen, GREEN, True, [[self.coord[0][7]+400, self.coord[1][7]+400], [self.coord[0][6]+400, self.coord[1][6]+400]])
    
		pygame.draw.aalines(screen, BLUE, True, [[self.coord[0][0]+400, self.coord[1][0]+400], [self.coord[0][4]+400, self.coord[1][4]+400]])
		pygame.draw.aalines(screen, BLUE, True, [[self.coord[0][1]+400, self.coord[1][1]+400], [self.coord[0][5]+400, self.coord[1][5]+400]])
		pygame.draw.aalines(screen, BLUE, True, [[self.coord[0][2]+400, self.coord[1][2]+400], [self.coord[0][6]+400, self.coord[1][6]+400]])
		pygame.draw.aalines(screen, BLUE, True, [[self.coord[0][7]+400, self.coord[1][7]+400], [self.coord[0][3]+400, self.coord[1][3]+400]])
S = [segment(0,0,0),
	 segment(0,50,0),
	 segment(0,100,0),
	 segment(50,0,0),
	 segment(50,50,0),
	 segment(50,100,0),
	 segment(100,0,0),
	 segment(100,50,0),
	 segment(100,100,0),

	 segment(0,0,50),
	 segment(0,50,50),
	 segment(0,100,50),
	 segment(50,0,50),
	 segment(50,50,50),
	 segment(50,100,50),
	 segment(100,0,50),
	 segment(100,50,50),
	 segment(100,100,50),
	 
	 segment(0,0,100),
	 segment(0,50,100),
	 segment(0,100,100),
	 segment(50,0,100),
	 segment(50,50,100),
	 segment(50,100,100),
	 segment(100,0,100),
	 segment(100,50,100),
	 segment(100,100,100)]

for i in S:
	i.Rotate_X(-math.pi/6,(0,0,0))
	i.Rotate_Y(math.pi/6,(0,0,0))
	i.Rotate_Z(math.pi/6,(0,0,0))
	i.proection()




pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
all_sprites = pygame.sprite.Group()
#all_sprites.add(player)
clock = pygame.time.Clock()
FPS_FONT = pygame.font.SysFont("Verdana", 20)
GOLDENROD = pygame.Color("goldenrod")
 

# Цикл игры
running = True
moutionAZ_ = False
moutionAZ = False
moutionAx_ = False
moutionAx = False
moutionAy_ = False
moutionAy = False
RotateTest = 0
RotateTestD = 0
pos = (400,400)
pos_mouse = (400,400)
Mouse = False
temp1 = (0,0,0)
CTRL = False
cubik = cube.cube(S)

moz =0

#kak = pixelarrey_test.render((800,800), RED)
#kak = RayMarching.render((800,800), RED)

while running:
	screen.fill(BLACK)
	
    # Держим цикл на правильной скорости
	clock.tick(FPS)
	pygame.event.pump()
	
	
	#surface = kak.render()
	#screen.blit(surface, (0, 0))
	
    # Ввод процесса (события)
	for event in pygame.event.get():
        # check for closing window
		if event.type == pygame.QUIT:
			running = False
	
		if pygame.mouse.get_pressed()[0]:
			pass
			#pos_mouse = pygame.mouse.get_pos()
		if not(pygame.mouse.get_pressed()[0]):
			#pos_mouse = (400,400)
			pass
		if pygame.mouse.get_focused():
			pass
			#pos = pygame.mouse.get_pos()
			
			
			
		elif event.type == pygame.MOUSEBUTTONUP:
			#Mouse = False
			#print(pos_mouse)
			pass
		elif event.type == pygame.MOUSEBUTTONDOWN:
			#print(pos_mouse)
			#Mouse = True
			#pos_mouse = (0,0)
			#Mouse = not(Mouse)
			pass	
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				moutionAZ_ = True
			elif event.key == pygame.K_RIGHT:
				moutionAZ = True
			if event.key == pygame.K_UP:
				moutionAx_ = True
			elif event.key == pygame.K_DOWN:
				moutionAx = True
			if event.key == pygame.K_q:
				moutionAy_ = True
			elif event.key == pygame.K_w:
				moutionAy = True
			elif event.key == pygame.K_s:
				if RotateTest == 0:
					RotateTest = 1
			elif event.key == pygame.K_d:
				if RotateTestD == 0:
					RotateTestD = 1
			elif event.key == pygame.K_LCTRL:
				CTRL = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				moutionAZ_ = False
			elif event.key == pygame.K_RIGHT:
				moutionAZ = False
			if event.key == pygame.K_UP:
				moutionAx_ = False
			elif event.key == pygame.K_DOWN:
				moutionAx = False
			if event.key == pygame.K_q:
				moutionAy_ = False
			elif event.key == pygame.K_w:
				moutionAy = False
			elif event.key == pygame.K_s:
				RotateTest = 0
			elif event.key == pygame.K_d:
				RotateTestD = 0
			elif event.key == pygame.K_LCTRL:
				CTRL = False
	rangl()
	if RotateTest==1 and not(CTRL):
		RotateTest = cubik.update("U",1)
	if RotateTestD==1 and not(CTRL):
		RotateTestD = cubik.update("R",1)
	
	if RotateTest==1 and CTRL:
		RotateTest = cubik.update("U",-1)
	if RotateTestD==1 and CTRL:
		RotateTestD = cubik.update("R",-1)
	
		

	#print(S[13].centerCube())
	for i in S:
		i.depthF()
	G = sorted(S, key=lambda section: section.depth,reverse=True)
	temp = (0,0,0)	      
	for i in G:
		if pos_mouse[0]-400 < 0:
			i.Rotate_Y(-ax,temp)
		elif pos_mouse[0]-400 > 0:
			i.Rotate_Y(ax,temp)
			
		if pos_mouse[1]-400 < 0:
			i.Rotate_X(-ay,temp)
		elif pos_mouse[1]-400 > 0:
			i.Rotate_X(ay,temp)
		
		
		#print(i.depth)
		if moutionAZ_:
			az = -math.pi/300
			i.Rotate_Z(az,temp)
			#print(S[0].C,S[1].C,'\n',S[0].depth,S[1].depth)
		elif moutionAZ:
			az = math.pi/300
			i.Rotate_Z(az,temp)
		if moutionAx_:
			ax = -math.pi/300
			i.Rotate_X(ax,temp)
		elif moutionAx:
			ax = math.pi/300
			i.Rotate_X(ax,temp)
		if moutionAy_:
			ay = -math.pi/300
			i.Rotate_Y(ay,temp)
		elif moutionAy:
			ay = math.pi/300
			i.Rotate_Y(ay,temp)
		i.proection()
		i.update1(400,400)
		#i.update()
	pygame.draw.aalines(screen, BLUE, True, [[0, 0], [temp1[0], temp1[1]]])

	
	'''
	if moutionAZ_:
		az = -math.pi/300
		cord = np.dot(Mz(az),cord)
	elif moutionAZ:
		az = math.pi/300
		cord = np.dot(Mz(az),cord)
	if moutionAx_:
		ax = -math.pi/300
		cord = np.dot(Mx(ax),cord)
	elif moutionAx:
		ax = math.pi/300
		cord = np.dot(Mx(ax),cord)
	if moutionAy_:
		ay = -math.pi/300
		cord = np.dot(My(ay),cord)
	elif moutionAy:
		ay = math.pi/300
		cord = np.dot(My(ay),cord)
  
    #all_sprites.update()

	
	#update1(cord,GREEN)
	#update(cord,GREEN)
	self = S[4]
	if moz == 0:
		temp = self.centerCube()
	ax = math.pi/5
	a = temp[1]/math.sqrt(temp[0]**2+temp[1]**2)
	b = temp[0]/math.sqrt(temp[0]**2+temp[2]**2)
	a = math.acos(a)
	b = math.acos(b)
		
	T  =np.array([[1,0,0,-temp[0]],
					  [0,1,0,-temp[1]],
					  [0,0,1,-temp[2]],
					  [0,0,0,1]])
	To =np.array([[1,0,0,temp[0]],
					  [0,1,0,temp[1]],
					  [0,0,1,temp[2]],
					  [0,0,0,1]])
	if moz == 0:			
		xyz = np.dot(T,self.coordP)
		moz +=1
	elif moz == 1:	
		xyz = np.dot(Mx(-a),xyz)
		moz +=1
	elif moz == 2:	
		xyz = np.dot(My(-b),xyz)
		moz +=1
	elif moz == 3:	
		xyz = np.dot(Mx(az),xyz)
		#xyz = np.dot(My(az),xyz)
		#xyz = np.dot(Mx(az),xyz)
		moz +=1
	
	elif moz == 4:	
		xyz = np.dot(My(b),xyz)
		moz +=1
	
	elif moz == 5:	
		xyz = np.dot(Mx(a),xyz)
		moz +=1
	
	elif moz == 6:	
		xyz = np.dot(To,xyz)
		moz +=1
		
	elif moz == 7:	
		self.getCoordP(xyz)
		moz =0
	self.getCoordP(xyz)
	self.proection()
	self.update1(400,400)

	
	
	
	cord = np.dot(Mz(az),cord)
	cord = np.dot(My(ay),cord)
	cord = np.dot(Mx(ax),cord)
	cord1 = np.dot(Mz(az),cord1)
	cord1 = np.dot(My(ay),cord1)
	cord1 = np.dot(Mx(ax),cord1)
	'''
	#pygame.draw.aalines(screen, GREEN, True, [[0, 400], [800, 400]])
	#pygame.draw.aalines(screen, GREEN, True, [[400, 0], [400, 800]])
	
    # Рендеринг
    #all_sprites.draw(screen)
    # После отрисовки всего, переворачиваем экран
	show_fps(screen, clock,S[0].depth,S[1].depth,pos[0],pos[1])
	pygame.display.flip()

pygame.quit()
