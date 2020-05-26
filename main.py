import turtle
import parameters
import borders

########## Draw Window ##########
game_window = turtle.Screen()
game_window.title("Snake")
game_window.setup(parameters.SCREEN_WIDTH, parameters.SCREEN_HEIGHT, parameters.STARTX, parameters.STARTY)
game_window.bgcolor(parameters.BACKGROUND_COLOR)
game_window.tracer(0)

########## Game borders ##########
borders.draw_game_borders()

########## Game Loop ##########
while True:
    game_window.update()


########## Color Palette ##########
########## Color Palette ##########
########## Color Palette ##########
########## Color Palette ##########
########## Color Palette ##########
########## Color Palette ##########
########## Color Palette ##########
########## Color Palette ##########

#turtle.mainloop()