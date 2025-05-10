x=1 
def setup():
    size(800,800)
def draw():
    global x
    background(255)
    fill(0)
    ellipse(250,200,150,150)
    textSize(20)
    fill(0)
    text(x,400,100)
    fill(200)
    text(u"нажми меня",200,200)
    if x>=1000:
        x=1
def mouseClicked():
    global x
    xDif = 250 - mouseX
    yDif = 200 - mouseY
    
    if sqrt(xDif*xDif + yDif*yDif) < 75:
        x=x+1
  
