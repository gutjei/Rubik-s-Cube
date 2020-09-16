import numpy as np
import math

def Mz(az):			   		   
	a = np.array([[math.cos(az),-math.sin(az),0,0],
			   [math.sin(az),math.cos(az),0,0],
			   [0,0,1,0],
			   [0,0,0,1]], float)
			 
	return a

class cube():
	def __init__(self,sgmnt):
		self.R = [[sgmnt[20],sgmnt[19],sgmnt[18]],
						   [sgmnt[23],sgmnt[22],sgmnt[21]],
						   [sgmnt[26],sgmnt[25],sgmnt[24]]]
						   
		self.L = np.array([[sgmnt[0],sgmnt[1],sgmnt[2]],
						   [sgmnt[3],sgmnt[4],sgmnt[5]],
						   [sgmnt[6],sgmnt[7],sgmnt[8]]])
						   
		self.U = np.array([[sgmnt[0],sgmnt[9],sgmnt[18]],
						   [sgmnt[1],sgmnt[10],sgmnt[19]],
						   [sgmnt[2],sgmnt[11],sgmnt[20]]])
						   
		self.D = np.array([[sgmnt[8],sgmnt[17],sgmnt[26]],
						   [sgmnt[7],sgmnt[16],sgmnt[25]],
						   [sgmnt[6],sgmnt[15],sgmnt[24]]])
						   
		self.F = np.array([[sgmnt[2],sgmnt[11],sgmnt[20]],
						   [sgmnt[5],sgmnt[14],sgmnt[23]],
						   [sgmnt[8],sgmnt[17],sgmnt[26]]])
						   
		self.B = np.array([[sgmnt[18],sgmnt[9],sgmnt[0]],
						   [sgmnt[21],sgmnt[12],sgmnt[3]],
						   [sgmnt[24],sgmnt[15],sgmnt[6]]])
		self.rtte = 0
	def shift(self,lst, steps):
		if steps < 0:
			steps = abs(steps)
			for i in range(steps):
				lst.append(lst.pop(0))
		else:
			for i in range(steps):
				lst.insert(0, lst.pop())
	
	def Rotate_F(self,i):
		self.F = np.rot90(self.F,2+i)
		F_ = [self.U[2][0],self.U[2][1],self.U[2][2],
			  self.R[0][0],self.R[1][0],self.R[2][0],
			  self.D[0][2],self.D[0][1],self.D[0][0],
			  self.L[2][2],self.L[1][2],self.L[0][2]]
		self.shift(F_, i*3)
		
		self.U[2][0]= F_[0]
		self.U[2][1]= F_[1]
		self.U[2][2]= F_[2]
		
		self.R[0][0]= F_[3]
		self.R[1][0]= F_[4]
		self.R[2][0]= F_[5]
		
		self.D[0][2]= F_[6]
		self.D[0][1]= F_[7]
		self.D[0][0]= F_[8]
		
		self.L[2][2]= F_[9]
		self.L[1][2]= F_[10]
		self.L[0][2]= F_[11]
	def Rotate_B(self,i):
		self.B = np.rot90(self.B,2+i)
		F_ = [self.U[0][0],self.U[0][1],self.U[0][2],
			  self.R[0][2],self.R[1][2],self.R[2][2],
			  self.D[2][2],self.D[2][1],self.D[2][2],
			  self.L[2][0],self.L[1][0],self.L[0][0]]
		self.shift(F_, -3*i)
		
		self.U[0][0]= F_[0]
		self.U[0][1]= F_[1]
		self.U[0][2]= F_[2]
		
		self.R[0][2]= F_[3]
		self.R[1][2]= F_[4]
		self.R[2][2]= F_[5]
		
		self.D[2][2]= F_[6]
		self.D[2][1]= F_[7]
		self.D[2][2]= F_[8]
		
		self.L[2][0]= F_[9]
		self.L[1][0]= F_[10]
		self.L[0][0]= F_[11]
	def Rotate_R(self,i):
		self.R = np.rot90(self.R,2+i)
		F_ = [self.U[0][2],self.U[1][2],self.U[2][2],
			  self.F[0][2],self.F[1][2],self.F[2][2],
			  self.D[0][2],self.D[1][2],self.D[2][2],
			  self.B[2][0],self.B[1][0],self.B[0][0]]
		self.shift(F_, -3*i)
		
		self.U[0][2]= F_[0]
		self.U[1][2]= F_[1]
		self.U[2][2]= F_[2]
		
		self.F[0][2]= F_[3]
		self.F[1][2]= F_[4]
		self.F[2][2]= F_[5]
		
		self.D[0][2]= F_[6]
		self.D[1][2]= F_[7]
		self.D[2][2]= F_[8]
		
		self.B[2][0]= F_[9]
		self.B[1][0]= F_[10]
		self.B[0][0]= F_[11]
	def Rotate_L(self,i):
		self.L = np.rot90(self.L,2+i)
		F_ = [self.U[0][0],self.U[1][0],self.U[2][0],
			  self.F[0][0],self.F[1][0],self.F[2][0],
			  self.D[0][0],self.D[1][0],self.D[2][0],
			  self.B[2][2],self.B[1][2],self.B[0][2]]
		self.shift(F_, -3*i)
		
		self.U[0][0]= F_[0]
		self.U[1][0]= F_[1]
		self.U[2][0]= F_[2]
		
		self.F[0][0]= F_[3]
		self.F[1][0]= F_[4]
		self.F[2][0]= F_[5]
		
		self.D[0][0]= F_[6]
		self.D[1][0]= F_[7]
		self.D[2][0]= F_[8]
		
		self.B[2][2]= F_[9]
		self.B[1][2]= F_[10]
		self.B[0][2]= F_[11]
	def Rotate_U(self,i):
		self.U = np.rot90(self.U,2+i)
		F_ = [self.L[0][0],self.L[0][1],self.L[0][2],
			  self.F[0][0],self.F[0][1],self.F[0][2],
			  self.R[0][0],self.R[0][1],self.R[0][2],
			  self.B[0][0],self.B[0][1],self.B[0][2]]
		self.shift(F_, -3*i)
		
		self.L[0][0]= F_[0]
		self.L[0][1]= F_[1]
		self.L[0][2]= F_[2]
		
		self.F[0][0]= F_[3]
		self.F[0][1]= F_[4]
		self.F[0][2]= F_[5]
		
		self.R[0][0]= F_[6]
		self.R[0][1]= F_[7]
		self.R[0][2]= F_[8]
		
		self.B[0][0]= F_[9]
		self.B[0][1]= F_[10]
		self.B[0][2]= F_[11]
	def Rotate_D(self,i):
		self.D = np.rot90(self.D,2+i)
		F_ = [self.L[2][0],self.L[2][1],self.L[2][2],
			  self.F[2][0],self.F[2][1],self.F[2][2],
			  self.R[2][0],self.R[2][1],self.R[2][2],
			  self.B[2][0],self.B[2][1],self.B[2][2]]
		self.shift(F_, -3*i)
		
		self.L[2][0]= F_[0]
		self.L[2][1]= F_[1]
		self.L[2][2]= F_[2]
		
		self.F[2][0]= F_[3]
		self.F[2][1]= F_[4]
		self.F[2][2]= F_[5]
		
		self.R[2][0]= F_[6]
		self.R[2][1]= F_[7]
		self.R[2][2]= F_[8]
		
		self.B[2][0]= F_[9]
		self.B[2][1]= F_[10]
		self.B[2][2]= F_[11]
	def update(self,side,i):
		
		ax = math.pi/10
		if side == "R":
			sides = self.R
			self.Rotate_R(i)
			ax = ax*i
		if side == "L":
			sides = self.L
			self.Rotate_L(i)
			ax = -ax*i
		if side == "U":
			sides = self.U
			self.Rotate_U(i)
			ax = ax*i
		if side == "D":
			sides = self.D
			self.Rotate_D(i)
			ax = -ax*i
		if side == "F":
			sides = self.F
			self.Rotate_F(i)
			ax = ax*i
		if side == "B":
			sides = self.B
			self.Rotate_B(i)
			ax = -ax*i
		
		temp1 = sides[1][1].centerCube()
		
		temp = [0,0,0]
		
		temp[0] = temp1[0]/math.sqrt(temp1[0]**2+temp1[1]**2+temp1[2]**2)
		temp[1] = temp1[1]/math.sqrt(temp1[0]**2+temp1[1]**2+temp1[2]**2)
		temp[2] = temp1[2]/math.sqrt(temp1[0]**2+temp1[1]**2+temp1[2]**2)
		
		#ax = math.pi/6
		
		n = temp[2]
		m = temp[1]
		l = temp[0]
		d = math.sqrt(temp[1]**2+temp[2]**2)
		
		T  =np.array([[1,0,0,-temp[0]],
					  [0,1,0,-temp[1]],
					  [0,0,1,-temp[2]],
					  [0,0,0,1]])
		
		To =np.array([[1,0,0,temp[0]],
					  [0,1,0,temp[1]],
					  [0,0,1,temp[2]],
					  [0,0,0,1]])
		
		Rx = np.array([[1,0,0,0],
				      [0,n/d,m/d,0],
					  [0,-m/d,n/d,0],
					  [0,0,0,1]])
		
		Ry = np.array([[d,0,l,0],
				      [0,1,0,0],
					  [-l,0,d,0],
					  [0,0,0,1]])
		
		for i in sides:
			for j in i:
				
				#xyz = np.dot(T,np.dot(Mx(a),np.dot(My(b),np.dot(Mz(ax),np.dot(My(-b),np.dot(Mx(-a),To))))))
				
				
				xyz = T
				xyz = np.dot(xyz,Rx)
				xyz = np.dot(xyz,Ry)
				
				xyz = np.dot(xyz,Mz(ax))
				
				xyz = np.dot(xyz,np.linalg.inv(Ry))
				xyz = np.dot(xyz,np.linalg.inv(Rx))
				xyz = np.dot(xyz,To)

				xyz = np.dot(xyz,j.coordP)

				j.getCoordP(xyz)
			
		self.rtte += 1
		print(self.rtte)
		if self.rtte == 5:
			self.rtte = 0
			return 2
		else:
			return 1
