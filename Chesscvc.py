def chess():
    import pandas as pd
    import numpy as np
    import chessfunc as cf
    import random as rd
    board=cf.board()
    print("Welcome to Chess, the game of the mind!")
    print(board)
    count=0
    en=None
    Ep1=[8,5]
    Ep2=[1,5]
    Efst={1:True,2:True}
    Rfst={1:True,2:True}
    while True:
        n=(count%2)+1
        count+=1
        t=(-1)**(n)  #directional variable
        #print("Player ",n)
        if cf.check(Ep1,Ep2,board)[n]:
            if cf.checkmate(Ep1,Ep2,board)[n]:
                print("Checkmate!!! Player",(count%2)+1,"wins!!")
                break
            print("You are under check!",n)
        m=[[rd.randint(1,8),rd.randint(1,8)],[rd.randint(1,8),rd.randint(1,8)]]
        [[r1,c1],[r2,c2]]=m
        if en!=None:
            if m in en['posA']:
               cf.move([en['posD'],m[1]],board)
        cas=cf.castle(m,n,board,Efst,Rfst)
        if cf.legal(m,n,board) or cas["V"]:
            b=cf.move(m,board.copy())
            if not cf.check(Ep1,Ep2,b)[n]:               
                board=cf.pawnpro(m,n,board) #pawn promotion
                if 'R' in str(board.at[r1,c1]):#Checking first move for castle
                    if n==1:
                        Rfst[1]=False
                    else:
                        Rfst[2]=False
                        
                if 'E' in str(board.at[r1,c1]):
                    #recording king loc for check
                    
                    if n==1:
                        Ep1=m[1]
                        Efst[1]=False
                    else:
                        Ep2=m[1]
                        Efst[2]=False
                
                if cas["V"]:
                    board=cas["B"]
                else:                     
                    en=cf.en(m,n,board)
                    board=cf.move(m,board)
                    print(board)
                    print(m)
                    #all checks over and move executed
            else:
                 count-=1
                 #print("Your move must not result in check for you! Play again!")
        else:
            count-=1
            #print("Wrong move! Play Again!")
    print(count)    
        
        
        
    
chess()
