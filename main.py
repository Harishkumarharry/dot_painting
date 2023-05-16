# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 50)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)
import random
import turtle as t

t.colormode(255)
tim = t.Turtle()
screen = t.Screen()
screen.setworldcoordinates(-1, -1, screen.window_width()-1, screen.window_height()-1)
color_list = [(132, 166, 205), (221, 148, 106), (32, 42, 61), (199, 135, 148), (166, 58, 48), (141, 184, 162),
              (39, 105, 157), (237, 212, 90), (150, 59, 66), (216, 82, 71), (168, 29, 33), (235, 165, 157),
              (51, 111, 90), (35, 61, 55), (156, 33, 31), (17, 97, 71), (52, 44, 49), (230, 161, 166), (170, 188, 221),
              (57, 51, 48), (184, 103, 113), (32, 60, 109), (105, 126, 159), (175, 200, 188), (34, 151, 210),
              (65, 66, 56), (106, 140, 124), (153, 202, 227), (48, 69, 71), (131, 128, 121)]

x_pos = tim.xcor()
y_pos = tim.ycor()


def draw_dot():
    for __ in range(10):
        tim.pendown()
        tim.dot(20, random.choice(color_list))
        tim.penup()
        tim.forward(50)


tim.hideturtle()
tim.speed("fastest")
for _ in range(10):
    tim.setposition(x_pos, y_pos)
    draw_dot()
    y_pos += 50


screen.exitonclick()
