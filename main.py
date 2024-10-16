### LIBRARY ####

from tkinter import *
from math import *


#### VARIABLES ####

## Constants ##

x_max = 800
y_max = 715

x_origin = x_max/2
y_origin = y_max/4

radius = 10

l = 3*y_max/4 - y_origin - radius

dt = 0.01 # seconds ; dt = 0.01 seconds = 10^(-2) seconds = 10 miliseconds
g = 9.81  # acceleration constant

fen = Tk()


## Mutables ##

reset = False
first = True

x = x_max/2
y = 3*y_max/4

theta_0 = 45  # degrees
theta = theta_0 * pi/180  # t
derivate_theta = 0
m = 2  # kilogram
alpha = 10  # Friction coefficient due to friction force f = -alpha*V where V is speed


## Graphics ##

entry_theta_0 = Entry(fen, width = 50)
entry_alpha = Entry(fen, width = 50)
entry_mass = Entry(fen, width = 50)
entry_g = Entry(fen, width = 50)

get = Button(fen, width = 20, text = "START")

canvas = Canvas(fen, width = 800, height = 600, bg = "black")

ball = canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill = "red")
stem = canvas.create_line(x_origin, y_origin, x, y, fill = "red")


#### FUNCTION ####

def reset_value():
    global x, y, derivate_theta, theta, reset, first

    if not(first):
        reset = True
    else:
        first = False

    theta = theta_0 * pi/180 
    derivate_theta = 0

    x = l*sin(theta) + x_origin
    y = l*cos(theta) + y_origin

    canvas.coords(ball, x - radius, y - radius, x + radius, y + radius)
    canvas.coords(stem, x_origin, y_origin, x, y)
    

def loop():
    global derivate_theta, theta, reset

    # theta = 0(t)
    # derivate_theta= 0_point(t)

    temp = derivate_theta

    derivate_theta -= (dt/(m*l))*(2*alpha*derivate_theta/cos(theta) + m*g* sin(theta))  # 0_point(t+dt)

    theta = dt*temp + theta  # 0(t+dt)

    x = l*sin(theta) + x_origin
    y = l*cos(theta) + y_origin

    canvas.coords(ball, x - radius, y - radius, x + radius, y + radius)
    canvas.coords(stem, x_origin, y_origin, x, y)

    if not(reset) :
        fen.after(int(100*dt), loop)
    else:
        reset = False


def start_loop():
    global theta_0, alpha, m, g

    test = True  # No problem with given number in entries
    try :
        theta_0 = int(entry_theta_0.get())
    except ValueError:
        entry_theta_0.config(textvariable="")
        entry_theta_0.insert(0, "NOT A NUMBER, please enter a number for the initial angle")
        test = False

    try :
        alpha = int(entry_alpha.get())
    except ValueError:
        entry_alpha.config(textvariable="")
        entry_alpha.insert(0, "NOT A NUMBER, please enter a number for the friction coefficient")
        test = False

    try :
        m = int(entry_mass.get())
    except ValueError:
        entry_mass.config(textvariable="")
        entry_mass.insert(0, "NOT A NUMBER, please enter a number for the mass")
        test = False

    try :
        g = float(entry_g.get())
    except ValueError:
        entry_g.config(textvariable="")
        entry_g.insert(0, "NOT A NUMBER, please enter a number for g")
        test = False
    
    if test :
        reset_value()
        loop()




#### PRINT ####

height = str(x_max) + "x" + str(y_max)
fen.geometry(height)

entry_theta_0.insert(0, str(theta_0))
entry_theta_0.pack()

entry_alpha.insert(0, str(alpha))
entry_alpha.pack()

entry_mass.insert(0, str(m))
entry_mass.pack()

entry_g.insert(0, str(g))
entry_g.pack()

get.config(command = start_loop)
get.pack()

canvas.pack()

fen.mainloop()