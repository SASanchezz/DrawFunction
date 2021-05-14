from graphics import *
import numpy as np
from PIL import EpsImagePlugin, Image
import math

ACCURACY = 0.01
WINDOW_HEIGHT = 800
WINDOW_WIDTH = 1200
Input_Plot = GraphWin('Input', 600, 400)


HEIGHT = WINDOW_HEIGHT * 0.44
WIDTH = WINDOW_WIDTH / 3
a = 1

def main():
    global a
    global WINDOW_WIDTH
    global WINDOW_HEIGHT
    global Plot

    a = Input(Input_Plot.getWidth(), Input_Plot.getHeight(), 'Input parameter a: ', 'red')
    WINDOW_WIDTH = Input(Input_Plot.getWidth(), Input_Plot.getHeight(), 'Input width of window: ', 'green')
    WINDOW_HEIGHT = Input(Input_Plot.getWidth(), Input_Plot.getHeight(), 'Input height of window: ', 'green')

    Input_Plot.close()
    Plot = GraphWin('Plot', WINDOW_WIDTH, WINDOW_HEIGHT) # Set window size\ create plot

    create_coordinates(a)
    draw_function(a)


    Plot.getMouse()
    Plot.close()


def create_coordinates(a):

    Plot.setBackground("white")

    Plot.setCoords(-100, -HEIGHT-50, WIDTH+50, HEIGHT+50)  # Set normal coordinates for plot

    X_Axis = Line(Point(0, 0), Point(WIDTH, 0))  # Draw the X Axis for plot
    X_Axis.setWidth(3.5)  # Set width for X Axis
    Y_Axis = Line(Point(0, -HEIGHT), Point(0, HEIGHT))  # Draw the Y Axis for plot
    Y_Axis.setWidth(3.5)  # Set width for Y Axis
    X_Axis.draw(Plot)
    Y_Axis.draw(Plot)

    x_axis_mark_creation(a)
    y_axis_mark_creation(a)


def x_axis_mark_creation(a):
    Gap = 0
    for x_mark in np.arange(0, WIDTH+0.1, WIDTH / 12):
        # Lines
        X_Mark = Line(Point(x_mark, 0), Point(x_mark, -10))
        X_Mark.setWidth(3)
        X_Mark.draw(Plot)
        # Values
        Output_text = Text(Point(x_mark, -15), Gap)
        Output_text.setSize(9)
        Output_text.draw(Plot)
        Gap = round((Gap + a / 10), 3)


def y_axis_mark_creation(a):
    maximalValue = math.ceil(function(a, a*0.95))
    auxiliary = maximalValue
    print (a, ' : ', maximalValue)

    for y_mark in np.arange(0, HEIGHT+0.01, HEIGHT / 5):
        Gap = round(maximalValue - auxiliary, 3)
        auxiliary = round(auxiliary-maximalValue/5, 3)

        # Lines
        Y_Mark = Line(Point(0, y_mark), Point(-5, y_mark))
        Y_Mark.setWidth(3)
        Y_Mark.draw(Plot)
        #Negative part
        Y_Mark = Line(Point(0, -y_mark), Point(-5, -y_mark))
        Y_Mark.setWidth(3)
        Y_Mark.draw(Plot)

        # Values
        Output_text = Text(Point(-15, y_mark), Gap)
        Output_text.setSize(9)
        Output_text.draw(Plot)
        # Negative part
        Output_text = Text(Point(-15, -y_mark), -Gap)
        Output_text.setSize(9)
        Output_text.draw(Plot)


def draw_function(a):
    Width_Multiplier = WIDTH*10/12/a
    Height_Multiplier = HEIGHT/math.ceil(function(a, a*0.95))
    for i in np.arange(0, a-ACCURACY, ACCURACY):
        Section = Line(Point(i*Width_Multiplier, function(a, i)*Height_Multiplier),
                       Point((i+ACCURACY)*Width_Multiplier, function(a, i+ACCURACY)*Height_Multiplier))
        Section.setFill('blue')
        Section.setWidth(1.5)
        Section.draw(Plot)

        Negative_Section = Line(Point(i * Width_Multiplier, -function(a, i) * Height_Multiplier),
                       Point((i + ACCURACY) * Width_Multiplier, -function(a, i + ACCURACY) * Height_Multiplier))
        Negative_Section.setFill('red')
        Negative_Section.setWidth(1.5)
        Negative_Section.draw(Plot)


def Input(width, height, label, color):
    global a

    a_input = Text(Point(width/2, height/5), label)
    a_input.setSize(25)
    a_input.draw(Input_Plot)

    input_text = Entry(Point(width/2, height / 3), 5)
    input_text.setFill(color)
    input_text.setSize(30)
    input_text.draw(Input_Plot)
    Button(100, 100, 'Shalom', 'red')
    Input_Plot.getMouse()
    input_text.undraw()
    a_input.undraw()
    return int(input_text.getText())

def Button(central_x, central_y, label, color):
    rectangle_button(central_x, central_y)


def rectangle_button(central_width, central_height):
    global Plot
    DEFAULT_WIDTH = 100
    DEFAULT_HEIGHT = 50
    button = Rectangle(Point(central_width-DEFAULT_WIDTH/2, central_height - DEFAULT_HEIGHT/2),
                        Point(central_width+DEFAULT_WIDTH/2, central_height + DEFAULT_HEIGHT/2))
    # print(central_height+DEFAULT_HEIGHT/2)
    # button = Rectangle(Point(central_width-DEFAULT_WIDTH/2, central_height - DEFAULT_HEIGHT/2), Point(400, 400))
    button.setFill('green')
    button.draw(Input_Plot)


def function(a, x):
    print("a:",a ," x:",x, " y:",math.sqrt(pow(x, 3) / round(a-x, 10)))
    Value = math.sqrt(pow(x, 3) / round(a-x, 10))
    return Value


main()


# Saving plot
"""Plot.postscript(file="image.eps", colormode='color')
EpsImagePlugin.gs_windows_binary = r'gs\gs9.54.0\bin\gswin64c'
# Convert from eps format to gif format using PIL

img = Image.open("image.eps")
img.save("Plot.gif", "gif")"""