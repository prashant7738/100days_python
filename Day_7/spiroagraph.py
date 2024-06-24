import turtle as turtle_module
import random 

# # THIS IS DONE TO EXTRACT THE COLORS FROM THE IMAGE
# import colorgram

# all_colors = []
# colors = colorgram.extract("image.jpg",15)
# # print(color)

# for color in colors:
#     r= color.rgb.r
#     g= color.rgb.g
#     b= color.rgb.b
#     new_color = (r,g,b)
#     all_colors.append(new_color)

# print(all_colors)


turtle_module.colormode(255)
mbappe = turtle_module.Turtle()

color_list = [(226, 222, 216), (228, 219, 222), (218, 227, 220), (219, 221, 229),
              (199, 165, 133), (142, 163, 193), (223, 205, 117), (77, 87, 136),
              (190, 151, 163), (149, 64, 81), (156, 85, 50), (143, 184, 161),
              (218, 82, 60), (190, 90, 109), (56, 43, 37)]

mbappe.speed("fastest")
mbappe.penup()
mbappe.hideturtle()
mbappe.setheading(225)
mbappe.forward(300)
mbappe.setheading(0)
for dot_count in range(1 , 101):
    mbappe.dot(20, random.choice(color_list))
    mbappe.forward(50)

    if dot_count %10 == 0:
        mbappe.setheading(90)
        mbappe.forward(50)
        mbappe.setheading(180)
        mbappe.forward(500)
        mbappe.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
