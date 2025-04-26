import pvporcupine
import pvrhino
import pyaudio
import wave
import numpy as np
import time
import gpios

class data:
	state_changed = False
	changes =  dict()
	
shared_data = data()

def speech2intent():
	porcupine = pvporcupine.create(keyword_paths=["~/speech-iot/hey_cera.ppn"],
								access_key = "sXtgT8EwOOUXNJFivyYkEnTYm/V5phsMNSDzw+Zh9p9HdniCBqbzCw==")  # You can also use the custom .ppn file if created
	
	rhino = pvrhino.create(context_path="cera_cmds.rhn",
								access_key = "sXtgT8EwOOUXNJFivyYkEnTYm/V5phsMNSDzw+Zh9p9HdniCBqbzCw==")

	pa = pyaudio.PyAudio()
	audio_stream = pa.open(
	    rate=porcupine.sample_rate,
	    channels=1,
	    format=pyaudio.paInt16,
	    input=True,
	    frames_per_buffer=porcupine.frame_length*5
	)
	
	global state_changes
	global changes
	
	rhino.reset()
			
	try:
		while True:
			print("\r","Listening for 'Cera'...", end = " ")
			signal_stream = audio_stream.read(porcupine.frame_length,exception_on_overflow=False)
			signal = np.frombuffer(signal_stream,dtype=np.int16)
			decide = porcupine.process(signal)
			if decide >= 0:
				print("\n\n'Cera' word detected\n")
				start_time = time.time()
				while (time.time() - start_time < 4):
					signal_stream = audio_stream.read(rhino.frame_length, exception_on_overflow = False)
					signal = np.frombuffer(signal_stream,dtype = np.int16)
					if rhino.process(signal):
						inference = rhino.get_inference()
						if inference.is_understood:
							state = 1 if inference.slots['state'] == 'on' else 0
							shared_data.changes[inference.intent] = state
							shared_data.state_changed = True
							gpios.switch(inference.intent.lower(), state)
							print("\ncommand :",inference.intent,"-",inference.slots['state'],"\n")
							break
	except:
		print(OSError)
	
	finally:
		print("\n\ncleaning up the resources...")
		porcupine.delete()
		rhino.delete()
		audio_stream.close()
		pa.terminate()

