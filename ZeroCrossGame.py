#ZERO CROSS GAME
#DEVELOP BY=MANINDER SINGH(GAME DEVELOPER)

import pygame

pygame.init()

#COLOURS
white=(255,255,255)
black=(0,0,0)
display_color=(46,53,105)
line_color=(80,181,4)


display_width=550
display_height=550
game_window=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock()

#LOAD IMAGES
#1.CROSS IMAGE
cross=pygame.image.load('tank/cross.png')
zero=pygame.image.load('tank/zero.png')
#FUNCTIONS
def rect(x,y,width,height):
    pygame.draw.rect(game_window,line_color,[x,y,width,height])

#specific variables
position_zero=[(80,45),(237,45),(390,45),(80,200),(237,200),
                (390,200),(80,355),(237,355),(390,355)]
position_cross=[(60,45),(215,45),(370,45),(60,200),(215,200),
                 (370,200),(60,355),(215,355),(370,355)]
check_position=[0,0,0,0,0,0,0,0,0]
won_position=[0,0,0,0,0,0,0,0,0]
turn=[]
blit_images=[]
xo=[[0,1,2],[0,3,6],[0,4,8],[6,7,8],[2,5,8],[2,4,6],[3,4,5],[1,4,7]]
game=True
while game:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()
    game_window.fill(display_color)
    rect(180,50,8,450)#prependicular lines
    rect(350,50,8,450)
    rect(50,175,450,8)#horizontal lines
    rect(50,330,450,8)
    mouse_position=pygame.mouse.get_pos()
    mouse_touch=pygame.mouse.get_pressed()
    if list(mouse_touch)[0]==1:
        if list(mouse_position)[0]>50 and list(mouse_position)[0]<180 and list(mouse_position)[1]>50 and list(mouse_position)[1]<175 and check_position[0]==0:
            check_position[0]=1
            blit_images.append(0)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[0]='zero'
                    
                else:
                    turn.append('cross')
                    won_position[0]='cross'
            else:
                turn.append('cross')
                won_position[0]='cross'
        if list(mouse_position)[0]>180 and list(mouse_position)[0]<350 and list(mouse_position)[1]>50 and list(mouse_position)[1]<175 and check_position[1]==0:
            check_position[1]=1
            blit_images.append(1)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[1]='zero'
                else:
                    turn.append('cross')
                    won_position[1]='cross'
            else:
                turn.append('cross')
                won_position[1]='cross'
        if list(mouse_position)[0]>350 and list(mouse_position)[0]<450 and list(mouse_position)[1]>50 and list(mouse_position)[1]<175 and check_position[2]==0:
            check_position[2]=1
            blit_images.append(2)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[2]='zero'
                else:
                    turn.append('cross')
                    won_position[2]='cross'
            else:
                turn.append('cross')
                won_position[2]='cross'
        if list(mouse_position)[0]>50 and list(mouse_position)[0]<180 and list(mouse_position)[1]>175 and list(mouse_position)[1]<330 and check_position[3]==0:
            check_position[3]=1
            blit_images.append(3)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[3]='zero'
                else:
                    turn.append('cross')
                    won_position[3]='cross'
            else:
                turn.append('cross')
                won_position[3]='zero'
        if list(mouse_position)[0]>180 and list(mouse_position)[0]<350 and list(mouse_position)[1]>175 and list(mouse_position)[1]<330 and check_position[4]==0:
            check_position[4]=1
            blit_images.append(4)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[4]='zero'
                else:
                    turn.append('cross')
                    won_position[4]='cross'
            else:
                turn.append('cross')
                won_position[4]='cross'
        if list(mouse_position)[0]>350 and list(mouse_position)[0]<450 and list(mouse_position)[1]>175 and list(mouse_position)[1]<330 and check_position[5]==0:
            check_position[5]=1
            blit_images.append(5)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[5]='zero'
                else:
                    turn.append('cross')
                    won_position[5]='cross'
            else:
                turn.append('cross')
                won_position[5]='cross'
        if list(mouse_position)[0]>50 and list(mouse_position)[0]<180 and list(mouse_position)[1]>330 and list(mouse_position)[1]<450 and check_position[6]==0:
            check_position[6]=1
            blit_images.append(6)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[6]='zero'
                else:
                    turn.append('cross')
                    won_position[6]='cross'
            else:
                turn.append('cross')
                won_position[6]='cross'
        if list(mouse_position)[0]>180 and list(mouse_position)[0]<350 and list(mouse_position)[1]>330 and list(mouse_position)[1]<450 and check_position[7]==0:
            check_position[7]=1
            blit_images.append(7)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[7]='zero'
                else:
                    turn.append('cross')
                    won_position[7]='cross'
            else:
                turn.append('cross')
                won_position[7]='cross'
        if list(mouse_position)[0]>350 and list(mouse_position)[0]<450 and list(mouse_position)[1]>330 and list(mouse_position)[1]<450 and check_position[8]==0:
            check_position[8]=1
            blit_images.append(8)
            if len(turn)!=0:
                if turn[-1]=='cross':
                    turn.append('zero')
                    won_position[8]='zero'
                else:
                    turn.append('cross')
                    won_position[8]='cross'
            else:
                turn.append('cross')
                won_position[8]='cross'
    check=0
    for i in blit_images:
        if turn[check]=='cross':
            game_window.blit(cross,position_cross[i])
        else:
            game_window.blit(zero,position_zero[i])
        check+=1
    for i in xo:
        if won_position[i[0]]=='cross' and won_position[i[1]]=='cross' and won_position[i[2]]=='cross':
            print('Cross won')
            game=False
        if won_position[i[0]]=='zero' and won_position[i[1]]=='zero' and won_position[i[2]]=='zero':
             print('zero won')
             game=False
        else:
            if len(turn)==9:
                print('game is draw')
                check_position=[0,0,0,0,0,0,0,0,0]
                won_position=[0,0,0,0,0,0,0,0,0]
                turn=[]
                blit_images=[]
    pygame.display.update()
    clock.tick(8)

    

