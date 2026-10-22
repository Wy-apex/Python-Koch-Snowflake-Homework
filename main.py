
import turtle
import math

# 第一步：定义科赫曲线递归函数
def koch_curve(pen, length, order):

    # 递归结束条件：0阶直接画一条直线
    if order == 0:
        pen.forward(length)

    else:
        # 将当前线段分成三等份
        length = length / 3

        # 绘制第一段
        koch_curve(pen, length, order - 1)

        # 向右转60度，绘制第二段
        pen.right(60)
        koch_curve(pen, length, order - 1)

        # 向左转120度，绘制第三段
        pen.left(120)
        koch_curve(pen, length, order - 1)

        # 向右转60度，绘制第四段
        pen.right(60)
        koch_curve(pen, length, order - 1)


# 第二步：定义科赫雪花绘制函数
def draw_snowflake(order):

    # 创建绘图窗口
    screen = turtle.Screen()
    screen.setup(900, 750)
    screen.title(f"科赫雪花 - {order}阶")
    screen.bgcolor("white")

    # 关闭逐笔动画，提高绘图速度
    screen.tracer(0)

    # 创建画笔
    pen = turtle.Turtle()
    pen.speed(0)
    pen.pensize(2)
    pen.color("blue")
    pen.hideturtle()

    # 设置初始三角形的边长
    length = 360

    # 移动画笔到绘图起点
    pen.penup()
    pen.goto(-length / 2, -length * math.sqrt(3) / 6)
    pen.setheading(0)
    pen.pendown()

    # 第三步：绘制三条科赫曲线，组成雪花
    for i in range(3):
        koch_curve(pen, length, order)
        pen.left(120)

    # 更新绘图窗口
    screen.update()

    print(f"{order}阶科赫雪花绘制成功！")

    # 保持绘图窗口打开
    screen.mainloop()


# 第四步：主程序
if __name__ == "__main__":

    try:
        # 接收用户输入的阶数
        order = int(input("请输入科赫雪花阶数（0～4）："))

        # 判断阶数是否符合要求
        if 0 <= order <= 4:
            draw_snowflake(order)

        else:
            print("错误：请输入0～4之间的整数！")

    except ValueError:
        print("错误：请输入一个整数！")
