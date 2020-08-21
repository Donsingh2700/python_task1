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
	if (('run' in p) or ('launch' in p) or ('execute' in p)) and ('chrome' in p):
	  speak("opening chrome")
	  os.system('start chrome')
	elif (('run' in p) or ('launch' in p) or ('execute' in p)) and ('wordpad' in p):
	  speak("opening wordpad")
	  os.system('wordpad')
	elif (('run' in p) or ('launch' in p) or ('execute' in p)) and ('notepad' in p):
	  speak("opening notepad")
	  os.system('notepad')
	elif (('run' in p) or ('launch' in p) or ('execute' in p)) and ('cmd' in p):
	  speak("opening command")
	  os.system('cmd.exe')
	elif (('run' in p) or ('launch' in p) or ('execute' in p)) and ('firefox' in p):
	  speak("opening firefox")
	  os.system('start firefox')
	elif (("run" in p) or ("launch" in p) or ('execute' in p)) and ("calculator" in p):
	  speak("opening calculator")
	  os.system("calc")
	elif (('show' in p) or ('tell' in p)) or ('what' in p) and ('date' in p):
	  os.system('date')
	elif (('show' in p) or ('what' in p)) and ('time' in p):
	  os.system('time')
	elif ("stop" in p) or ("close" in p) or ("exit" in p) or ("end" in p):
	  speak("closing the software")
	  break
	else:
	  speak("dont support")
	  print('dont support')