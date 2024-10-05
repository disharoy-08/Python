import turtle


screen = turtle.Screen()
screen.title("India States Game")
image = "empty_state_india.gif"
screen.addshape(image)
turtle.shape(image)

# def get_mouse_click_coor(x,y):
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()

answer_state = screen.textinput(title= "Guess the state", prompt="What's another state's name?")
print(answer_state)

#screen.exitonclick()
