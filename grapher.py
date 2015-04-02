
################################################################################
###########      Grapher in Python 2.7 with Pygame library           ###########
###########      Samarth Paboowal                                    ###########
###########      Starting Date : 15 - 01 - 2015                      ###########
###########      Ending Date : 17 - 01 - 2015                        ###########
################################################################################

import pygame
import sys
from math import *

# initialisng pygame
pygame.init()

# Setting font colour
font_one = pygame.font.SysFont('Verdana', 16)
font_two = pygame.font.SysFont('Serif', 24)
font_three = pygame.font.SysFont('Arial', 14)

# Setting rgb values for colours
white = (255, 255, 255)
black = (0, 0, 0)
dark_green = (0, 100, 0)
red = (255, 0, 0)
graph_color = (200, 0, 200)
grid_color = (100, 250, 240)

# Setting width and height of screen
width, height = 600, 600
extra_width = 400

screen = pygame.display.set_mode((width + extra_width, height))
pygame.display.set_caption("Graph")

def graph_paper(k):
    
    # Clipping screen to size 500 * 500 for graph and leaving rest on the right side for
    # other stuffs
    screen.set_clip(0, 0, width, height)
    screen.fill(white)
    
    # Loop for drawing horizontal and vertical lines as in the graph paper
    for i in range(width / k):
        grid_x = k * i
        grid_y = k * i
        pygame.draw.line(screen, grid_color, (grid_x, 0), (grid_x, height), 1)
        pygame.draw.line(screen, grid_color, (0, grid_y), (width, grid_y), 1)
 
    # These are four lines that are boundaries of the graph
    # pygame.draw.line takes 5 arguments:
    # 1) graphical screen name
    # 2) color of line
    # 3) starting co-ordinates
    # 4) ending co-ordinates
    # 5) boldness of line to be drawn in pixels
    pygame.draw.line(screen, dark_green, (width, 0), (width, height), 5)
    pygame.draw.line(screen, dark_green, (0, 0), (0, height), 5)
    pygame.draw.line(screen, dark_green, (0, 0), (width, 0), 5)
    pygame.draw.line(screen, dark_green, (0, height), (width, height), 5)
    
    # These four lines are for drawing x and y axis with black color inside the graph
    mid_x = width / (2 * k)
    mid_y = height / (2 * k)
    pygame.draw.line(screen, black, (mid_x * k, 0), (mid_x * k, height), 3)
    pygame.draw.line(screen, black, (0, mid_y * k), (width, mid_y * k), 3)
    
    # Reseting the screen to its original size of width = 500 + 400 and height 500
    screen.set_clip(None)

