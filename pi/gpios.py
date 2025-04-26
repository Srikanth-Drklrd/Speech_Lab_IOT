import RPi.GPIO as gp

pin = { 'light' : 8,
		'printer' : 10,
		'speaker' : 12,
		'tv' : 16,
		'ac': 18,
		'fan' : 22,
		'anechoic_chamber' : 24}

gp.setmode(gp.BOARD)
for i in pin:
	gp.setup(pin[i],gp.OUT)
	
def switch(entity, state):
	gp.output(pin[entity],state)
