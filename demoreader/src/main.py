from turtle import Turtle, Screen
import random


# creating the object of the turtle
temp = Turtle("turtle")
tummy = Turtle("turtle")
tonny = Turtle("turtle")
tinny = Turtle("turtle")
tommy = Turtle("turtle")
zanny = Turtle("turtle")
screen = Screen()


colors = ['red','orange','yellow','green','blue','purple']


# we don't went to draw so we are going to do this 
temp.penup()
tummy.penup()
tonny.penup()
tinny.penup()
tommy.penup()
zanny.penup()


is_game_over = False
winner_of_the_turtle_race = ""

# now i am going to store the object to an list object
obj_of_turtle = [temp,tummy,tonny,tinny,tommy,zanny]
# nwo i am going to setup the screen with width of 500 and hight of 400
screen.setup(width=500,height=400)

# we need to ask the user to input the bet 
user_bat_on = screen.textinput(title = "Make youur bat", prompt= "Which turtle will win the race? Enter a color:")
# now i am also going to check whether user have choosen the right color
if not user_bat_on in colors:
    user_bat_on = screen.textinput(title="Again Make you're bat", prompt= "Choose a color:")
# now i am going to set every color to separate turtlee object
for i in range(len(colors)):
    obj_of_turtle[i].color(colors[i])
    # # we need to move our turtle randomly forward
    # obj_of_turtle[i].forward(random.randint(0,10))


# now i need to move my cursor to the - x esis that is as start point
temp.goto(x=-230,y=-100)
# print(user_bat_on)
tummy.goto(x=-230,y=-80)
tonny.goto(x=-230,y=-60)
tinny.goto(x=-230,y=-40)
tinny.goto(x=-230,y=80)
tommy.goto(x=-230,y=60)
zanny.goto(x=-230,y=40)

# now again i am giong to loop throu the object variable list..
while not is_game_over:
    for i in obj_of_turtle:
        i.forward(random.randint(a=0, b=10))
        # nwo we are going to define a logic that will
        # check if one of the turtle object reach to the 
        # x cordinate of 230 then the game will give the victore
        if i.xcor() > 230 :
            winner_of_the_turtle_race = i.pencolor()
            is_game_over = True


if winner_of_the_turtle_race == user_bat_on:
    print(f"You have won the race!!{winner_of_the_turtle_race}")
else:
    print(f"You have lose the game!! the winner is :{winner_of_the_turtle_race}")


screen.exitonclick()