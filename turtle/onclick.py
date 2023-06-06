import turtle

# 定义一个函数，用来画一个正方形
def draw_square(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    for i in range(4):
        turtle.forward(100)
        turtle.left(90)

# 将draw_square函数作为参数传递给onclick函数
turtle.onclick(draw_square)

# 保持窗口不关闭
turtle.done()
