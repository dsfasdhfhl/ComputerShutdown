import appJar
import webbrowser
import os
import time
import random
from appJar import gui

def fortnite():
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	webbrowser.open("youtube.com/watch?v=os9FW79RVEI&t=17s")
	
def close():
	os.startfile("Shutdown.bat")
	time.sleep(3)

app = gui()
app.addLabel("30", "Anti-Virus Scan")
app.addButton("Start Scaning", fortnite)
app.addButton("Close", close)
app.go()
	