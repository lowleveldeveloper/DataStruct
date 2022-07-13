from turtle import Turtle, Screen
import turtle as t
from math import sin, cos



planets = {
    'sun': {'diameter': 2.0, 'orbit': 0, 'speed': 1, 'color': 'red'},
    'mercury': {'diameter': 0.383, 'orbit': 58, 'speed': 7, 'color': 'gray'},
    'venus': {'diameter': 0.949, 'orbit': 108, 'speed': 7, 'color': 'yellow'},
    'earth': {'diameter': 1.0, 'orbit': 150, 'speed': 7, 'color': 'blue'},
    'mars': {'diameter': 0.532, 'orbit': 228, 'speed': 7, 'color': 'red'},
}

def setup_planets(planets):
    for planet in planets:
        dictionary = planets[planet]
        turtle = Turtle(shape='circle')
        turtle.speed("fastest")  # speed controlled elsewhere, disable here
        turtle.shapesize(dictionary['diameter'])
        turtle.color(dictionary['color'])
        turtle.pu()
        turtle.sety(-dictionary['orbit'])
        turtle.pd()

        dictionary['turtle'] = turtle

    screen.ontimer(revolve, 50)

def revolve():
    for planet in planets:
        dictionary = planets[planet]
        dictionary['turtle'].pu()
        dictionary['turtle'].goto(dictionary['orbit']*cos(10),dictionary['orbit']*sin(10))
        dictionary['turtle'].pd()
        for x in range(10,1000):
            dictionary['turtle'].goto(dictionary['orbit']*cos(x),dictionary['orbit']*sin(x))
    screen.ontimer(revolve, 50)

t.bgcolor("black")

screen = Screen()

setup_planets(planets)

screen.exitonclick()

