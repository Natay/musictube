

"""
main module extracting mp3

input:
	-yt_url: youtube link with music wanted 
	-save: destination directory

ouputs:

	-mp3 file in specified directory

"""


from __future__ import unicode_literals 
import youtube_dl




def myhook(e):
	
	if e['status'] == 'finished':
		print('DOWNLOAD COMPLETE, converting to mp3')



def urls_from_file(txtfile):

	with open(txtfile, 'r') as links:

		for one_link in links:
			yield one_link

 

class Download(object):


	def __init__(self, yt_url, save):

		self.link = yt_url
	
		self.opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192'
					}],
			'progress_hooks': [myhook],
			'forcefilename': True,
			'outtmpl': save + '%(title)s.%(ext)s'
			}

	def info(self):

		"""
		Extract page info without downloading link ( bit of an overkill )
		
		"""
		with youtube_dl.YoutubeDL(self.opts) as ydl:
		
			return ydl.extract_info(self.link, download=False)


	def download(self):
 

		"""
		Download mp3

		"""

		with youtube_dl.YoutubeDL(self.opts) as ydl:
			ydl.download([self.link])
		
		print('-'*100)


if __name__ == '__main__':
	
	

	links = urls_from_file('/home/natay/Desktop/mymusic/links.txt')
	
	for link in links:
		

		Download(link, '/home/natay/Desktop/mymusic/').download()
		



		
		

		
















