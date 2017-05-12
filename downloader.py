

"""
main module extracting mp3

input:
	-yt_url: youtube link with music wanted 

"""



from __future__ import unicode_literals # 2.7 compatablity 
import youtube_dl




def myhook(e):
	
	if e['status'] == 'finished':
		print('Download complete, converting to mp3')




def save(mp3, path):
	# last thing to work on 
	return NotImplementedError 





class Download(object):


	def __init__(self, yt_url):

		self.link = yt_url

		self.opts = {
			'format': 'bestaudio/best',
			'postprocessors': [{
				'key': 'FFmpegExtractAudio',
				'preferredcodec': 'mp3',
				'preferredquality': '192'
					}],
			'progress_hooks': [myhook],
			}

	def info(self):

		"""
		Extract page info without downloading link 
		
		"""

		return NotImplemented 



	def download(self):


		"""
		Download link given

		"""

		with youtube_dl.YoutubeDL(self.opts) as ydl:
	    		ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])


if __name__ == '__main__':
	
	testlinks = ['https://www.youtube.com/watch?v=vxa-RHeOc0w',
		    'https://www.youtube.com/watch?v=qkxEKumTj08' ]

	
	for link in testlinks:

		dl = Download(link)

		print(dl.info()) # print info 
		
		

		
















