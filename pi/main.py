from time import sleep
import cloud
import speech_engine
import gpios
import threading

speech_thread = threading.Thread(target = speech_engine.speech2intent)
speech_thread.start()

cloud.start_fb()

online_thread = threading.Thread(target = cloud.online_check)
online_thread.start()

while(1):
	sleep(0.5)
	if speech_engine.shared_data.state_changed:
		data = speech_engine.shared_data.changes.items()
		speech_engine.shared_data.state_changed = False
		speech_engine.shared_data.changes = dict()
		for key,state in data:
			try:
				cloud.update_state(key.lower(),state)
			except:
				print('\nproblem at cloud -> update_state')

	
