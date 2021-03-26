import turtle

str = 'X'
queue = []

def evolve(str):
    new_str = ''
    for ch in str:
        if(ch == 'X'):
            new_str += 'F+[[X]-X]-F[-FX]+X'
        elif(ch == 'F'):
            new_str += 'FF'
        elif(ch == '['):
            new_str += '['
        elif(ch == ']'):
            new_str += ']'
        elif(ch == '-'):
            new_str += '-'
        elif(ch == '+'):
            new_str += '+'

    return new_str

for n in range(6):
    str = evolve(str)

wn = turtle.Screen()
wn.bgcolor("black")

mrk = turtle.Turtle()
mrk.color("green")
mrk.shape("circle")
mrk.turtlesize(stretch_wid=0.2, stretch_len=0.2)
mrk.degrees()
mrk.speed("fastest")
mrk.penup()
mrk.setpos(-600, -300)
mrk.pendown()
mrk.seth(45)

while str:
    if(str[0] == 'F'):
        mrk.forward(6)
    elif(str[0] == '-'):
        mrk.right(20)
    elif(str[0] == '+'):
        mrk.left(20)
    elif(str[0] == '['):
        queue.append([mrk.pos(), mrk.heading()])
    elif(str[0] == ']'):
        data = queue.pop()
        mrk.penup()
        mrk.setpos(data[0])
        mrk.seth(data[1])
        mrk.pendown()
    str = str[1:]

wn.mainloop()