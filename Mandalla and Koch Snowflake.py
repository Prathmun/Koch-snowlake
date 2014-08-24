import turtle

def draw_square(some_turtle):
    for i in range(1,5):
        some_turtle.forward(100)
        some_turtle.right(90)

def draw_circle(circle_turtle):
    circle_turtle.circle(25)

def draw_triangle(some_turtle,size):
    for i in range(1,4):              
        some_turtle.forward(size)
        some_turtle.right(120)

def draw_lefttriangle(some_turtle, size):
    for i in range(1,4):
        some_turtle.forward(size)
        some_turtle.left(120)

def draw_kochsnowflake():
    window = turtle.Screen()
    window.bgcolor("blue")

    stylus = turtle.Turtle()
    stylus.shape("turtle")
    stylus.color("red")
    stylus.speed(1)

    def kochsprouter(size,zoom):
        for i in range(1,4):
            stylus.speed(10000)
            stylus.color("green")
            stylus.forward(size/zoom)
            stylus.color("black")
            draw_lefttriangle(stylus,( size/zoom))
            stylus.color("red")
            stylus.forward(size/zoom)
            stylus.forward(size/zoom)
            stylus.right(120)
            stylus.speed(1)
            #Okay, so we want it do do the whole process over again, but introduce
            #new layers. it may be possible to have it do the deeper sprouts
            #on the first pass rather than having it draw itself all over again.
            
    def initiator(stylus,size,zoom):
        print(size*2/(zoom/3))
        stylus.forward(size*2/(zoom/3))
        stylus.right(180)
    def cornertaker(stylus,size,zoom):
        stylus.right(180)
        stylus.forward(size*1/(zoom/3))
        stylus.right(120)
        
    size = 270
    zoom = 3
    depth = 10
    
    for i in range(1,depth): #accepts the paremeter of how many times to iterate on the snowflake
        
        if zoom == 3:
            kochsprouter(size,zoom)
        if zoom == 9:
            for i in range (1,4):
                initiator(stylus,size,zoom)
                kochsprouter(size,zoom)
                cornertaker(stylus,size,zoom)
        if zoom == 27:
            for i in range (1,4):
                initiator(stylus,size,9)
                kochsprouter(size,zoom)
                cornertaker(stylus,size,zoom)
            
                
        zoom = zoom*3
          
        
            
    
    window.exitonclick()
    
def draw_mandala():
    #create the indow this all sits in.
    window = turtle.Screen()
    window.bgcolor("green")
    #Create brad, get bard to draw a square
    brad = turtle.Turtle()
    brad.shape("turtle")
    brad.color("blue")
    brad.speed(600)
    for i in range (1,361):
        draw_square(brad)
        brad.right(1)

    #sides = 0 #original square drawing code
    #while sides < 4:
     #  brad.forward(100)
      #  brad.right(90)
       # sides = sides + 1
    
    angie = turtle.Turtle()
    angie.shape("circle")
    angie.color("red")
    angie.speed(30)

    for i in range(1,(360/5)):
        draw_circle(angie)
        angie.left(5)

    

    freddy = turtle.Turtle()
    freddy.shape("triangle")
    freddy.color("purple")
    freddy.speed(5)

    for i in range(1, 360/20):
        draw_triangle(freddy,160)
        freddy.right(20)
    
    
    
    window.exitonclick()


#draw_mandala()

draw_kochsnowflake()