def graph_eq(eq, k):
    
    # traversing each pixel to draw graph
    for i in range(width):
        
        try:
            # Solving equation
            x = (width / 2 - i) / float(k)
            y = eval(eq)
            pos_1 = (width / 2 + x * k, height / 2 - y * k)
            
            n_x = x = (width / 2 - (i + 1)) / float(k)
            n_y = eval(eq)
            pos_2 = (width / 2 + n_x * k, height / 2 - n_y * k)
            
            #drawing line for each point
            pygame.draw.line(screen, graph_color, pos_1, pos_2, 3)
            
        except:
            pass
            
        title = font_two.render("Your Own Grapher", 1, red)
        screen.blit(title, (width + 10, 20))
        title = font_one.render("Select 'q' to start over", 1, black)
        screen.blit(title, (width + 10, 70))
        
        # Computing and Displaying y-intercept
        x = 0
        try:
            int_y = eval(eq)
            int_y = round(int_y, 2)
        except:
            int_y = "Does Not Exist"
            
        title = font_one.render("The y-intercept is at (0.0," + str(int_y) + ")", 1, black)
        screen.blit(title, (width + 10, 100))
        
        if int_y != "Does Not Exist":
            title = font_one.render("Select 'y' to plot the intercept", 1, black)
            screen.blit(title, (width + 10, 120))
            
        title = font_one.render("Select 's' 'm' 'l' 'o' for grid size", 1, black)
        screen.blit(title, (width + 10, height - 70))
        
        title = font_one.render("Type in value, Select 'Enter' to plot", 1, black)
        screen.blit(title, (width + 10, 150))
        
        # plotting values
        x_value = []
        x_val = '?'
        y_val = '?'
            
    active = True
    while active:
        
        screen.set_clip(width + 10, 150, width + extra_width, 200)
        screen.fill(white)
        string = ""
        x_display = string.join(x_value)
        plot_x = font_one.render("x = " + str(x_display), 1, (0, 0, 200))
        screen.blit(plot_x, (width + 10, 170))
        plot_y = font_one.render("(" + str(x_val) + "," + str(y_val) + ")", 1, (0, 0, 200))
        screen.blit(plot_y, (width + 210, 170))
        screen.set_clip(None)
        
        # Updating screen each time
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                active = False
                
            elif event.type == pygame.KEYDOWN:
                
                # Commands for start over and other features
                if event.unicode == u'q':
                    main()
                elif event.unicode == u'y':
                    a = width / 2
                    b = (int)(height/2-int_y*k)
                    pygame.draw.circle(screen, black, (a, b), 4)
                # Re-size comments
                elif event.unicode == u's':
                    k = 25
                    graph_paper(k)
                    graph_eq(eq, k)
                elif event.unicode == u'm':
                    k = 20
                    graph_paper(k)
                    graph_eq(eq, k)
                elif event.unicode == u'l':
                    k = 10
                    graph_paper(k)
                    graph_eq(eq, k)
                elif event.unicode == u'o':
                    k = 5
                    graph_paper(k)
                    graph_eq(eq, k)
                
                elif event.unicode == u'\r':
                    try:
                        x = x_val = float(x_display)
                        y_val = eval(eq)
                        a = int(width / 2 + x *k)
                        b = int(height / 2 - y_val * k)
                        pygame.draw.circle(screen, black, (a, b), 4)
                        x_value = []
                    except:
                        pass
                
                # For x and y co-ordinates    
                elif event.unicode == u'1':
                    x_value.append("1")
                elif event.unicode == u'2':
                    x_value.append("2")
                elif event.unicode == u'3':
                    x_value.append("3")
                elif event.unicode == u'4':
                    x_value.append("4")
                elif event.unicode == u'5':
                    x_value.append("5")
                elif event.unicode == u'6':
                    x_value.append("6")
                elif event.unicode == u'7':
                    x_value.append("7")
                elif event.unicode == u'8':
                    x_value.append("8")
                elif event.unicode == u'9':
                    x_value.append("9")
                elif event.unicode == u'0':
                    x_value.append("0")
                elif event.unicode == u'.':
                    x_value.append(".")
                elif event.unicode == u'-':
                    x_value.append("-")

    # Quit the game            
    pygame.quit()
    sys.exit()
  
     
           
