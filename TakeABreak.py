'''
The program below prompts the user to take a break every 2 hours that they are on their computer
It plays a song by Marcus Warner called If I Should Return
'''
import webbrowser
import time

take_a_break = 3;

def get_off_computer (take_a_break):
	print ("This program started at" + time.ctime())
	for i in range (0,take_a_break):
		time.sleep(7200) #2 hour break program
		webbrowser.open("https://www.youtube.com/watch?v=mvlThZjDhzw")
	return ''
print (get_off_computer(take_a_break))	