import turtle
import pandas
import time
from tkinter import messagebox

sc = turtle.Screen()
sc.setup(width=910, height=540)
tur = turtle.Turtle()
fo = ('Sans Serif',5,'bold')
big_fo = ('Sans Serif',10,'bold')
ex_big = ('Sans Serif',25,'bold')

SU = 'soviet.gif'
sc.addshape(SU)
tur.shape(SU)

soviet = pandas.read_csv('Soviet_Union.csv')
small = ['Moldova','Armenia','Azerbaijan','Georgia','Estonia','Lithuania','Latvia']
big = ['Russia','Kazakhstan']

found_states = 0
while found_states < 15:
    province = soviet['Countries'].unique()
    sc.title(f'Soviet Union quiz. Found {found_states} out of 15')
    try:
        ans = turtle.textinput(title="Guess the Province", prompt='Enter the name of a province').title()
        if ans in province:
            found_states += 1
            turtle.hideturtle()
            turtle.penup()
            turtle.setheading(245)
            coor = soviet[soviet['Countries'] == ans]
            turtle.goto(int(coor['x']),int(coor['y']))
            if ans in small:
                turtle.write(ans, font=fo)
            elif ans in big:
                turtle.write(ans, font=ex_big)
            elif ans not in big and small:
                turtle.write(ans, font=big_fo)
    except AttributeError:
        print('Successfully exited')
        quit()

if found_states == 15:
    messagebox.showinfo(title='Quiz is finished', message='You have guessed all the names of the Countries!!\nCongratulations.')
    time.sleep(1.5)
    quit()

sc.exitonclick()
