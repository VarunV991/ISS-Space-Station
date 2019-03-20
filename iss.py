#!/bin/python3

import json
import turtle
import urllib.request
import tkinter
url='http://api.open-notify.org/astros.json'
url1='http://api.open-notify.org/iss-now.json'
response=urllib.request.urlopen(url)  #To load the JSON response into a Python data structure
response1=urllib.request.urlopen(url1)
res=json.loads(response.read())
res1=json.loads(response1.read())
print('No. of people currently in Space: ',res['number'])
people=res['people']
for p in people:
	print(p['name'],end=' - ')
	print(p['craft'])
loc=res1['iss_position']
print('The current co-ordinates of the iss are: ')
lat=float(loc['latitude'])
lon=float(loc['longitude'])
print('latitude: ',lat)
print('longitude: ',lon)
#To show the iss in the world map
screen = turtle.Screen() 
screen.setup(720, 360)
screen.setworldcoordinates(-180,-90,180,90)
screen.bgpic('map.gif')

screen.register_shape('sat1.gif')
iss = turtle.Turtle()
iss.shape('sat1.gif')
iss.setheading(90)

iss.penup()
iss.goto(lon,lat)
tkinter.mainloop()
