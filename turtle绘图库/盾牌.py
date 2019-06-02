# import turtle
#顺时针旋转角度right
#goto 设置开始位置
#画笔提起放下 penup pendown
# t = turtle.Turtle()
# t.penup()
# t.goto(50,50) #x,y轴移动的距离
# t.pendown()
# t.forward(50)
# t.right(90)
# t.forward(100)
# t.right(90)

#画布，宽，高，背景颜色
# turtle.screensize(500,500,'yellow')

#画笔，宽，颜色，移动速度
#粗细
# turtle.pensize(1)
#颜色
# turtle.pencolor('black')
#运动长
# turtle.forward(500)
#移动速度 0 - 10 快到慢
# turtle.speed(9)

#颜色填充
# t.fillcolor('red')
# t.speed(0)
# t.begin_fill() #准备填充
# for i in range(360):
#     t.forward(1)
#     t.right(1)
# t.end_fill() #填充结束

#保存画布一直开启状态
# turtle.done()

import turtle

t = turtle.Turtle()
t.speed(0)
def sepen(x,y):
     '''
     设置画笔的位置
     :param x:
     :param y:
     :return:
     '''
     #提笔
     t.penup()
     t.goto(x,y)
     t.pendown()
def circle(x,y,r,color):
    n = 36
    angle = 360/n
    p = 3.1415926
    c = 2 * p * r
    l = c/n
    sepen(x-l/2,y+r)
    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill()
    for i in range(n):
        t.forward(l)
        t.right(angle)
    t.end_fill()
def five_start(l):
    sepen(0,0)
    t.setheading(162)
    t.forward(150)
    t.setheading(0)
    t.fillcolor('red')
    t.begin_fill()
    t.hideturtle()
    t.penup()
    for i in range(5):
        t.forward(l)
        t.right(144)
    t.end_fill()

circle(0,0,300,'red')
circle(0,0,250,'white')
circle(0,0,200,'red')
circle(0,0,150,'blue')

five_start(284)
turtle.done()