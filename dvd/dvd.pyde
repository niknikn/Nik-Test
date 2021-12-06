x = 0
y = 300
x2 = 300
y2 = 0

speed_x = 2
speed_y = 2
speed_x_2 = 2
speed_y_2 = 2

dvd = None
dvd2 = None

def setup():
    global dvd, dvd2
    size(800,600)
    dvd = loadImage('dvd-logo.png')
    dvd2 = loadImage('dvd-logo.png')

def draw():
    global x,y, x2, y2, speed_x, speed_y, speed_y_2, speed_x_2, dvd, dvd2
    background('#000000')
    image(dvd, x, y)
    image(dvd2, x2, y2)
    x += speed_x
    y += speed_y
    x2 += speed_x_2
    y2 += speed_y_2
    
    
    if x2 > x and x2 < (x + 100) and y >= y2 and y <= (y2 +45):
        speed_x *= -1
        speed_x_2 *= -1
        
    if x > x2 and x < (x2 + 100) and y >= y2 and y <= (y2 +45):
        speed_x *= -1
        speed_x_2 *= -1
    
    if (x2 > 700 or x2 < 0):
        speed_x_2 *= -1
    elif (y2 > 555 or y2 < 0):
        speed_y_2 *= -1
        
    if (x > 700 or x < 0):
        speed_x *= -1
    elif (y > 555 or y < 0):
        speed_y *= -1
    
       
    
