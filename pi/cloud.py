import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
import gpios
import socket
import time
import threading

state_data = dict()   # for future use (use it in a class)
state_changed = False
changed_entity = ''

class network:
	online_state = False
	started = False
	lab_ref = None
	listener = None

ntwk_state = network()

def is_connected():
    try:
        socket.create_connection(("8.8.8.8", 53), timeout=10)
        return True
    except (socket.timeout, socket.error):
        return False

if is_connected():
    print("Connected to the Internet")
else:
    print("No Internet Connection")


def listener_callback(event):
	global state_data, state_changed, changed_entity
	if event.path == '/':
		state_data = event.data
		for i in state_data:
			gpios.switch(i,state_data[i])
	else:
		changed_entity = event.path.strip('/')
		state_data[changed_entity] = event.data
		gpios.switch(changed_entity,event.data)
	
	state_changed = True

def start_fb():
	global ntwk_state
	if is_connected():
		cred = credentials.Certificate("/home/cera/speech-iot/key.json")
		firebase_admin.initialize_app(cred,{'databaseURL':'https://speech-lab-iot-default-rtdb.europe-west1.firebasedatabase.app/'})
		lab_ref = db.reference('/lab/actuation')
		lab_ref.listen(listener_callback)
		ntwk_state.online_state = True
		ntwk_state.started = True
		ntwk_state.lab_ref = lab_ref
		for thread in threading.enumerate():
			if 'start_listen' in thread.name:
				ntwk_state.listner = thread
	else:
		ntwk_state.online_state = False
		
def online_check():
	global ntwk_state
	while True:
		if not ntwk_state.online_state:
			if is_connected():
				ntwk_state.online_state = True
				if not ntwk_state.started:
					start_fb()
				elif not ntwk_state.listener.is_alive():
					ntwk_state.lab_ref.listen(listener_callback)
					for thread in threading.enumerate():
						if 'start_listen' in thread.name:
							ntwk_state.listner = thread		
		time.sleep(10)
			

def update_state(entity,state):
	global ntwk_state
	if ntwk_state.online_state:
		try:
			ntwk_state.lab_ref.update({entity:state})
		except:
			ntwk_state.online_state = False
