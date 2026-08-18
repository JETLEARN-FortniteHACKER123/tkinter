from operator import pos
from tkinter import *
import time
import random
from tkinter import messagebox
mywin = Tk()
mywin.title("Ping Pong CLASH")
# can not resize the window
mywin.resizable(0, 0)


# the canvas is 600 by 500
canvas_width = 600
canvas_height = 500



# making a canvas widget
canvas = Canvas(mywin, width=canvas_width, height=canvas_height, bg="black") 
# then pack the canvas widget
canvas.pack()

#make a font for showing the score
score_font = ("Arial", 20, "bold")
# inside the canvas make a text object called scoring_text
scoring_text = canvas.create_text(200,20,font=score_font, text = "0:0", fill="blue")

# create a line in the centre - kind of a partition
canvas.create_line(canvas_width/2, 0, canvas_width/2, canvas_height, fill="white",)
# to make a circle at the centre of the canvas, first find the centre of the canvas

x = canvas_width/2
y = canvas_height/2
# i want to draw the circle of radius 50
r = 50
#now for drawing the circle, we need to find the top left point and the bottom right point
x0 = x - r
y0 = y - r
x1 = x + r
y1 = y + r
# now draw the circle
middle_circle = canvas.create_oval(x0, y0, x1, y1, outline="white")

#paddle dimensions
paddle_width = 20
paddle_height = 80

#creating a class for the paddle
class Paddle:
    # the padle needs the canvas, where it is to be drawn, the x and y coordinates of the top left corner of the paddle, and the color of the paddle
    def __init__(self, canvas, x, y, color):
        self.canvas = canvas
        # the paddle is like a rectangle which needs the top left and bottom right corners
        #so in the below command
        #x, y - refer to the top left corner of the rectangle
        #x + paddle_width, y + paddle_height - refer to the bottom right corner 
        self.paddle = canvas.create_rectangle(x, y, x + paddle_width, y + paddle_height, fill=color)
        #this delta defines the speed with which we need to move the paddle up or down
        self.delta = 0

 # there are two paddles, so i am making a function which will define the movement of the paddle 
    def moveUpDownUsing(self, keypressUp, keypressDown):
    # binding for moving the paddle up
     self.canvas.bind_all(keypressUp, self.moveUp)
    # binding for moving the paddle down
     self.canvas.bind_all(keypressDown, self.moveDown)
 #this function is the main behaviour function which the paddle moves up or down
    def draw(self):
        # move is a generic method which helps in moving any component
     # here we want to move the paddle itself
     #0 means do not move it horizontally
        #delta means that it needs to move only vertically
        self.canvas.move(self.paddle, 0, self.delta)
        pos =   self.canvas.coords(self.paddle)
    # if the paddle touches the top , make the delta to 0, so that it does not move up anymore
        if pos[1] <= 0:
          self.delta = 0
    # if the paddle touches the bottom, make the delta to 0, so that it does not move down anymore
        if pos[3] >= canvas_height:
         self.delta = 0


 # the delta changes to -4 so that the paddle starts moving up
    def moveUp(self, event):            
     self.delta = -4
 # delta changes to 4 so that the paddle starts moving down
    def moveDown(self, event):
     self.delta = 4

leftpaddle = Paddle(canvas, "orange", 10 , canvas_height/2)
leftpaddle.moveUpDownUsing("<w>", "<s>")
rightpaddle = Paddle(canvas, "green", 570, canvas_height/2)
rightpaddle.moveUpDownUsing("<Up>", "<Down>")

#2 scores
leftPaddleScore = 0
rightPaddleScore = 0

# now lets make the ball
class Ball:
    global leftpaddle, rightpaddle
    #constructs the ball
    def __init__(self, canvas, color):
        self.canvas = canvas
        # its an oval - create it first
        #10,10 is top left
        # 30,30 is bottom right
        self.ball = canvas.create_oval(10, 10, 30, 30, fill=color)
        # then move it to the centre of the screen
        self.canvas.move(self.ball, canvas_width/2, canvas_height/2)
        # the ball moves both horizontally and vertically, so we need to define two deltas
        self.deltax  = random.randint(-4,4)
        self.deltay = random.randint(-4,4)
    # the function which makes the ball move
    def draw(self):
        global leftPaddleScore, rightPaddleScore
        self.canvas.move(self.ball, self.deltax, self.deltay)
        # lets get the position of the ball
        pos = self.canvas.coords(self.ball)
        # if the ball touches the top or bottom, reverse the vertical direction
        if pos[1] <= 0 :
            self.deltay = random.randint(1,4)
        #if the ball hits the bottom edge
        if pos[1] >= canvas_height:
            self.deltay = random.randint(-4,-1)
        # if the ball hits the left side
        if pos[0] <= 0:
        # start sending it from left to right
         self.deltax = 4    
         rightPaddleScore += 1
         canvas.itemconfig(scoring_text, text = str(leftPaddleScore)) 
        # if the ball hits the right side
        if pos[2] >= canvas_width:
        # start sending it from right to left
         self.deltax = -4
         leftPaddleScore += 1
         canvas.itemconfig(scoring_text, text = str(leftPaddleScore)+":"+str(rightPaddleScore))
        # checking if hitting paddles
        if self.hit_Paddle1(pos) == True:
           self.deltax = 4
        if self.hit_Paddle2(pos) == True:
           self.deltax = -4

# can draW A PICTURE TO EXPLAIN THIS CHECK, BALL TOUCHING LEFT PADDLE
    def hit_Paddle1(self, pos):
        global leftpaddle
        paddle_pos = self.canvas.coords(leftpaddle.paddle)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
        return False
    def hit_Paddle2(self, pos):
       global rightpaddle
       paddle_pos = self.canvas.coords(rightpaddle.paddle)
       if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
       return False


ball = Ball(canvas, "yellow")    
while 1:
    leftpaddle.draw()
    rightpaddle.draw()
    ball.draw()
    mywin.update_idletasks()
    mywin.update()
    time.sleep(0.01)
    # game stop as soon as one of the players scores 10 points
    if leftPaddleScore == 10 or rightPaddleScore == 10:
        messagebox.showinfo("Game Over", "Player 1 Score: " + str(leftPaddleScore) + "\nPlayer 2 Score: " + str(rightPaddleScore))
        break
mywin.mainloop()    
