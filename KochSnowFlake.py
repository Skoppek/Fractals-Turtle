import turtle
import math

seq = "A"

def get_new_seq(seq):
    newseq = ""
    for i in seq:
        if(i == "A"):
            newseq += "ABCD"
        elif(i == "B"):
            newseq += "BBCD"
        elif(i == "C"):
            newseq += "CBCD"
        elif(i == "D"):
            newseq += "DBCD"
    return newseq

def draw_Koch(plr, seq, len):
    for i in seq:
        if(i == "A"):
            plr.forward(len)
        elif(i == "B"):
            plr.left(60)
            plr.forward(len)
        elif(i == "C"):
            plr.right(120)
            plr.forward(len)
        elif(i == "D"):
            plr.left(60)
            plr.forward(len)

def draw_Koch_inv(plr, seq, len):
    for i in seq:
        if(i == "A"):
            plr.forward(len)
        elif(i == "B"):
            plr.right(60)
            plr.forward(len)
        elif(i == "C"):
            plr.left(120)
            plr.forward(len)
        elif(i == "D"):
            plr.right(60)
            plr.forward(len)

wn = turtle.Screen()
wn.title("fff")
wn.bgcolor("black")

plr = turtle.Turtle()
plr.color("white")
plr.speed("fastest")

turtle.degrees()
len = 360
n = 6
plr.penup()
plr.setpos(-len / 2, 0.5 * math.sqrt(0.75 * len **2))
plr.pendown()
while(n > 0):
    draw_Koch(plr, seq, len)
    plr.right(120)
    draw_Koch(plr, seq, len)
    plr.right(120)
    draw_Koch(plr, seq, len)
    plr.right(120)
    draw_Koch_inv(plr, seq, len)
    plr.right(120)
    draw_Koch_inv(plr, seq, len)
    plr.right(120)
    draw_Koch_inv(plr, seq, len)
    seq = get_new_seq(seq)
    plr.right(120)
    len /= 3
    n -= 1

wn.mainloop()

