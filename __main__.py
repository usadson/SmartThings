#!/usr/bin/python3
from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

#############################
#    Color = task equiv.    #
#############################
# Blue = idling             #
# Yellow = more than idling #
# Orange = Small game       #
# Red = heavy game          #
#############################

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
  if temp < 45:
    return calculate(blue, yellow, (temp - 30) / 15)
  elif temp < 60:
    return calculate(yellow, orange, (temp - 45) / 15)
  elif temp < 75:
    return calculate(orange, red, (temp - 60) / 25)
  elif temp < 90:
    return calculate(red, dark_red, (temp - 75) / 25)
  return dark_red # i.e. the component is in critical condition

def run_test0():
  for i in range(0, 17):
    ret = calculate((0xFF, 0x00, 0x00), (0x00, 0xFF, 0x00), i / 16.0)
    print("Ret: {0} {1} {2}".format(ret[0], ret[1], ret[2]))

def run_test1():
  temp = 20
  while True:
    temp += 1
    if temp > 100:
      temp = 20
    print("Temp: ", temp)
    sense.clear(temperature_to_color(temp))
    sleep(0.05)

run_test1()

