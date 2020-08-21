from pyttsx3 import speak
import os
import time 
import calendar

speak("tell me what you desire for")
print('tell me what you desire for')
speak("simply type whatever you need")
print('simply type whatever you need:', end=" ")
while True:
	
	p = input()
	if (('show' in p) or ('tell' in p)) or ('what' in p) and ('date' in p):
	  os.system('date')
	elif (('show' in p) or ('what' in p)) and ('time' in p):
	  os.system('time')
	elif (('run' in p) or ('launch' in p)) and ('chrome' in p):
	  os.system('start chrome')
	elif (('run' in p) or ('launch' in p)) and ('wordpad' in p):
	  os.system('wordpad')
	elif (('run' in p) or ('launch' in p)) and ('notepad' in p):
	  speak("opening notepad")
	  os.system('notepad')
	elif (('run' in p) or ('launch' in p)) and ('camera' in p):
	  os.system('start camera')
	elif (('run' in p) or ('launch' in p)) and ('cmd' in p):
	  os.system('cmd.exe')
	elif (('run' in p) or ('launch' in p)) and ('firefox' in p):
	  os.system('start firefox')
	elif (("run" in p) or ("launch" in p)) and ("calculator" in p):
	  speak("opening calculator")
	  os.system("calc")
	elif ("stop" in p) or ("close" in p) or ("exit" in p) or ("end" in p):
	  speak("closing the software")
	  break
	else:
	  speak("dont support")
	  print('dont support')