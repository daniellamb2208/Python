from random import seed, randrange
P=" ♟♜♞♝♛♚"; L,R,BL,TL="▌▐▄▀"
Norm='\033[1;m'
BonR=WonR=WonB=DonR=DonB=RonB=GonR=GonB=RonG='\033[1;m\033['
WonR+='7;31;47m'; WonB+='7;30;47m'; DonR+='2;37;41m'; DonB+='2;37;40m'; 
GonR+='2;33;41m'; GonB+='2;33;40m'; RonG+='2;31;43m'; RonB+='7;30;41m'; BonR+='0;30;41m'; 

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


a=P[2:7]+P[4:1:-1]
b=P[1]*8
c=P[0]*8
B =[a,b,c,c,c,c,b,a]
W = []
for i in range(8):
    for j in range(2):
        W += [complex(i,j)]

color = 0; #0 fo while

l = ['R','N','B','Q','K','B','N','R']
P = ['P']*8
s = [' ']*8
Bc = s + s + s + s + s + s + P + l
Wc = l + P + s + s + s + s + s + s
position = []
for i in ('8','7','6','5','4','3','2','1'):
    for j in ('a','b','c','d','e','f','g','h'):
        position += [j+i]
who=''             #which chess,where is it before moved,where will it move to
wheau=''
whaug=''
wx=''

def GetAMove():
    global B,W
    global color
    global Bc,Wc
    global who,wheau,whaug,wx
    who=''             
    wheau=''
    whaug=''
    wx=''
    move = input()

    (Islegal,color,cango) = Legal(*move,c=color)
    
    if Islegal == False or wheau == False or whaug == False or who == False or wx == False:
        print("Wrong move, try again.\n")
        return (B,W);
    
    if wx == 'x':
        if color == 1:           #now white board but eat rival chess
            if  whaug != 'a8':
                Bc = Bc[:position.index(whaug)] + [' '] + Bc[position.index(whaug)+1:]
            elif whaug == 'a8':
                Bc = [' '] + Bc[1:]
        elif color == 0:
            if  whaug != 'a8':
                Wc = Wc[:position.index(whaug)] + [' '] + Wc[position.index(whaug)+1:]
            elif whaug == 'a8':
                Wc = [' '] + Wc[1:]
 
    elif not (wx == 'x' or wx == ''):
        return (B,W)
    
    if color == 1:                                   #represent white because it's been changed
        if wheau != 'a8' and whaug != 'a8':
            Wc = Wc[:position.index(wheau)] + [' '] + Wc[position.index(wheau)+1:]
            Wc = Wc[:position.index(whaug)] + [who] + Wc[position.index(whaug)+1:]
        elif wheau == 'a8':
            Wc = [' '] + Wc[1:]
            Wc = Wc[:position.index(whaug)] + [who] + Wc[position.index(whaug)+1:]
        else:
            Wc = Wc[:position.index(wheau)]+[' '] + Wc[position.index(wheau)+1:]
            Wc = [who] + Wc[1:]
    elif color == 0:
        if wheau != 'a8' and whaug != 'a8':
            Bc = Bc[:position.index(wheau)] + [' '] + Bc[position.index(wheau)+1:]
            Bc = Bc[:position.index(whaug)] + [who] + Bc[position.index(whaug)+1:]
        elif wheau == 'a8':
            Bc = [' '] + Bc[1:]
            Bc = Bc[:position.index(whaug)] + [who] + Bc[position.index(whaug)+1:]
        else:
            Bc = BWc[:position.index(wheau)]+[' '] + Bc[position.index(wheau)+1:]
            Bc = [who] + Bc[1:]
          
    Ro = ['♜']; kN = ['♞'];Pa = ['♟'];Bi = ['♝']; Qn = ['♛']; Kg = ['♚']
#    print(Bc,Wc)    
    B =[]
    for i in range(64):                    
        if Bc[i] != ' ':
            if Bc[i] == 'R':
                B += Ro 
            elif Bc[i] == 'N':
                B += kN
            elif Bc[i] == 'B':
                B += Bi
            elif Bc[i] == 'Q':
                B += Qn
            elif Bc[i] == 'K':
                B += Kg
            elif Bc[i] == 'P':
                B += Pa
        elif Wc[i] != ' ':
            if Wc[i] == 'R':
                B += Ro 
            elif Wc[i] == 'N':
                B += kN
            elif Wc[i] == 'B':
                B += Bi
            elif Wc[i] == 'Q':
                B += Qn
            elif Wc[i] == 'K':
                B += Kg
            elif Wc[i] == 'P':
                B += Pa
        else:
            B += [' ']
