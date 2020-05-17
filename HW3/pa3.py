import PA2a

Symbol=dict(zip("PRBNQK","♟♜♝♞♛♚"))
class board():
    def __init__(self):
        global W,B
        W={(1+x//8,1+x%8):p for x,p in zip (range(16),"♜♞♝♛♚♝♞♜♟♟♟♟♟♟♟♟")}
        B={(7+x//8,1+x%8):p for x,p in zip (range(16),reversed(list(W.values())))}
    def __str__(self):
        def DrawRow(r):
            nonlocal s
            for c in range(1,9):
                s+=PA2a.FillInASquare((c+r)%2,pos(r,c).__str__(), (r,c) in W,c)
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
    def __init__(self,x,y): self.__pos = (x,y)
    def __str__(self):
        if self.__pos in W: return W[self.__pos]
        if self.__pos in B: return B[self.__pos]
        return " "
    def toAset(self):
        return {1} if self.__pos in W else {2} if self.__pos in B else set()
    def __contains__(self,color): return self.toAset == {color}-{None} 
    def __eq__(self,color): return self.toAset == {color}-{None} 
    def __ne__(self,color): return self.toAset != {color}-{None} 
    def __ge__(self,color): return self.toAset >= {color}-{None} 
    def __le__(self,color): return self.toAset <= {color}-{None} 
    def __gt__(self,color): return self.toAset >  {color}-{None} 
    def __lt__(self,color): return self.toAset <  {color}-{None}
    def remove(self):
        try:
            p=piece(W[self.__pos],1)
            del W[self.__pos]
        except:
            try:
                p=piece(B[self.__pos],2)
                del B[self.__pos]
            except:return None
        return p
    def __ilshift__(self,pos_):
        piece = pos_.remove()
        assert piece
        was = self.remove()
        if piece.color==1: W.update({self.__pos:piece.symbol})
        else: B.update({self.__pos:piece.symbol})
        return was and was.symbol=='K'

G=board();  print(G)
p=pos(4,5); p<<=pos(2, 5); print(G)
p=pos(5,5); p<<=pos(7, 5); print(G)
p=pos(3,6); p<<=pos(1, 7); print(G)
p=pos(6,4); p<<=pos(7, 4); print(G)
p=pos(4,4); p<<=pos(2, 4); print(G)
p=pos(4,7); p<<=pos(8, 3); print(G)
p=pos(5,5); p<<=pos(4, 4); print(G)
p=pos(3,6); p<<=pos(4, 7); print(G)
p=pos(3,6); p<<=pos(1, 4); print(G)
p=pos(5,5); p<<=pos(6, 4); print(G)
p=pos(4,3); p<<=pos(1, 6); print(G)
p=pos(6,6); p<<=pos(8, 7); print(G)
p=pos(3,2); p<<=pos(3, 6); print(G)
p=pos(7,5); p<<=pos(8, 4); print(G)
p=pos(3,3); p<<=pos(1, 2); print(G)
p=pos(6,3); p<<=pos(7, 3); print(G)
p=pos(5,7); p<<=pos(1, 3); print(G)
p=pos(5,2); p<<=pos(7, 2); print(G)
p=pos(5,2); p<<=pos(3, 3); print(G)
p=pos(7,4); p<<=pos(8, 2); print(G)
p=pos(8,2); p<<=pos(7, 4); print(G)
p=pos(8,2); p<<=pos(7, 4); print(G)
