def setup():
    size(800,800)
def draw():
    background(random(0,255),random(0,255),random(0,255))
    rect(200,200,250,200)
    if mousePressed:
       rect(mouseX,mouseY,250,200)
