import pgzrun

box=Rect((50,50),(150,100))
box2=Rect((600,50),(100,100))
#box3=Rect((300,50),(100,100))
bvx =2
b2vx=-2

def draw():
    screen.fill('blue')
    screen.draw.filled_rect(box,'yellow')
    screen.draw.filled_rect(box2,'red')
   # screen.draw.filled_rect(box3,'green')
def update():
    global bvx,b2vx
    box.x += bvx
    box2.x +=-b2vx
    if box.colliderect(box2):
        bvx=-bvx
        b2vx=b2vx
        sounds.cling.play()
    if box.left <0:
        bvx=-bvx
        sounds.cling.play()
    if box2.right>800:
        b2vx=-b2vx 
        sounds.cling.play()    
    #box.x +=2
    #box2.x +=-2
    #box3.y +=2
    #box2.y  +=-2
pgzrun.go()