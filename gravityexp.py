import pygame,math,random
pygame.init()
G=0.00001
height=600
width=800
disp= pygame.display.set_mode((width,height))
pygame.display.update()
pygame.display.set_caption("Let's predict the Universe")
clock = pygame.time.Clock()
state = True

pygame.draw.circle(disp,(255,0,255),(400,300),5,0)

disp.fill((0,0,0))
#pygame.draw.circle(disp,(255,255,255),[400,300],10,0)
pygame.display.update()
planets=list()
class planet():
    def __init__(self,x,y,mass,radius):
        self.x=x
        self.y=y
        self.m=mass
        self.r=radius
        self.dx=0
        self.dy=0
    def draw(self):
        self.x+=self.dx
        self.y+=self.dy
        self.color=(255,255,255)
        pygame.draw.circle(disp,self.color,(self.x+self.dx,height-self.y+self.dy),self.r,0)


# p1=planet(300,200,5000,10)
# p1.dx=-0.01
# p2=planet(200,300,5000,10)
# p2.dx=0.01
# 
# planets.append(p1)
# planets.append(p2)

for i in range(10):
    p=planet(random.randint(50,750),random.randint(50,550),5000,10)
    planets.append(p)
def ds(p,q):
    distance_squared= (p.x-q.x)**2+(p.y-q.y)**2
    return distance_squared
def force(p,q):
    distance=ds(p,q)
    force=-p.m*q.m*G/distance
    return force
def acc(p,q):
    f=force(p,q)
    acc=f/p.m
    #print(acc)
    return acc
def angle(p,q):
    if p.x==q.x and p.y>q.y:
        angle=math.pi/2
    elif p.x==q.x and p.y<q.y:
        angle=math.pi*3/2
    else:
        angle=math.atan((p.y-q.y)/(p.x-q.x))
    #print(angle)
    return angle
def comp(p,q):#this diviede acc into x and y comp
    a=acc(p,q)
    if p.x<q.x:
        p.dx-=a*math.cos(angle(p,q))
        p.dy-=a*math.sin(angle(p,q))
    else:
        p.dx+=a*math.cos(angle(p,q))
        p.dy+=a*math.sin(angle(p,q))
while state:
    disp.fill((0,0,0))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            state = False
    for rp in planets:
        for p in planets:
            if rp != p:
                comp(rp,p)
        rp.draw()
    pygame.display.update()
    #clock.tick(120)
pygame.quit()