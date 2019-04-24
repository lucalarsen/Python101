from sense_hat import SenseHat
from time import sleep
from random import randint
from random import choice

sense = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)


rndcolor1 = randint(0,255)
rndcolor2 = randint(0,255)
rndcolor3 = randint(0,255)
rndcolortotal = (rndcolor1, rndcolor2, rndcolor3)

deck = ['ace', 'king', 'queen','jack']
card = choice(deck)

def message():
  sense.show_message("Lagkage", scroll_speed=0.05, text_colour=rndcolortotal)
  
def letter():
  sense.show_letter("L", text_colour=blue)
  
def smiley():
  G = green
  B = blue
  Y = yellow
  R = red
  O = nothing
  logo = [
  O, O, O, O, O, O, O, O,
  O, Y, Y, Y, B, G, O, O,
  Y, Y, Y, Y, Y, B, G, O,
  Y, Y, Y, Y, Y, B, G, O,
  Y, Y, Y, Y, Y, B, G, O,
  Y, Y, Y, Y, Y, B, G, O,
  O, Y, Y, Y, B, G, O, O,
  O, O, O, O, O, O, O, O,
  ]
  return logo

while True:
  #letter()
  #sleep(1)
  #message()
  #sleep(1)
  #letter()
  sense.set_pixels(smiley())
