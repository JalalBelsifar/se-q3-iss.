#!/usr/bin/env python

__author__ = 'Jalal, with help from Joseph, Greg'

import json
import turtle
import time
import requests


def get_astraunauts():
    """get a total number of astronauts in
    the spacecraft in space"""
    crew = requests.get('http://api.open-notify.org/astros.json')
    astronauts = crew.text
    astronauts = json.loads(astronauts)
    for i in astronauts['people']:
        print('{} is on the ISS  spaceship orbiting the Earth'.format(
            i['name']))


def get_coords():
    """get current coordinates of ISS along with
    timestamp"""
    position = requests.get(
        'http://api.open-notify.org/iss-now.json')
    coords = position.text
    coords = json.loads(coords)
    current_location = coords['iss_position']
    print('At ' + str(time.ctime(coords['timestamp'])) +
          ' the ISS was at ' + str(current_location['longitude']) +
          ' latitude and ' + str(current_location['latitude']) + ' longitude')
    return (float(current_location['longitude']), float(current_location['latitude']))


def indianapolis_pass():
    res = requests.get(
        "http://api.open-notify.org/iss-pass.json?lat=40&lon=-86.1349")
    over_head = res.text
    over_head = json.loads(over_head)
    over_indiana = over_head['response'][0]
    next_pass_date = time.ctime(over_indiana['risetime'])
    return 'The next time the ISS will pass over Indianapolis is on : {}'.format(next_pass_date)


def create_turtle_display(iss_position, next_run):
    """Setup a turtle dispay screen. Create a yellow dot for
    Indy geolocation"""
    graphic_screen = turtle.Screen()
    graphic_screen.bgpic('./map.gif')
    graphic_screen.addshape('iss.gif')
    graphic_screen.setup(width=720, height=360)
    graphic_screen.setworldcoordinates(-180, -90, 180, 90)
    iss = turtle.Turtle()
    iss.shape('iss.gif')
    iss.penup()
    iss.goto(iss_position)
    indy_dot = turtle.Turtle()
    indy_dot.shape('triangle')
    indy_dot.color('yellow')
    indy_dot.penup()
    indy_dot.goto(-86.1349, 40.273502)
    indy_text = turtle.Turtle()
    indy_text.penup()
    indy_text.color('yellow')
    indy_text.write(next_run, True, align='center', font=('Times New Roman', 15, 'normal'))
    graphic_screen.exitonclick()


def main():
    get_astraunauts()
    position = get_coords()
    next_run = indianapolis_pass()
    create_turtle_display(position, next_run)


if __name__ == '__main__':
    main()