#    print(B)
    tb = ''
    ttb = []
    for i in range(8):
        for j in range(8):
            tb += B[i*8+j]
        ttb +=  [tb]
        tb = ''
    B = ttb 
            
      
    te =[]    

    for i in range(64):
        if Wc[i] != ' ':
            te += [complex(int(i%8),int(i/8))]
    W = te    

    return(B,W) 
#    
def Legal(*m,c):
    
    if SyntacticallyLegal(*m):

        where = SemanticallyLegal(*m,colored=c)
        
        origin = ''                 #origin input
        for i in m:
            origin += i
        
        if where == False:
            return (False,c,0)
        elif c == 1:
            return (True,0,where)
        elif c == 0:
            return (True,1,where)
    else:
        return (False,c,0)
#
def SyntacticallyLegal(*m):

    legal_alph = ("K","Q","B","N","R","x","a","b","c","d","e","f","g","h")

    if (m[0],) == m:           #avoid input only one character
        return False

    for i in m:

        if i in legal_alph:
            continue
        elif i.isdigit() :
            j = int(i)
            if 0<=j<=8:
                continue 
        else:
            return False

    ingo = m[-2]+m[-1]

    if ingo in position:
        return True
    else:
        return False
#
def SemanticallyLegal(*m,colored):
    def conv(i):           #alpha to num
        if i == 'a':
            return 0
        elif i == 'b':
            return 1
        elif i == 'c':
            return 2
        elif i == 'd':
            return 3
        elif i == 'e':
            return 4
        elif i == 'f':
            return 5
        elif i == 'g':
            return 6
        elif i == 'h':
            return 7
        else:
            return False
    def cconv(i):          #num to alpha
        if i == 0:
            return 'a'
        elif i == 1:
            return 'b'
        elif i == 2:
            return 'c'
        elif i == 3:
            return 'd'
        elif i == 4:
            return 'e'
        elif i == 5:
            return 'f'
        elif i == 6:
            return 'g'
        elif i == 7:
            return 'h'
        else:
            return False

    def another(index,chess,inchs):
#        print('Second find')
        copychess = []
        for i in chess:
            copychess += i 
        removed = copychess.index(inchs)
        copychess.remove(inchs)
        copychess.insert(removed," ")
        if copychess.index(inchs) == index:
            return True
        else:
            return False#    

    if colored == 1:
        chess = Bc
        othch = Wc
    elif colored == 0:
        chess = Wc
        othch = Bc

    inchs = ''                  # classify input
    ingo = m[-2]+m[-1]
    inpos = ''
    inx = ''
    if m == (m[0],m[1]):
        m = ()        
    elif m[-3] == 'x':          # exist 'x' or not
        inx = m[-3]
        m = m[:-3]
        
    else:
        m = m[:-2]
    if m == ():
        inchs = 'P'
        m=()
    elif m[0].isupper():        #upper chess
        inchs = m[0]
        if m == (m[0]):         #no input position
            inpos = ''
        else:
            m = m[1:]
            for i in m:
                inpos += i
    else:                       #something about position
        for i in m:
            inpos += i
    if inchs == '':
        inchs ='P'
