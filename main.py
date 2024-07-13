from instagrapi import Client
import os
import random
from inspirational_quotes import quote
from textwrap import wrap
import cv2




def upload():


	username = "" # your username here
	password = "" # your password here
	print("logging in...")


	client = Client()
	client.login(username, password)
	music_keywords = ["love", "emotional", "motivating"] # you can customize your music searchword here


	tracklist = client.search_music(random.choice(music_keywords))
	print("uploading...")
	try:
		video = client.clip_upload_as_reel_with_music("Video.mp4", caption = "test2", track = tracklist[0])
	except:

		print("Done")


class Text():
	def __init__(self):
		self.text = quote()["quote"]

		self.font = cv2.FONT_ITALIC # your font goes here
		self.text = wrap(self.text, 12)
		self.line_width = self.get_width()
		self.line_height = self.get_height()
		self.heightlist = []



		print(self.line_height)
		print(self.line_width)
		
	def fill_heightlist(self, vy):
		counter = 0
		for i in self.text:

			self.heightlist.append((vy + (self.line_height[0] / 2)) + counter)
			counter += self.line_height[0] + 20

	def get_width(self):

		width = []
		if isinstance(self.text, list):
			print("this is a list")
			for i in self.text:
				width.append(cv2.getTextSize(i, self.font, 1, 2 )[0][0])
		elif isinstance(self.text, str):
			print("string")
		return width

	def get_height(self):


		height = []
		if isinstance(self.text, list):
			print("this is a list")
			for i in self.text:
				height.append(cv2.getTextSize(i, self.font, 1, 2 )[0][1])
		elif isinstance(self.text, str):
			print("string")

		return height


class Producer():
	def __init__(self):


		self.video = ""
		self.audio = ""
		self.text = ""
		self.video_width = ""
		self.video_height = ""

		self.video_length = ""
		self.video_name = "Video.mp4"


		self.duration = 15
		self.bg_choice = "./backgrounds/" + random.choice(os.listdir("./backgrounds"))
		
	def put_text_in_video(self, text, frame):
		

		linecounter = 0
		for i in text.text:
			cv2.putText(
				frame,
				str(i.replace("’", "")),
				(int((self.video_width/2) - (text.line_width[text.text.index(i)] * 1.5)),
				 int(((self.video_height / 4) + (text.line_height[0] /2)) + (linecounter * (text.line_height[0] + 20)))),
				self.text.font,
				3,
				(0,0,0),
				2 )´# size of the text
			# you need to finetune your TextSize and Video size

			linecounter += 5
		
			


	def produce_video(self):
		
		self.video = cv2.VideoCapture(self.bg_choice)

		

		self.video_width = int(self.video.get(3))
		self.video_height = int(self.video.get(4))
		print(self.video_width)
		print(self.video_height)



		writer = cv2.VideoWriter( filename = self.video_name, fourcc = cv2.VideoWriter_fourcc(*'MP4V'), fps = 30, frameSize =(self.video_width, self.video_height))
		self.text = Text()
		self.text.fill_heightlist(self.video_height)
		
		print(self.text.text)
		while True:
			returnable, frame = self.video.read() 
			
			if returnable == True :
				self.put_text_in_video(self.text, frame)

				writer.write(frame)
				
				
			
			else:
				break
			
		writer.release()
		self.video.release()
		
		

if __name__ == "__main__":
	


	producer = Producer()
	producer.produce_video()
	upload()
	