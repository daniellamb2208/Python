import PA2a 

class board():
	def __init__(self):
		global W,B

		wk = [(i,j) for i in range(1,3) for j in range(1,9)]
		W=dict(zip(wk,"♜♞♝♛♚♝♞♜♟♟♟♟♟♟♟♟"))
		swv = sorted(W.values())
		B={};#I cannot map the correct position on previouse dictionary
		B[(8,1)],B[(8,8)],B[(8,2)],B[(8,7)] = swv[2],swv[3],swv[6],swv[7]
		B[(8,3)],B[(8,6)],B[(8,4)],B[(8,5)] = swv[4],swv[5],swv[1],swv[0]
		for i in range(1,9):
			B[(7,i)] = swv[-1]

	def __str__(self):
		def DrawRow(r):
			nonlocal s
			for c in range(1,9):
				s+=PA2a.FillInASquare((c+r)%2,pos(r,c).__str__(),(r,c) in W,c)
		s=PA2a.top()
		for r in range(8,0,-1):
			DrawRow(r)
		s+=PA2a.bot()
		return s

class piece():
	def __init__(self,symbol,color):
		self.symbol=symbol
		self.color=color

class pos():
	def __init__(self, x, y):
		self.__where = (x, y)
		self.clr = 0	#initial for remove()
                            
	def __str__(self):
		if self.__where in W:
			return W[self.__where]
		elif self.__where in B:
			return B[self.__where]
		else:
			return " "
                
	def toAset(self):
		return {1} if (self.__where in W) else {2} if (self.__where in B) else set() #the
       

	def substraction(setA):
		if setA == {None}:
			setA -= {None}		#become empty set 
	def __gt__(self,another):	#@total_ordering
		return self.toAset() > another.toAset()
	def __ge__(self,another):
		return self.toAset() >= another.toAset()
	def __lt__(self,another):
		return self.toAset() < another.toAset()
	def __le__(self,another):
		return self.toAset() <= another.toAset()
	def __eq__(self,another):
		return self.toAset() == another.toAset()
	def __ne__(self,another):
		return self.toAset() != another.toAset()
	def __in__(self,another):
		return self.toAset() in another.toAset()
 
	def remove(self):
		rmd_p = ''							#rmd_p (removed_piece)
		try:
			self.clr = 1					#clr (color)
			rmd_p = W[self.__where]			#if False raise Error
			del W[self.__where]				
		except KeyError:
			try:
				self.clr = 2
				rmd_p = B[self.__where]
				del B[self.__where]
			except:
				return None
		return piece(rmd_p, self.clr)	

	def __ilshift__(self,pos_):
		here = pos_.remove()
		assert here != None

		gameover = 0
		if self.clr != pos_.clr:
			there = self.remove()
			if there != None and there.symbol == '♚':
				gameover = 1
		else:
			raise AssertionError

		if pos_.clr == 1:
			W[self.__where] = here.symbol
		else:
			B[self.__where] = here.symbol

		if gameover:
			return True
		
		return False

G=board();  print(G)

p=pos(4,5); p<<=pos(2,5); print(G)
p=pos(5,5); p<<=pos(7,5); print(G)
p=pos(3,6); p<<=pos(1,7); print(G)
p=pos(6,4); p<<=pos(7,4); print(G)
p=pos(4,4); p<<=pos(2,4); print(G)
p=pos(4,7); p<<=pos(8,3); print(G)
p=pos(5,5); p<<=pos(4,4); print(G)
p=pos(3,6); p<<=pos(4,7); print(G)
p=pos(3,6); p<<=pos(1,4); print(G)
p=pos(5,5); p<<=pos(6,4); print(G)
p=pos(4,3); p<<=pos(1,6); print(G)
p=pos(6,6); p<<=pos(8,7); print(G)
p=pos(3,2); p<<=pos(3,6); print(G)
p=pos(7,5); p<<=pos(8,4); print(G)
p=pos(3,3); p<<=pos(1,2); print(G)
p=pos(6,3); p<<=pos(7,3); print(G)
p=pos(5,7); p<<=pos(1,3); print(G)
p=pos(5,2); p<<=pos(7,2); print(G)
p=pos(5,2); p<<=pos(3,3); print(G)
p=pos(7,4); p<<=pos(8,2); print(G)
p=pos(8,2); p<<=pos(7,4); print(G) #not an error, for us
p=pos(8,2); p<<=pos(7,4); print(G) #triggers an error