#    print(inchs,inpos,inx,ingo)
    def anotherindex(inchs,now=chess):
            copychess = []
            for i in now:
                copychess += i 
            removed = copychess.index(inchs)
            copychess.remove(inchs)
            copychess.insert(removed," ")
            if inchs in copychess: 
                return copychess.index(inchs)  
            else:
                return False#    
    
    def nopi(inchs,ingo,inx,now=chess,rival=othch):              #no origin position input (inpos == ' ')

        if ( rival[position.index(ingo)] != ' ' and inx == 'x' ) or ( now[position.index(ingo)] == ' ' and inx != 'x' ):
            c1 = chess.index(inchs)
            xc1 =  int( conv(ingo[0]) - conv(position[c1][0]) )                
            yc1 =  (-1) * ( int(ingo[1]) - int(position[c1][1]) )

            c2 = anotherindex(inchs)
            if c2 ==False:
                return position[c1]
            else:
                xc2 =  int( conv(ingo[0]) - conv(position[c2][0]) )                
                yc2 =  (-1) * ( int(ingo[1]) - int(position[c2][1]) )                           
                                    
            if inchs == 'R':
                if ((xc1 == 0 and yc1) or (xc1 and yc1 == 0)) and (not ( (xc2 == 0 and yc2)or(xc2 and yc2 == 0) ) ):
                    return position[c1]
                elif  (not((xc1 == 0 and yc1) or (xc1 and yc1 == 0))) and ( (xc2 == 0 and yc2)or(xc2 and yc2 == 0) ):
                    return position[c2]
                elif ((xc1 == 0 and yc1)or(xc1 and yc1 == 0)) and ((xc2 == 0 and yc2)or(xc2 and yc2 == 0)):
                    return position[min(c1,c2)]
                else:
                    return False

            elif inchs == 'N':
                if ( (abs(xc1)==1 and abs(yc1)==2) or (abs(xc1)==2 and abs(yc1)==1) ) and (not ( (abs(xc2)==2 and abs(yc2)==1) or ( abs(xc2)==1 and abs(yc2)==2) ) ):
                    return position[c1]
                elif ((not (abs(xc1)==1 and abs(yc1)==2) or (abs(xc1)==2 and abs(yc1)==1) )) and ( (abs(xc2)==2 and abs(yc2)==1) or ( abs(xc2)==1 and abs(yc2)==2) ):
                    return position[c2]
                elif ( (abs(xc1)==1 and abs(yc1)==2) or (abs(xc1)==2 and abs(yc1)==1) ) and ( (abs(xc2)==2 and abs(yc2)==1) or ( abs(xc2)==1 and abs(yc2)==2) ):
                    return position[min(c1,c2)]
                else:
                    return False

            elif inchs == 'B':
                if abs(xc1)==abs(yc1) and (not (abs(xc2)== abs(yc2))):
                    return position[c1]
                elif (not (abs(xc1)==abs(yc1))) and abs(xc2)== abs(yc2):
                    return position[c2]
                elif abs(xc1)==abs(yc1) and abs(xc2)== abs(yc2):
                    return position[min(c1,c2)]
                else:
                    return False
            
        return False     

    def wocp(p,chess,inchs,g=ingo,x=inx):      #inpos,chess,inchs      #return p "a8"       #where origin chess position
        
        c1 = int (chess.index(inchs))          # 0-63 
        if inchs =='Q' or inchs == 'K':
            return position[c1]                #  position[0]='a8'
        else:
            c2 = int (anotherindex(inchs))
            if c2 == False:
                return position[c1]

        if p in position:                 #eg: 'a8'         
            return p

        elif p.isdigit():            
            if int(p) == (c1//8) and int(p) == (c2//8):
                if cmc(inchs,c1,p) and cmc(inchs,c2,p):
                    return position[min(position.index(c1),position.index(c2))]  
                elif cmc(inchs,c1,p) and not cmc(inchs,c2,p):
                    return position[c1]
                elif not cmc(inchs,c1,p) and cmc(inchs,c2,p):
                    return position[c2]
                else: 
                    return False
            elif int(p) == 8-(c1//8) :
                return position[c1]
            elif int(p) == 8-(c2//8) :
                return position[c2]  
            else:
                return False

        elif p.isalpha() and not p.isalnum(): #alpha  
            if c1%8 == c2%8:
                if cmc(inchs,c1,p) and cmc(inchs,c2,p):
                    return position[min(position.index(c1),position.index(c2))]
                elif cmc(inchs,c1,p) and not cmc(inchs,c2,p):
                    return position[c1]
                elif not cmc(inchs,c1,p) and cmc(inchs,c2,p):
                    return position[c2]
                else:
                    return False
            elif c1%8 == conv(p):
                return position[c1]
            elif c2%8 == conv(p):
                return position[c2]
            else:
                return False

        else:
            return nopi(inchs,g,x)                       #     no inpos

         
######################################################
                                                     #check move can go? and something on its road
    def cmc(ch,posi,go,now,rival,inpos=''):       #posi is which right chess      
                                                     #(ichs,where chess,ingo,chess,othch)
        if posi == False:                            #if any barrier return False   
            return posi   
#        print(ch,posi,go,color,inpos)############################
        x =  int( conv(go[0]) - conv(posi[0]) )                #DELTA x y for computer
        y =  (-1) * ( int(go[1]) - int(posi[1]) )
#        print(x,y)###################
        if ch == 'P':
            if inpos.isalpha() and inpos != posi[0]:
                return False
            elif inpos.isdigit() and inpos != posi[1]:
                return False
            elif inpos != '' and inpos != posi:
                return False 
            if colored == 0:
                if int(posi[1]) == 7:
                    if not (y==1 or y==2):
                        return False
                else:
                    if y!=1:
                        return False
            elif colored ==1 :
                if int(posi[1]) == 2:
                    if not (y==-1 or y==-2):
                        return False
                else:
                    if y!=-1:
                        return False
            if abs(x) == abs(y) == 1:
                if rival[int(conv(go[0])) + (8-int(go[1]))*8] == ' ':
                    return False
            return True       

        else:
            if ch == 'R':                            ######      Rook
                if x != 0 and y == 0 :
                    if x<0:
                        start = -1
                        while start != x:
                            if now[ int(conv(posi[0])) + start + (8-int(posi[1]))*8 ] == ' ' and rival[ int(conv(posi[0])) + start + (8-int(posi[1]))*8 ] == ' ':
                                start -= 1
                            else:
                                return False  
                    if x>0:
                        start = 1
                        while start != x: 
                            if now[ int(conv(posi[0])) + start + (8-int(posi[1]))*8 ] == ' ' and rival[ int(conv(posi[0])) + start + (8-int(posi[1]))*8 ] == ' ':
                                start += 1
                            else:
                                return False

                                
         
                elif x == 0 and y != 0:
                    if y<0:
                        start = -1
                        while start != y:
                            if now[ int(conv(posi[0])) + (8-int(posi[1])+start)*8 ] == ' ' and rival[ int(conv(posi[0])) + (8-int(posi[1])+start)*8 ] == ' ':
                                start -= 1 
                            else:
                                return False  
                    if y>0:
                        start = 1
                        while start != y:
                            if now[ int(conv(posi[0])) + (8-int(posi[1])+start)*8 ] == ' ' and rival[ int(conv(posi[0])) + (8-int(posi[1])+start)*8 ] == ' ':
                                start += 1                                
                            else:
                                return False  
                else :
                    return False
                
            elif ch == 'N':                             ####  kNight
                if not ( (abs(x) == 2 and abs(y) == 1)  or  (abs(x) == 1 and abs(y) == 2) ):
                    return False

            elif ch == 'B':                             ####Bishop
                if not abs(x) == abs(y):
                    return False
                else:
                    if x>0 and y>0:
                        sx = 1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 + sx*9] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  + sx*9] == ' ':
                                print(int(conv(posi[0])) + (8-int(posi[1]))*8 + sx*9)
                                sx +=1
                            else:
                                return False
                    elif x>0 and y<0:
                        sx = 1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 - sx*7] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  - sx*7] == ' ':
                                sx +=1
                            else:
                                return False
                    elif x<0 and y>0:
                        sx = -1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 - sx*7] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  - sx*7] == ' ':
                                sx -=1
                            else:
                                return False
                    elif x<0 and y<0:
                        sx = -1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 + sx*9] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  + sx*9] == ' ':
                                sx -=1
                            else:
                                return False
            elif ch == 'Q':                            ###Queen 
                if abs(x) == abs(y):
                    if x>0 and y>0:
                        sx = 1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 + sx*9] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  + sx*9] == ' ':
                                sx +=1
                            else:
                                return False
                    elif x>0 and y<0:
                        sx = 1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 - sx*7] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  - sx*7] == ' ':
                                sx +=1
                            else:
                                return False
                    elif x<0 and y>0:
                        sx = -1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 - sx*7] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  - sx*7] == ' ':
                                sx -=1
                            else:
                                return False
                    elif x<0 and y<0:
                        sx = -1
                        while sx != x :
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 + sx*9] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8  + sx*9] == ' ':
                                sx -=1
                            else:
                                return False

                elif (x == 0 and y != 0):
                    if y>0:
                        sy = 1
                        while sy != y:
                            if now[int(conv(posi[0])) + (8-int(posi[1])+sy)*8 ] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1])+sy)*8] == ' ':\
                                sy += 1 
                            else:
                                return False

                    elif y<0:
                        sy = -1
                        while sy != y:
                            if now[int(conv(posi[0])) + (8-int(posi[1])+sy)*8 ] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1])+sy)*8] == ' ':
                                sy -= 1 
                            else:
                                return False
                            

                elif (y == 0 and x != 0):
                    if x>0:
                        sx = 1
                        while sx != x:
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 +sx ] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8 +sx] == ' ':
                                sx += 1
                            else:
                                return False
                            sx += 1

                    elif x<0:
                        sx = -1
                        while sx != x:
                            if now[int(conv(posi[0])) + (8-int(posi[1]))*8 +sx] == ' '  and rival[ int(conv(posi[0])) + (8-int(posi[1]))*8 +sx ] == ' ':
                                sx -= 1
                            else:
                                return False
                else:
                    return False

            elif ch == 'K':                        #### King
                if (abs(x) == abs(y) == 1) or (x == 0 and abs(y) == 1) or (abs(x) == 1 and y == 0):
                    return True
                else:
                    return False

        return True

    def opcp(go,inx,chess,othch,inpos): # find where P  #return eg 'a8'     #### origin P chess position
            
        maybe = []
        if inx == 'x':
            if not othch[position.index(go)]==' ':
                if 0<=position.index(go)+7<64 and chess[position.index(go)+7] == 'P':
                    maybe += [position.index(go)+7] 
                elif 0<=position.index(go)+9<64 and chess[position.index(go)+9] == 'P':
                    maybe += [position.index(go)+9]
                elif 0<=position.index(go)-7<64 and chess[position.index(go)-7] == 'P':
                    maybe += [position.index(go)-7]
                elif 0<=position.index(go)-9<64 and chess[position.index(go)-9] == 'P':
                    maybe += [position.index(go)-9]

            if maybe == []:
                return False
            maybe.sort()
            return position[maybe[0]]
        else:
            if colored == 0:
                if 8 <= position.index(go) - 8 <= 63 and chess[position.index(go) - 8] == 'P' :
                    return position[position.index(go) - 8]
                elif int(position.index(go)/8) == 3 and chess[position.index(go) - 16] == 'P' :
                    return position[position.index(go) - 16]
            elif colored == 1:
                if 0 <= position.index(go) - 8 <= 55 and chess[position.index(go) + 8] == 'P':
                    return position[position.index(go) + 8]
                elif chess[position.index(go) + 16] == 'P' and int(position.index(go)/8) == 4 :
                    return position[position.index(go) + 16]
        return False 
    
    global who,wheau,whaug,wx      #which chess,where is it before moved,where will it move to
 
    wx = inx    ### 'x'
    if wheau == False or whaug == False or who == False or wx == False:
        return False 
    if chess[position.index(ingo)] == " " and othch[position.index(ingo)] == " ":   # arrive destination?? P
        if inchs == 'P':
            if cmc('P',opcp(ingo,inx,chess,othch,inpos),ingo,chess,othch,inpos):
                who='P';wheau=opcp(ingo,inx,chess,othch,inpos);whaug=ingo;wx=inx
                return True

        elif cmc(inchs,wocp(inpos,chess,inchs),ingo,chess,othch,inpos):
            who=inchs;wheau=wocp(inpos,chess,inchs);whaug=ingo;wx=inx              
            return True

    elif inx == 'x' and othch[position.index(ingo)] != ' ':
        if inchs == 'P':
            if cmc('P',opcp(ingo,inx,chess,othch,inpos),ingo,chess,othch,inpos):
                who='P';wheau=opcp(ingo,inx,chess,othch,inpos);whaug=ingo;wx=inx                
                return True

        elif cmc(inchs,wocp(inpos,chess,inchs),ingo,chess,othch,inpos):
            who=inchs;wheau=wocp(inpos,chess,inchs);whaug=ingo;wx=inx 
            return True
    else:
        return False

    return False
#
def PlayGame():
    global B,W
    DrawBoard(B,W)
    (B,W) = GetAMove()
#
while True:
    PlayGame()






    