def main():
    
    screen.fill(white)
    # Always use value of k such that it is a factor of width, extra_width and height
    # otherwise there'll  be a problem with grid lines!!.
    k = 25
    
    # Calling graph_paper function to draw the graph outlinea and boundaries
    graph_paper(k)
    
    #Setting instructions and results 
    title = font_two.render("GRAPH", 1, black)
    screen.blit(title, (width + 150, 20))
    
    instructions = font_one.render("Type in an equation such as : '3 * x^2 + 5'", 1, red)
    screen.blit(instructions, (width + 10, 70))
    
    instructions = font_one.render("Select 'Enter' when done or 'q' to start again", 1, red)
    screen.blit(instructions, (width + 10, 100))
    
    instructions = font_one.render("Select 'Backspace' to clear", 1, red)
    screen.blit(instructions, (width + 10, 130))
    
    instructions = font_three.render("s = sin()", 1, dark_green)
    screen.blit(instructions, (width + 65, 170))
    
    instructions = font_three.render("c = cos()", 1, dark_green)
    screen.blit(instructions, (width + 65, 210))
    
    instructions = font_three.render("t = tan()", 1, dark_green)
    screen.blit(instructions, (width + 65, 250))
    
    instructions = font_three.render("r = sqrt()", 1, dark_green)
    screen.blit(instructions, (width + 165, 170))
    
    instructions = font_three.render("a = abs()", 1, dark_green)
    screen.blit(instructions, (width + 165, 210))
    
    instructions = font_three.render("l = log10()", 1, dark_green)
    screen.blit(instructions, (width + 165, 250))
    
    instructions = font_three.render("n = log()", 1, dark_green)
    screen.blit(instructions, (width + 265, 170))
    
    instructions = font_three.render("e = e", 1, dark_green)
    screen.blit(instructions, (width + 265, 210))
    
    instructions = font_three.render("p = pi", 1, dark_green)
    screen.blit(instructions, (width + 265, 250))
    
    equation = []
    
    # Done is the variable which controls quiting of the screen
    # Active is the variable which controls the while loop condition
    done = False
    active = True
    while active:
        
        # Clipping bottom right corner to display the equation
        screen.set_clip(width + 10, height - 30, width + extra_width, height)
        screen.fill(white)
        string = ""
        eq = string.join(equation)
        eq_show = font_one.render("Function: y = " + eq, 1, red)
        screen.blit(eq_show, (width + 10, height - 30))
        
        # Refreshing screen each time
        pygame.display.update()
        
        for event in pygame.event.get():
            
            # If mouse event is clicking on close button, quit pygame screen
            if event.type == pygame.QUIT:
                active = False
                done = True
            
            # If any key is pressed    
            elif event.type == pygame.KEYDOWN:
                
                # cases for different keys on keyboard
                # also appending each key pressed to the array 'equations'
                if event.unicode == u'*':
                    equation.append("*")
                elif event.unicode == u'/':
                    equation.append("/")
                elif event.unicode == u'+':
                    equation.append("+")
                elif event.unicode == u'-':
                    equation.append("-")
                elif event.unicode == u'.':
                    equation.append(".")
                elif event.unicode == u'(':
                    equation.append("(")
                elif event.unicode == u')':
                    equation.append(")")      
                elif event.unicode == u'^':
                    equation.append("**")                 
                elif event.unicode == u'1':
                    equation.append("1")
                elif event.unicode == u'2':
                    equation.append("2")
                elif event.unicode == u'3':
                    equation.append("3")
                elif event.unicode == u'4':
                    equation.append("4")
                elif event.unicode == u'5':
                    equation.append("5")
                elif event.unicode == u'6':
                    equation.append("6")
                elif event.unicode == u'7':
                    equation.append("7")
                elif event.unicode == u'8':
                    equation.append("8")
                elif event.unicode == u'9':
                    equation.append("9")
                elif event.unicode == u'0':
                    equation.append("0")
                elif event.unicode == u'x':
                    equation.append("x")
                # For Enter key
                elif event.unicode == u'\r':
                    active = False
                # For Backspace key
                elif event.unicode == u'\b':
                    equation = []
                elif event.unicode == u'q':
                    main()
                # Math functions
                elif event.unicode == u's':
                    equation.append("sin(")
                elif event.unicode == u'c':
                    equation.append("cos(")
                elif event.unicode == u't':
                    equation.append("tan(")
                elif event.unicode == u'l':
                    equation.append("log10(")
                elif event.unicode == u'n':
                    equation.append("log(")
                elif event.unicode == u'e':
                    equation.append("e")
                elif event.unicode == u'p':
                    equation.append("pi")
                elif event.unicode == u'a':
                    equation.append("abs(")
                elif event.unicode == u'r':
                    equation.append("sqrt(")
                    
    
    if done:
        # Quit Pygame window                
        pygame.quit()
        
    else:
        # Clip right side of the screen (except the equation part)
        screen.set_clip(width, 0, width + extra_width, height - 30)
        screen.fill(white)
        screen.set_clip(None)
        
        # Calling graph equation function
        graph_eq(eq, k)
        
    sys.exit()
        
# Running the program by Python' way   
if __name__ == '__main__':
    main()