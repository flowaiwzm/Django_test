import turtle

def on_release(x, y):
    print("Mouse button released at", x, y)

turtle.penup()
turtle.ondrag(turtle.goto)
turtle.onrelease(on_release)

turtle.mainloop()
