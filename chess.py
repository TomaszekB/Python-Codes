import turtle

window = turtle.Screen()
pen = turtle.Turtle()

def chess_board():
    for i in range(4):
        pen.forward(50)
        pen.left(90)

    pen.forward(50)

if __name__ == "__main__":
    window.setup(1024, 800)
    pen.speed(3)

    for i in range(4):
        pen.up()
        pen.setpos(0, 50 * i)
        pen.down()
        for j in range(4):
            if (i + j) % 2 == 0:
                col = 'white'
            else:
                col = 'black'
            pen.fillcolor(col)
            pen.begin_fill()
            chess_board()
            pen.end_fill()
