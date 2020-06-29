import pyautogui
from pynput import keyboard
from pptx import Presentation
from pptx.util import Inches
import os
from PIL import Image
import time
class Slide:
	prs = Presentation()
	prs.slide_height = Inches(18/1.2)
	prs.slide_width = Inches(32/1.2)
	blank_slide_layout = prs.slide_layouts[6]
	title_slide_layout = prs.slide_layouts[0]
	Slides = []
	screenshots = []
	imageName = None
	left = Inches(0)
	top = Inches(0)
	width,height = 1920,1080
	width_,height_ = int(width/3) , int(height/3)	
	pptxName = ""
	tempPath = r"D:\TOBB ETU\SstoPptx\temp\\"

	def addText(self):
		title = input("Title\t: ")
		subtitle = input("Subtitle\t:")
		self.screenshots.append((title,subtitle))

	def createNewSlide(self,type):
		if(type == "title"):
			self.Slides.append(self.prs.slides.add_slide(self.title_slide_layout))
		elif(type == "image"):
			self.Slides.append(self.prs.slides.add_slide(self.blank_slide_layout))		


	def takeSS(self):	
		self.screenshots.append(pyautogui.screenshot())


	def convertToPptx(self):
		t = time.localtime()
		timestamp = time.strftime('%b-%d-%Y_%H%M', t)
		self.pptxName = r"D:\TOBB ETU\SstoPptx" + r"\Slide  "+timestamp+".pptx"
		for i in range(len(self.screenshots)):
			print(str(i)+"->"+str(type(self.screenshots[i])))
		for i in range(len(self.screenshots)):			
			if(isinstance(self.screenshots[i],Image.Image)):
				print("*"*2+str(i)+"--> "+str(type(self.screenshots[i])))
				self.screenshots[i].save(self.tempPath + "ss"+str(i)+".png")##TODO: CLEAN THIS FOLDER BEFORE EXITING			
				self.createNewSlide("image")
				self.Slides[i].shapes.add_picture(self.tempPath + "ss"+str(i)+".png",self.left,self.top)
			elif(isinstance(self.screenshots[i],tuple)):
				self.createNewSlide("title")
				title = self.Slides[i].shapes.title
				subtitle = self.Slides[i].placeholders[1]
				title.text = self.screenshots[i][0]
				subtitle.text = self.screenshots[i][1]
				#self.Slides[i].shapes.title.text = self.screenshots[i][0]
				#self.Slides[i].placeholders[1].text = self.screenshots[i][1]	
		self.prs.save(self.pptxName)
		print("Saved to "+self.pptxName)


slide = Slide()
print("App Started ... \nListening for Key Inputs...\nScroll Lock\t-> TakeSS\nPause\t\t-> Convert\nEsc\t\t\t-> !!Exit!! ")

def on_press(key):
    try:    	
        #print('alphanumeric key {0} pressed'.format(key.char))
        pass
    except AttributeError:    	
        #print('special key {0} pressed'.format(key))
        pass

def on_release(key):
    #print('{0} released'.format(key))
    if key == keyboard.Key.esc:
    	if(input("Are you sure you want to quit without saving the file ? [Y/n]").lower() == 'y'):
    		return False
    	else:
    		print("Exiting aborted.\n")
    if key == keyboard.Key.pause:
        # Stop listener
        """  
        try:
        	slide.convertToPptx()
        	return False
        except:
        	print("!!! ERROR !!! File is safe.\t-->Check if powerPoint file is already opened and try again")
        """
        slide.convertToPptx()
        return False   
        
    if key == keyboard.Key.scroll_lock:
    	print(f"Scroll Lock key pressed : {len(slide.screenshots)+1}.Screenshot Taken")
    	#print('{0} released -> screenshot taken'.format(key))
    	slide.takeSS()

    if key == keyboard.Key.f9:
    	print("Title Slide created.\n")
    	slide.addText()

# Collect events until released
with keyboard.Listener(
        on_press=on_press,
        on_release=on_release) as listener:
    listener.join()

# ...or, in a non-blocking fashion:
listener = keyboard.Listener(
    on_press=on_press,
    on_release=on_release)
listener.start()
try:
	input("Press any key to exit.")
except:
	pass