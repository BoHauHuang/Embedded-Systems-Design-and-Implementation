import keyboard

while 1:
	key = keyboard.read_hotkey(suppress=False)
	if key:
		print("You pressed "+str(key))
	if key == 'esc+q':
		break
