# In this file, fill in the ... parts with lines of code. Do not
# create new functions.

from random import seed, randrange
P=" ♟♜♝♞♛♚"; L,R,BL,TL="▌▐▄▀"
Norm='\033[1;m'
BonR=WonR=WonB=DonR=DonB=RonB=GonR=GonB=RonG='\033[1;m\033['
WonR+='7;31;47m' # For drawing a white piece on a red background
WonB+='7;30;47m' # For drawing a white piece on a black background
DonR+='2;37;41m' # For drawing a dark piece on a red background
DonB+='2;37;40m' # For drawing a dark piece on a black background
GonR+='2;33;41m' # For drawing gold on a red background
GonB+='2;33;40m' # For drawing gold on a black background
RonG+='2;31;43m' # For drawing red on a gold background
RonB+='7;30;41m' # For drawing red on a black background
BonR+='0;30;41m' # For drawing black on a red background

def Black(x,w,c):                                          

    if c==0:
        print("   ",GonB+L,end="")
    if w==1:
        print(WonB+x,WonB,end="",sep=" ")
    else:
        print(DonB+x,DonB,end="",sep=" ")
    
    if c==7:
        print(GonB+R+Norm)
    
def Red(x,w,c):

    if c==0:
        print("   ",GonR+L,end="")
    if w==1:
        print(WonR+x,WonR,end="",sep=" ")
    else:
        print(DonR+x,DonR,end="",sep=" ")
    
    if c==7:
        print(GonR+R+Norm)

    
def DrawBoard(B,W):
    def DrawRow(r,B,W):
        
        for i in range(8):   
            if r%2==0:
                if i%2==0:
                    Black(B[i],complex(i,r) in W,i)
                else:
                    Red(B[i],complex(i,r) in W,i)
            else: 
                if i%2==0:
                    Red(B[i],complex(i,r) in W,i)
                else:
                    Black(B[i],complex(i,r) in W,i)

    print("   ",GonB+BL,end="")
    for i in range(4):
        print(2*(GonB+BL),end="")
        print(2*(GonB+BL),end="")
        ++i
    print(GonB+BL+Norm)

    for i in range(8):               #draw
        DrawRow(i,B[i],W)
    
    print("   ",GonB+TL,end="")
    for i in range(4):
        print(2*(GonB+TL),end="")
        print(2*(GonB+TL),end="")
        #++i
    print(GonB+TL+Norm)

def DrawAnInitialBoard():
    a=P[2:7]+P[4:1:-1]
    b=P[1]*8
    c=P[0]*8
    B =[a,b,c,c,c,c,b,a]
    W = []
    for i in range(8):
        for j in range(2):
            W += [complex(i,j)]

    DrawBoard(B,W)


DrawAnInitialBoard()
    
def DrawRandomBoard():                                
    def RandomPlacement(color,otherColor):
        while(len(color)<16): 
            new = complex(randrange(8),randrange(8))
            if (not (new in color)) and (not(new in otherColor)):
                color += [new]

    seed(0) # Comment this line to make it run differently each time
    W=[];D=[];B=[];C=[];temp="";Final=[]; #This B object is the board. 
    RandomPlacement(W, D)
    RandomPlacement(D, W)

    charA=P[2:7]+P[4:1:-1]+P[1]*8         #chess
    charB=P[1]*8+P[4:1:-1]+P[2:7]
    for i in range(8):                   #position
        for j in range(8):            
            C += [complex(i,j)]              #C with [x,y]
            B += [""]	                     #B with length of 64[" "]

    for i in range(len(W)):              #insert random W into B
        del B[C.index(W[i])]                 #replace [" "] with chess char
        B.insert(C.index(W[i]),charA[i])    

    for i in range(len(D)):              #same as W
        del B[C.index(D[i])]
        B.insert(C.index(D[i]),charB[i])

    for i in range(8):                   #create playbook of chess
        for j in range(8):               #from 64 elements to 8 strings
            if B[i+(j*8)]=="":               #error but revised
                B[i+(j*8)]=" "
            temp += B[i+(j*8)]

        Final += [temp]
        temp = ""
    
    DrawBoard(Final,W)

DrawRandomBoard()
