

"""
main module extracting mp3

input:
	-yt_url: youtube link with music wanted 

"""
#TODO: change destination path


from __future__ import unicode_literals # 2.7 compatablity 
import youtube_dl




def myhook(e):
	
	if e['status'] == 'finished':
		print('DOWNLOAD COMPLETE, converting to mp3')



def urls_from_file(txtfile):

	with open(txtfile, 'r') as links:

		for one_link in links:
			yield one_link

 

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
			'forcefilename': True
			}

	def info(self):

		"""
		Extract page info without downloading link ( bit of an overkill )
		
		"""
		with youtube_dl.YoutubeDL(self.opts) as ydl:
			res = ydl.extract_info(self.link, download=False)

			return res


	def download(self):


		"""
		Download mp3

		"""

		with youtube_dl.YoutubeDL(self.opts) as ydl:
	    		ydl.download([self.link])


if __name__ == '__main__':
	
	testlinks = ['https://www.youtube.com/watch?v=vxa-RHeOc0w',
		    'https://www.youtube.com/watch?v=qkxEKumTj08' ]

	
	for link in testlinks:

		dl = Download(link)

		print(dl.download()) # print info
 
		break

		
		

		
















