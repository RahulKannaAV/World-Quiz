import turtle
import pandas
import time
from tkinter import messagebox

sc = turtle.Screen()
tur = turtle.Turtle()
fo = ('Sans Serif',10,'bold')

ntl = 'map_img_588854_1527275717.gif'
sc.addshape(ntl)
tur.shape(ntl)

ned_province = pandas.read_csv('Netherlands.csv')

found_states = 0

while found_states<12:
    province = ned_province['Provinces'].unique()
    sc.title(f'Netherlands quiz. Found {found_states} out of 12')
    try:
        ans = turtle.textinput(title="Guess the Province", prompt='Enter the name of a province').title()
        if ans in province:
            found_states += 1
            turtle.hideturtle()
            turtle.penup()
            coor = ned_province[ned_province['Provinces'] == ans]
            turtle.goto(int(coor['x']),int(coor['y']))
            turtle.write(ans, font=fo)
    except AttributeError:
        print('Successfully exited')
        quit()

if found_states == 12:
    messagebox.showinfo(title='Quiz is finished', message='You have guessed all the names of the provinces!!\nCongratulations.')
    time.sleep(1.5)
    quit()

sc.exitonclick()
