

"""
main module extracting mp3

input:
	-yt_url: youtube link with music wanted 

"""



from __future__ import unicode_literals # 2.7 compatablity 
import youtube_dl





def extract_infot(yt_url):
	return NotImplemented 

def download(yt_url):

	ydl_opts = {
		'format': 'bestaudio/best',
		'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192'
				}],
		}
	with youtube_dl.YoutubeDL(ydl_opts) as ydl:
    		ydl.download(['http://www.youtube.com/watch?v=BaW_jenozKc'])
