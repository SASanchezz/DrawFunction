from graphics import *
import numpy as np
from PIL import EpsImagePlugin, Image
import math
from Buttons import *

class Drawing(object):

    WINDOW_HEIGHT = 800
    WINDOW_WIDTH = 1200
    Input_Plot = GraphWin('Input', 600, 400)


    a = 1



    @staticmethod
    def main():
        global HEIGHT
        global WIDTH
        global a
        global WINDOW_WIDTH
        global WINDOW_HEIGHT
        global Plot
        global ACCURACY

        WINDOW_WIDTH = 1200
        WINDOW_HEIGHT = 800
        #WINDOW_WIDTH = Drawing.Input(Drawing.Input_Plot.getWidth(), Drawing.Input_Plot.getHeight(), 'Input width of window: ', 'green', 'orange', 'Next', Drawing.Input_Plot)
        #WINDOW_HEIGHT = Drawing.Input(Drawing.Input_Plot.getWidth(), Drawing.Input_Plot.getHeight(), 'Input height of window: ', 'green', 'orange', 'Next', Drawing.Input_Plot)

        a = Drawing.Input(Drawing.Input_Plot.getWidth(), Drawing.Input_Plot.getHeight(), Drawing.Input_Plot.getHeight(), 'Input parameter a: ', 'red', Drawing.Input_Plot)
        Drawing.Button(Drawing.Input_Plot.getWidth() / 2, Drawing.Input_Plot.getHeight() / 2, 'Next', 'orange', 25, Drawing.Input_Plot, 0, 0, 'next')
        if Drawing.click('next', Drawing.Input_Plot):
            a[1].undraw()
            a = float (a[0].getText())
        ACCURACY = Drawing.Input(Drawing.Input_Plot.getWidth(), Drawing.Input_Plot.getHeight(), Drawing.Input_Plot.getHeight(), 'Input parameter Step: ', 'red', Drawing.Input_Plot)
        Drawing.Button(Drawing.Input_Plot.getWidth() / 2, Drawing.Input_Plot.getHeight() / 2, 'To plot', 'orange', 25, Drawing.Input_Plot, 0, 0, 'to_plot')
        if Drawing.click('to_plot', Drawing.Input_Plot):
            ACCURACY[1].undraw()
            ACCURACY = float(ACCURACY[0].getText())



        HEIGHT = math.ceil(Drawing.function(a, a * 0.95))
        WIDTH = a / 10 * 12
        Drawing.Input_Plot.close()
        Plot = GraphWin('Plot', WINDOW_WIDTH, WINDOW_HEIGHT) # Set window size\ create plot

        Drawing.create_axes(a)
        Drawing.draw_function(a)
        Drawing.function_info(a, Plot)

        print('a/10:',a/10,' y coord:', -math.ceil(Drawing.function(a, a*0.95)) /20, ' a/3',a/3)

        a_change = Drawing.Input(a / 3, -math.ceil(Drawing.function(a, a * 0.95))*3*4/5, -math.ceil(Drawing.function(a, a * 0.95))*5*13/20 , 'Change a: ', 'grey', Plot)

        Drawing.Button(a / 3, -math.ceil(Drawing.function(a, a * 0.95)) / 5*3, 'Exit', 'orange', 16, Plot, a/10, math.ceil(Drawing.function(a, a*0.95)) / 15, 'exit')

        Drawing.Button(a / 10, -math.ceil(Drawing.function(a, a * 0.95)) / 5*3, 'Change', 'orange', 16, Plot, a / 10, math.ceil(Drawing.function(a, a * 0.95)) / 15, 'change')


        if (Drawing.click('exit', Plot)):
            Plot.close()


    @staticmethod
    def create_axes(a):
        Plot.setBackground("white")

        Plot.setCoords(-(a/10*3), -(math.ceil(Drawing.function(a, a*0.95)) * 6 / 5),
                       a/10*14, math.ceil(Drawing.function(a, a*0.95)) * 6 / 5)  # Set normal coordinates for plot

        X_Axis = Line(Point(0, 0), Point(a/10*12, 0))  # Draw the X Axis for plot
        X_Axis.setWidth(3.5)  # Set width for X Axis
        Y_Axis = Line(Point(0, -(math.ceil(Drawing.function(a, a*0.95)))), Point(0, math.ceil(Drawing.function(a, a*0.95))))  # Draw the Y Axis for plot
        Y_Axis.setWidth(3.5)  # Set width for Y Axis
        X_Axis.draw(Plot)
        Y_Axis.draw(Plot)

        Drawing.x_axis_mark_creation(a)
        Drawing.y_axis_mark_creation(a)


    @staticmethod
    def x_axis_mark_creation(a):
        for x_mark in np.arange(0, WIDTH+0.1, WIDTH / 12):
            # Lines
            X_Mark = Line(Point(x_mark, 0), Point(x_mark, -HEIGHT / 35))
            X_Mark.setWidth(3)
            X_Mark.draw(Plot)
            # Values
            Output_text = Text(Point(x_mark, -HEIGHT / 20), round(x_mark, 3))
            Output_text.setSize(9)
            Output_text.draw(Plot)


    @staticmethod
    def y_axis_mark_creation(a):
        maximalValue = math.ceil(Drawing.function(a, a*0.95))
        auxiliary = maximalValue
        print (a, ' : ', maximalValue)

        for y_mark in np.arange(0, HEIGHT+0.01, HEIGHT / 5):
            auxiliary = round(auxiliary-maximalValue/5, 3)

            # Lines
            Y_Mark = Line(Point(0, y_mark), Point(-a / 70, y_mark))
            Y_Mark.setWidth(3)
            Y_Mark.draw(Plot)
            #Negative part
            Y_Mark = Line(Point(0, -y_mark), Point(-a / 70, -y_mark))
            Y_Mark.setWidth(3)
            Y_Mark.draw(Plot)

            # Values
            Output_text = Text(Point(-a / 15, y_mark), round(y_mark, 3))
            Output_text.setSize(9)
            Output_text.draw(Plot)
            # Negative part
            if (y_mark != 0):
                Output_text = Text(Point(-a / 15, -y_mark), -round(y_mark, 3))
                Output_text.setSize(9)
                Output_text.draw(Plot)


    @staticmethod
    def draw_function(a):
        Width_Multiplier = WIDTH*10/12/a
        Height_Multiplier = HEIGHT/math.ceil(Drawing.function(a, a*0.95))
        for i in np.arange(0, a, ACCURACY):
            Section = Line(Point(i*Width_Multiplier, Drawing.function(a, i)*Height_Multiplier),
                           Point((i+ACCURACY)*Width_Multiplier, Drawing.function(a, i+ACCURACY)*Height_Multiplier))
            Section.setFill('blue')
            Section.setWidth(1.5)
            Section.draw(Plot)

            Negative_Section = Line(Point(i * Width_Multiplier, - Drawing.function(a, i) * Height_Multiplier),
                           Point((i + ACCURACY) * Width_Multiplier, - Drawing.function(a, i + ACCURACY) * Height_Multiplier))
            Negative_Section.setFill('red')
            Negative_Section.setWidth(1.5)
            Negative_Section.draw(Plot)


    @staticmethod
    def Input(width, height, text_height, label, color, Plot):

        global a

        a_input = Text(Point(width / 2, text_height / 5), label)
        a_input.setSize(20)
        a_input.draw(Plot)

        input_text = Entry(Point(width / 2, height / 3), 5)
        input_text.setFill(color)
        input_text.setSize(30)
        input_text.draw(Plot)

        return [input_text, a_input]


    @staticmethod
    def Button(central_x, central_y, label, color, font_size, Plot, size_x, size_y, key):
        if (size_x==0 or size_y==0):
            DEFAULT_WIDTH = 110
            DEFAULT_HEIGHT = 50
            return Drawing.rectangle_button(central_x, central_y, color, font_size, DEFAULT_WIDTH, DEFAULT_HEIGHT, Plot, label, key)
        else:
            return Drawing.rectangle_button(central_x, central_y, color, font_size, size_x, size_y, Plot, label, key)


    @staticmethod
    def button_text(central_x, central_y, label, font_size, Plot):
        a_input = Text(Point(central_x, central_y*5/3), label)
        a_input.setSize(font_size)
        a_input.draw(Plot)



    @staticmethod
    def rectangle_button(central_x, central_y, color, font_size, DEFAULT_WIDTH, DEFAULT_HEIGHT, Plot, label, key):
        Buttons[key] = [central_x-DEFAULT_WIDTH/2, central_y*5/3 - DEFAULT_HEIGHT/2, central_x+DEFAULT_WIDTH/2, central_y*5/3 + DEFAULT_HEIGHT/2]

        print('making rectangle')
        print(DEFAULT_WIDTH, DEFAULT_HEIGHT)
        print('with parameters:', 'x1:',central_x-DEFAULT_WIDTH/2, ' y1:',central_y*5/3 - DEFAULT_HEIGHT/2, ' x2:',central_x+DEFAULT_WIDTH/2, ' y2:',central_y*5/3 + DEFAULT_HEIGHT/2)


        button = Rectangle(Point(central_x-DEFAULT_WIDTH/2, central_y*5/3 - DEFAULT_HEIGHT/2),
                            Point(central_x+DEFAULT_WIDTH/2, central_y*5/3 + DEFAULT_HEIGHT/2))
        button.setFill(color)
        button.draw(Plot)

        Drawing.button_text(central_x, central_y, label, font_size, Plot)

        #return Drawing.click(key, Plot)


    @staticmethod
    def click(element, Plot):
        coordinates = Buttons[element]

        X_start = coordinates[0]
        X_end = coordinates[2]
        Y_start = coordinates[1]
        Y_end = coordinates[3]

        while(True):
            click = Plot.getMouse()
            print('click')
            click_X = click.getX()
            click_Y = click.getY()

            if (click_X > X_start and click_X < X_end and  click_Y > Y_start and click_Y < Y_end):

                return True

    @staticmethod
    def function_info(a, Plot):
        first_height = math.ceil(Drawing.function(a, a*0.95))
        second_height = math.ceil(Drawing.function(a, a * 0.95)) - math.ceil(Drawing.function(a, a * 0.95)) / 10

        Blue_line = Line(Point(a/10, first_height), Point(a * 3/20, first_height))
        Blue_line.setWidth(2)
        Blue_line.setFill('blue')
        Blue_line.draw(Plot)

        Red_line = Line(Point(a / 10,second_height ), Point(a * 3/20, second_height))
        Red_line.setWidth(2)
        Red_line.setFill('red')
        Red_line.draw(Plot)

        Blue_text = Text(Point(a / 4, first_height), '+ Цисоїда Діоклеса')
        Blue_text.setSize(10)
        Blue_text.draw(Plot)

        Red_text = Text(Point(a / 4, second_height), '- Цисоїда Діоклеса')
        Red_text.setSize(10)
        Red_text.draw(Plot)

    @staticmethod
    def function(a, x):
        if (a==x):
            x*=0.999
        print("a:", a, " x:", x, " y:", math.sqrt(pow(x, 3) / round(a - x, 10)))
        Value = math.sqrt(pow(x, 3) / round(a - x, 10))
        return Value

Drawing.main()


# Saving plot
"""Plot.postscript(file="image.eps", colormode='color')
EpsImagePlugin.gs_windows_binary = r'gs\gs9.54.0\bin\gswin64c'
# Convert from eps format to gif format using PIL

img = Image.open("image.eps")
img.save("Plot.gif", "gif")"""