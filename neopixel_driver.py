import time
from random import uniform
from neopixel import *

FILENAME = "buzz.dat"

# LED strip configuration:
LED_COUNT	  = 150	  # Number of LED pixels.
LED_PIN		= 18	  # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ	= 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA		= 5	   # DMA channel to use for generating signal (try 5)
LED_BRIGHTNESS = 255	 # Set to 0 for darkest and 255 for brightest
LED_INVERT	 = False   # True to invert the signal (when using NPN transistor level shift)
color = [1,.75,.5]

def ramp(strip, wait_ms=50):
	for bright in range(0,256,6):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(int(bright*color[0]),int(bright*color[1]),int(bright*color[2])))
		strip.show()
	for bright in range(255,-1,-1):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, Color(int(bright*color[0]),int(bright*color[1]),int(bright*color[2])))
		strip.show()

# Define functions which animate LEDs in various ways.
def colorWipe(strip, color, wait_ms=50):
	"""Wipe color across display a pixel at a time."""
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, color)
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChase(strip, color, wait_ms=50, iterations=10):
	"""Movie theater light style chaser animation."""
	for j in range(iterations):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, color)
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)

def wheel(pos):
	"""Generate rainbow colors across 0-255 positions."""
	if pos < 85:
		return Color(pos * 3, 255 - pos * 3, 0)
	elif pos < 170:
		pos -= 85
		return Color(255 - pos * 3, 0, pos * 3)
	else:
		pos -= 170
		return Color(0, pos * 3, 255 - pos * 3)

def black(strip, wait_ms=20):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0, 0, 0))
		strip.show();
		time.sleep(wait_ms/1000.0)

def red(strip, wait_ms=20):
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(255, 0, 0))
		strip.show();
		time.sleep(wait_ms/1000.0)

def rainbow(strip, wait_ms=20, iterations=1):
	"""Draw rainbow that fades across all pixels at once."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel((i+j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def rainbowCycle(strip, wait_ms=20, iterations=5):
	"""Draw rainbow that uniformly distributes itself across all pixels."""
	for j in range(256*iterations):
		for i in range(strip.numPixels()):
			strip.setPixelColor(i, wheel(((i * 256 / strip.numPixels()) + j) & 255))
		strip.show()
		time.sleep(wait_ms/1000.0)

def theaterChaseRainbow(strip, wait_ms=50):
	"""Rainbow movie theater light style chaser animation."""
	for j in range(256):
		for q in range(3):
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, wheel((i+j) % 255))
			strip.show()
			time.sleep(wait_ms/1000.0)
			for i in range(0, strip.numPixels(), 3):
				strip.setPixelColor(i+q, 0)


strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS)
# Intialize the library (must be called once before other functions).
strip.begin()

oldbuzz = 0
while True:
	buzzdat = open(FILENAME, 'r').read()
	try:
		buzz=int(buzzdat)
	except ValueError:
		pass
	wait_ms = 220 - buzz*2 
	spacing = int(wait_ms / 10) + 1
	if (oldbuzz != buzz): 
		ramp(strip)
		print "buzz =", buzz
	for i in range(strip.numPixels()):
		strip.setPixelColor(i, Color(0,0,0))

	for q in range(buzz):
		random=int(uniform(0,strip.numPixels()));
		strip.setPixelColor(random, Color(int(color[0]*255),int(color[1]*255),int(color[2]*255)))
	strip.show()
	time.sleep(wait_ms/1000.0)
	oldbuzz = buzz


	# for q in range(spacing):
	#	 for i in range(0, strip.numPixels(), spacing):
	#		 strip.setPixelColor(i+q, Color(255,255,255))
	#	 strip.show()
	#	 time.sleep(wait_ms/1000.0)
	#	 for i in range(0, strip.numPixels(), spacing):
	#		 strip.setPixelColor(i+q, 0)

	# time.sleep(.1)
		# theaterChaseRainbow(strip, wait_ms=delta)
