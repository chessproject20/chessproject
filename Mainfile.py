def arm_movement(move,empty):
    cells=[move[i:i+2] for i in range(0, len(move), 2)]
    switcher={
                'a':0,
                'b':1,
                'c':2,
                'd':3,
                'e':4,
                'f':5,
                'g':6,
                'h':7
                }
    i1=switcher.get(cells[0][0],-1)
    i2=switcher.get(cells[1][0],-1)
    j1=int(cells[0][1])-1
    j2=int(cells[1][1])-1
    s_f1=shoulder_angle[i1][j1]
    e_f1=elbow_angle[i1][j1]
    s_f2=shoulder_angle[i2][j2]
    e_f2=elbow_angle[i2][j2]
    if empty==1:
        arm_movement_empty(s_f1,e_f1,s_f2,e_f2)
    else:
        arm_movement_capture(s_f1,e_f1,s_f2,e_f2)
    


if __name__=='__main__'
    First_Move=int(input())
    if(First_Move==1):#'Player Move'
        Pic=Camera()
        resized_image=Pic.takePicture()
        imgRecognition=board_Recognition(resized_image)
        '''Two methods with and without initaliseboard''''
        board=imgRecognition.initalize_Board()
        ''''OR METHOD CALLING
         
        img=cv2.imread(r'C:\Users\mayuresh\Desktop\ESE205-CVChess-master\capture1.jpg',1)
adth,s2=b1.clean_Image(img)
#print(s1)
ext=b1.initialize_mask(adth,s2)
edges,coloredges=b1.findEdges(img)
print(len(coloredges))
h1,v1=b1.findLines(edges,coloredges)
Corners=b1.findCorners(h1,v1,coloredges)
#b1.findCorners (h1, v1, colorEdges)
Squares=b1.findSquares(Corners, coloredges)
d1 = Board(Squares)
d1.draw(img)
d1.assignState()
img1=cv2.imread('C:\\Users\\mayuresh\\Desktop\\ESE205-CVChess-master\\capture2.jpg',1)
movechange=d1.determineChanges(img,img1)'''
        board.draw(img)
        board.assignState()
        img1=cv2.imread('C:\\Users\\mayuresh\\Desktop\\ESE205-CVChess-master\\capture3.jpg',1)
        movechange=board.determineChanges(img,img1)
        c1 = ChessEng()
        changedet=c1.updateMove(movechange)
        movefromuci=c1.feedToAI()
        arm_movement(movefromuci,1) 
        
        

    
