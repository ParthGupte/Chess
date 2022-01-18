import pandas as pd 
import numpy as np
import math as mt   
def board():
    A={1:'R2',2:'K2',3:'B2',4:'Q2',5:'E2',6:'B2',7:'K2',8:'R2'}
    B={1:'P2',2:'P2',3:'P2',4:'P2',5:'P2',6:'P2',7:'P2',8:'P2'}
    C={}
    D={}
    E={}
    F={}
    G={1:'P1',2:'P1',3:'P1',4:'P1',5:'P1',6:'P1',7:'P1',8:'P1'}
    H={1:'R1',2:'K1',3:'B1',4:'Q1',5:'E1',6:'B1',7:'K1',8:'R1'}
    dic={1:A,2:B,3:C,4:D,5:E,6:F,7:G,8:H}
    b=pd.DataFrame(dic)
    b=b.T
    b=b.fillna(' ')
    return b
def move(m,b):
    a=b.at[m[0][0],m[0][1]]
    b.at[m[0][0],m[0][1]]=' '
    b.at[m[1][0],m[1][1]]=a
    return b
def obs(m,b):
       [[r1,c1],[r2,c2]]=m
       tR=[r1,r2]
       tC=[c1,c2]
       tR.sort()
       tC.sort()
       T=b.loc[tR[0]:tR[1],tC[0]:tC[1]]
       look=T.copy(deep=True)
       look.at[r1,c1]=look.at[r2,c2]=np.NaN
       L=[]
       if 'K' not in str(b.at[r1,c1]):
           if c2-c1==0:
               return bool(look.count()[c1])
           else:
               s=(r2-r1)/(c2-c1)
               for r in look.axes[0]:
                   for c in look.axes[1]:
                       if c==c1:
                           continue
                       S=(r-r1)/(c-c1)
                       if S==s:
                           L.append(str(look.at[r,c])==str(np.NaN))
               return False in L
       else:
            return False

def valid(m,n,b):
    t=(-1)**(n)
    n1=str(n)
    if n1=='1':
        n2='2'
    else:
        n2='1'

    [[r1,c1],[r2,c2]]=m
    if 1<=r1<=8 and 1<=r2<=8 and 1<=c1<=8 and 1<=c2<=8:
        frm=str(b.at[r1,c1])
        to=str(b.at[r2,c2])
        if (n1 in frm) and (n1 not in to):
            if m[0]!=m[1]:
                if 'P' in frm:
                    if n2 not in to:
                        if c1-c2==0:
                            if r2-r1==2*t:
                                if n==1:
                                    return r1==7
                                else:
                                    return r1==2

                        else:
                            return r2-r1==t and ((c2-c1==0 and to=='nan') or (mt.fabs(c2-c1)==1 and to!='nan'))
                elif 'R' in frm:
                    return r1==r2 or c1==c2
                elif 'B' in frm:
                    return mt.fabs(r2-r1)==mt.fabs(c2-c1)
                elif 'Q' in frm:
                    return r1==r2 or c1==c2 or mt.fabs(r2-r1)==mt.fabs(c2-c1)
                elif 'K' in frm:
                    return mt.fabs(r2-r1)==0.5*mt.fabs(c2-c1) or mt.fabs(r2-r1)==2*mt.fabs(c2-c1) 
                elif 'E' in frm:
                    if (mt.fabs(r2-r1)==1 and mt.fabs(c2-c1)==0) or (mt.fabs(r2-r1)==0 and mt.fabs(c2-c1)==1) or mt.fabs(c2-c1)==mt.fabs(r2-r1)==1:
                        return True
                    else:
                        return False
                else:
                    return False
            else:
                return False
    else:
        return False

def legal(m,n,b):
    return (valid(m,n,b) and not obs(m,b))

def check(Ep1,Ep2,b):
    D={1:[],2:[]}
    for r in b.axes[0]:
        for c in b.axes[1]:
            m1=[[r,c],Ep1]
            m2=[[r,c],Ep2]
            D[1].append(legal(m1,2,b))
            D[2].append(legal(m2,1,b))        
    return {1:(True in D[1]),2:(True in D[2])}
def castle(m,n,b,Efst,Rfst):
    [[r1,c1],[r2,c2]]=m
    if (('E'+str(n))  in str(b.at[r1,c1])) and (mt.fabs(r2-r1)==0 and mt.fabs(c2-c1)==2):
        
    
        if Efst[n]==Rfst[n]==True:
            if n==1 and m[1]==[8,3]:
                Rm=[[8,1],[8,4]]
            elif n==1 and m[1]==[8,7]:
                Rm=[[8,8],[8,6]]
            elif n==2 and m[1]==[1,3]:
                Rm=[[1,1],[1,4]]
            else:
                Rm=[[1,8],[1,6]]
            
            if (not obs(m,b)) and (not obs(Rm,b)):                
                if (not check(m[0],m[0],b)[n]):
                    T=move([m[0],Rm[1]],b.copy())
                    if check(Rm[1],Rm[1],T)[n]:
                        return {"V":False,"B":b}
                    else:
                        
                        b=move(m,b)
                        
                        b=move(Rm,b)
                        return {"V":True,"B":b}
                else:
                    return {"V":False,"B":b}
            else:
                return {"V":False,"B":b}
        else:
            return {"V":False,"B":b}
                
    else:
        return {"V":False,"B":b}
        
        
        
        
    
    
def pawnpro(m,n,b):
    [[r1,c1],[r2,c2]]=m
    if (n==1 and r2==1 or n==2 and r2==8) and 'P' in str(b.at[r1,c1]):
        print("Player",n," is eligible for pawn promotion.")
        while True:
            P=input("Enter the peice of your choice: ")
            if P in ['R','K','B','Q','P']:
                b.at[r1,c1]=P+str(n)
                break
            else:
                print("This peice is not allowed! Try again!")
    return b


def en(m,n,b):
    t=(-1)**(n)
    [[r1,c1],[r2,c2]]=m
    if (r1 in [7,2]) and ('P' in b.at[r1,r2]):
        if r2-r1==t*2:
            k1=[[r2,c1+1],[(r1+r2)/2,c1]]
            k2=[[r2,c1-1],[(r1+r2)/2,c1]]
            return {'posA':[k1,k2],'posD':m[1]}


def checkmate(Ep1,Ep2,b):
    bt=b.copy()
    D={1:True,2:True}
    for r in b.axes[0]:
        for c in b.axes[1]:
            m1=[Ep1,[r,c]]
            if legal(m1,1,bt):
                move(m1,bt)
                if check([r,c],Ep2,bt)[1]:
                    bt=b.copy()
                else:
                    D[1]=False
            m2=[Ep2,[r,c]]
            if legal(m2,2,bt):
                move(m2,bt)
                if check(Ep1,[r,c],bt)[2]:
                    bt=b.copy()
                else:
                    D[2]=False
    return D
    
        
    
    
    

        
        
       
    
    

   
 
        
    
            
            
            
    
                
        
     
    
    
    
    
    
    
                
                       
                       
               
            
        
           
           
           
           
           
       
       

       
    
    
