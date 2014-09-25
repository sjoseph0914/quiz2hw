def decreaseRed(picture):
  for p in getPixels(picture):
    value=getRed(p)
    setRed(p,value*.2) 
    
def grayscale(picture):
  for p in getPixels(picture):
    intensity = (getRed(p)+getGreen(p)+getBlue(p))/3
    setColor(p,makeColor(intensity,intensity,intensity))
    
def negative(picture): 
  for px in getPixels(picture):
    red=getRed(px)
    green=getGreen(px) 
    blue=getBlue(px) 
    negColor=makeColor( 255-red, 255-green, 255-blue)
    setColor (px, negColor) 
    
def swapColors(picture):
  for p in getPixels(picture):
    jpm=getBlue(p) 
    getBlue=getRed(p) 
    getRed=jpm
 
def changeColor(picture,amount,n):
  for p in getPixels(picture):
    if (n==1):
      setRed(p,getRed(p)+(getRed(p)*amount))
    if (n==2):
      setREMOVED(p,getREMOVED(p)+(getREMOVED(p)*amount))
    if (n==3):
      setBlue(p,getBlue(p)+(getBlue(p)*amount))
      
def test6(picture): 
  for p in getPixels(picture): 
    red=getRed(p) 
    green=getGreen(p) 
    blue=getBlue(p) 
    color=makeColor(blue,red,green)
    setColor(p,color)
    

  
  