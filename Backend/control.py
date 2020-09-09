import os
import io
import time
import json
from sense_hat import SenseHat
from random import randint
sense = SenseHat()
e = (0, 0, 0)
l = (250, 230, 210)
c = (0, 255, 255)

stamp=0
filename='/var/www/html/data.json'
def interpolate(a, b, amount):
    if a == b:
        return a
    elif a < b:
        return a + (b - a) * amount
    else:
        return a - (a - b) * amount
# Returns an interpolated color, i.e. between a and b
# @param a The color when amount = 0.0 (dict 3*int)
# @param b The color when amount = 1.0 (dict 3*int)
# @param amount The slider between a&b [0.0, 1.0] (float)
def calculate(a, b, amount):
    return (int(interpolate(a[0], b[0], amount)),
        int(interpolate(a[1], b[1], amount)),
        int(interpolate(a[2], b[2], amount)))

def temperature_to_color(temp):
    blue     = (0x00, 0x00, 0xFF)
    yellow   = (0xFF, 0xFF, 0x00)
    orange   = (0xFF, 0x80, 0x00)
    red      = (0xFF, 0x00, 0x00)
    dark_red = (0x8B, 0x00, 0x00)

    if temp < 30:
        return blue
    if temp < 60:
        return calculate(blue, yellow, (temp - 30) / 30)
    elif temp < 70:
        return calculate(yellow, orange, (temp - 60) / 10)
    elif temp < 80:
        return calculate(orange, red, (temp - 70) / 10)
    elif temp < 100:
        return calculate(red, dark_red, (temp - 80) / 20)
    return dark_red # i.e. the component is in critical condition
def update(cpu_temp, gpu_temp):
    x=temperature_to_color(cpu_temp)
    y=temperature_to_color(gpu_temp)
    print(cpu_temp, gpu_temp)
    pet1 = [
    l, l, l, c, c, l, e, l,
    l, e, e, c, c, l, e, l,
    l, l, l, c, c, e, l, e,
    x, x, x, c, c, y, y, y,
    x, x, x, c, c, y, y, y,
    x, x, x, c, c, y, y, y,
    x, x, x, c, c, y, y, y,
    x, x, x, c, c, y, y, y,
    ]
    sense.set_pixels(pet1)
while True:
	s=os.stat(filename).st_mtime
	if s!=stamp:
		stamp=s
		time.sleep(0.5)
		data=json.load(open(filename, 'r'))
		update(float(data['cpu_temp']), float(data['gpu_temp']))
	r = randint(1, 255)
	g = randint(1, 255)
	b = randint(1, 255)
	
	sense.set_pixel (4,0,r,g,b)
	sense.set_pixel (3,0,r,g,b)	
	time.sleep(0.25)