def setup():
    size(800,800)
def draw():
    line(mouseX,mouseY,pmouseX,pmouseY)
    fill(255)
    rect(100,150,150,50)
    ellipse(370,225,150,150)
    textSize(20)
    fill(0)
    text(u"фон",130,190)
    text(u"цвет",340,225)
    
def mouseClicked():
    if mouseX>100 and mouseX<250 and mouseY>150 and mouseY<200:
        background(200)
    xDif = 370 - mouseX
    yDif = 225 - mouseY
    
    if sqrt(xDif*xDif + yDif*yDif) < 75:
        stroke(random(0,255),random(0,255),random(0,255))
        
