from PA1 import *
Symbol={"P":"♟","R":"♜","B":"♝","N":"♞","Q":"♛","K":"♚"}

def ColorOf(y,x):
    if not ((0<=y<=7) and (0<=x<=7)): return(99)
    if complex(y,x) in W: return 1
    return -(G[y][x]!=' ')

def WhosThere(y,x):
    color=ColorOf(y,x)
    if color==99: return 'x', 99
    return G[y][x],color

def GetAMove(color=[1]):
    while True:
        M=input("    "+["Dark",0,"White"][color[0]+1]+"'s move: "+WonB[:5])
        ans = Legal(color[0],*M)
        if ans: break
    color[0]*=-1
    return (*ans,(8-int(M[-1]),ord(M[-2])-ord('a')))

def Legal(c,*move):
    if not SyntacticallyLegal(*move): return False
    return SemanticallyLegal(c,*move)

def SyntacticallyLegal(*move):
    if len(move)<2: return False
    if move[-1] not in '12345678': return False
    if move[-2] not in 'abcdefgh': return False
    m = list(move[:-2])
    if len(m)==0: return True
    if m[0].islower(): m.insert(0,'P')
    if m[-1] == 'x': del m[-1]
    if len(m)==0: return True
    if m[-1] not in '12345678': m.append('1')
    if m[-2] not in 'abcdefgh': m.insert(1,'a')
    if len(m)!=3: return False
    return (m[0] in 'PRNBQK') and (m[1] in 'abcdefgh') and (m[2] in '12345678')
    
def SemanticallyLegal(c,*move):
    m = list(move)
    if m[0].islower(): m.insert(0,'P')    
    TO=(8-int(m[-1]),ord(m[-2])-ord('a'))
    #TO=(ord('h')-ord(m[-2]),int(m[-1])-1)
    if ColorOf(*TO)==c: return False # Can't move over your own piece 
    if ColorOf(*TO)==0 and m[-3]=='x': return False # Nothing to take
    if ColorOf(*TO)!=0 and m[-3]!='x': return False # Forgot to say to take
    x=WhereAreAllOfThePiecesOfThisTypeThatCanGetHere(m[0],*TO,c,m[-3]=='x')
    if len(x)==0: return False # Nothing could move here
    if m[-3]=='x': del m[-3]
    if len(x)==1 and len(m)!=3: return False # If just 1, should be no extra
    if len(x)==1: return x
    if len(m)==3: return False # Forgot to disambiguate
    p=m[1].islower()+1
    if p==2:
        which=WhichThisFile(x,ord(m[1])-ord('a'))
        if not which: return False #No match
        if len(which)== 1 and len(m)!=4: return False
        if len(which) > 1 and len(m)!=5: return False
    if m[p].isdigit(): 
        which=WhichThisRank(x,8-int(m[p]))
        if not which: return False #No match
        if len(which)!=1 and p==1: return False#Rank not unique, need File too.
        if len(which)==1 and p==2: return False#Rank unique, why gave File too?
        numFile = len(WhichThisFile(x,which[0][1]))
        if numFile == 1 and p==1: return False#File unique, why Rank instead?
        if p==2: which=[(8-int(m[p]),ord(m[1])-ord('a')),]
    return which

def WhichThisRank(x,R):
    which=[]
    for i in x:
        if i[0] == R: which += [i]
    return which

def WhichThisFile(x,F):
    which=[]
    for i in x:
        if i[1] == F: which += [i]
    return which

def GetTheFromOffsets(piece,y,x,c,X):
    fromoffset=[]  
    if piece=='P':
        if not X: # Pawn moves differently when taking (even ignoring en pass.)
            fromoffset=[(c,0)]
            if y-3==(c+1)>>1 and WhosThere(y+c,x)[0]==' ':#Condition for double
                fromoffset+=[(c+c,0)] #Allow to move 2 squares
        else:
            fromoffset=[(c,-1),(c,1)] #These are the 2 diagonals
    elif piece=='N':
        for i in [-2,-1,1,2]:
            for j in [abs(i)-3,3-abs(i)]:
                fromoffset+=[(i,j)]
    else:
        for i in [-1,0,1]:
            for j in [-1,0,1]:
                if i or j:
                    if i==0 or j==0:
                        if piece in "RQK": fromoffset+=[(i,j)]
                    else:
                        if piece in "BQK": fromoffset+=[(i,j)]
    return fromoffset
                        
def WhereAreAllOfThePiecesOfThisTypeThatCanGetHere(piece,y,x,c,X):
    fromoffset=GetTheFromOffsets(piece,y,x,c,X)
    Ans=[]
    for offset in fromoffset:
        for d in range(1,8):
            who,color=WhosThere(y+d*offset[0],x+d*offset[1])
            if who==Symbol[piece] and color==c:
                Ans+=[(y+d*offset[0],x+d*offset[1])]
                break
            if who!=" ": break # Hit a block
            if piece in "KNP": break # These pieces have bounded movement
    return Ans
     
def PlayGame():
    while True:
        DrawBoard(G,W)
        UpdateBoard(*GetAMove())
        
def UpdateBoard(Fr,To):
    P,C=WhosThere(*Fr)
    if (C!=white) and (complex(*To) in W): W.remove(complex(*To))
    G[To[0]]=G[To[0]][:To[1]]+P+G[To[0]][To[1]+1:]
    G[Fr[0]]=G[Fr[0]][:Fr[1]]+" "+G[Fr[0]][Fr[1]+1:]
    if (C==white): W[W.index(complex(*Fr))]=complex(*To)

white=1;G=[];W=[]
InitializeBoard(G,W)
PlayGame()
