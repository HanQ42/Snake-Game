import turtle
import parameters
########## Game borders ##########
def draw_game_borders():
    ########## Upper border ##########
    gameFrame = turtle.Turtle()
    gameFrame.penup()
    gameFrame.goto(parameters.ORIGIN, (parameters.SCREEN_HEIGHT - parameters.BLOCK_WIDTH)/2)
    gameFrame.shape(parameters.SQUARE)
    gameFrame.color(parameters.BORDER_COLOR)
    gameFrame.shapesize(parameters.UPPER_LOWER_BORDER_HEIGHT, (parameters.SCREEN_WIDTH / 20))

    ########## Lower border ##########
    gameFrame = turtle.Turtle()
    gameFrame.penup()
    gameFrame.goto(parameters.ORIGIN, -300)
    gameFrame.shape(parameters.SQUARE)
    gameFrame.color(parameters.BORDER_COLOR)
    gameFrame.shapesize(parameters.UPPER_LOWER_BORDER_HEIGHT, (parameters.SCREEN_WIDTH / 20))

    ########## Left border ##########
    gameFrame = turtle.Turtle()
    gameFrame.penup()
    gameFrame.goto(parameters.SCREEN_WIDTH / -2, parameters.ORIGIN)
    gameFrame.shape(parameters.SQUARE)
    gameFrame.color(parameters.BORDER_COLOR)
    gameFrame.shapesize(parameters.LEFT_RIGHT_BORDER_HEIGHT, parameters.LEFT_RIGHT_BORDER_WIDTH)

    ########## Right border ##########
    gameFrame = turtle.Turtle()
    gameFrame.penup()
    gameFrame.goto(parameters.SCREEN_WIDTH / 2, parameters.ORIGIN)
    gameFrame.shape(parameters.SQUARE)
    gameFrame.color(parameters.BORDER_COLOR)
    gameFrame.shapesize(parameters.LEFT_RIGHT_BORDER_HEIGHT, parameters.LEFT_RIGHT_BORDER_WIDTH)

    ########## Upper border game field line ##########
    gameFrame = turtle.Turtle()
    gameFrame.penup()
    gameFrame.goto(parameters.ORIGIN, parameters.GAME_FIELD_LINE_LOCATION)
    gameFrame.shape(parameters.SQUARE)
    gameFrame.color(parameters.BORDER_COLOR)
    gameFrame.shapesize(1, parameters.BLOCK_WIDTH)