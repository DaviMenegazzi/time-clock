import random

angle = 0

def back(rx, ry, rad):
    
    noFill()
    strokeWeight(2)
    stroke(255) #100
    line(rx, ry, rx + random.randint(0, 4), ry)
                    

def setup():
    size(1000, 500)
    
def draw():
    global angle
    frameRate(30)
    background(0)
    
    rx = random.randint(0, 1000)
    ry = random.randint(0, 500)
    rad = random.randint(1, 10)

    back(rx, ry, rad) #Executa o fundo
    
    fill(255)
    translate(width / 2, height / 2)
    
    rad_planet = 60
    
    planet = Planet(rad_planet, 0, 0)
    planet.dance()
    planet.create()
    
    #fill(255, 241, 48) #Azul
    #fill(56, 139, 255) #Amarelo
    n = 5
    
    for i in range(n):
        rotate(cos(angle) * angle)
        ellipse((rad_planet / 2) + (i * 50 + 20), rad_planet / 2, 20, 20) #Satélite
        line((rad_planet / 2) + (i * 50 + 20), rad_planet / 2, 10, 10)

    
    angle = angle + 0.02
    
    
class Planet:
    def __init__(self, rad, posx, posy):
        self.rad = rad
        self.posx = posx
        self.posy = posy
        
    def create(self):
        fill(255)
        ellipse(self.posx, self.posy, self.rad, self.rad) #Planeta
        
    def dance(self):
        self.posx = self.posx + random.randint(-5, 5)
        self.posy = self.posy + random.randint(-5, 5)
