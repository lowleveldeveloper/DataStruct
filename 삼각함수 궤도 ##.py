import turtle as t
from math import sin,cos  #터틀모듈과 math모듈을 불러온다.

earth=t.Turtle()          #지구와 화성개체를 생성하고 궤도를 지정한다.
earthorbit=50
mars=t.Turtle()
marsorbit=150

earth.shape("circle")
earth.color("blue")
mars.shape("circle")
mars.color("red")



short=earthorbit*cos(10)
short2=earthorbit*sin(10)

def setting():            #시작위치 지정을 정의한다.
    earth.pu()
    earth.goto(short,short2)
    earth.pd()
    mars.pu()
    mars.goto(marsorbit*cos(10),marsorbit*sin(10))
    mars.pd()
   

def revolve():                       
    x=10                  #시작위치 10씩을 변수에 저장한다.               
    y=10
    while True:           #변수의 변화를 다르게 부여해 상대적인 속도를 맞춘다
        earth.goto(earthorbit*cos(x),earthorbit*sin(x))
        mars.goto(marsorbit*cos(y),marsorbit*sin(y))
        x+=0.3
        y+=0.2


    
        

t.bgcolor("black")        #배경을 어둡게 한다.
       

setting()
revolve()
