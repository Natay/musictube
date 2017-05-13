

"""
main module extracting mp3

input:
	-link: youtube link with music wanted 
	-dest: destination directory

ouputs:

	-mp3 file in specified directory

"""


from __future__ import unicode_literals 
import sys

import youtube_dl



def main():

	dest = sys.argv[2]
	urlfile = sys.argv[1]	
	
	links = urls_from_file(urlfile)
	
	if dest[-1] != '/': dest + '/'
	print(1/0)


	for link in links:
		
		download(link, dest)
	


OPTS = {
	'format': 'bestaudio/best',
	'postprocessors': [{
			'key': 'FFmpegExtractAudio',
			'preferredcodec': 'mp3',
			'preferredquality': '192'
			}],
	'progress_hooks': [myhook],
	'forcefilename': True,
	}



def myhook(e):
	
	if e['status'] == 'finished':
		print('DOWNLOAD COMPLETE, converting to mp3')


def urls_from_file(txtfile):

	with open(txtfile, 'r') as links:

		for one_link in links:
			yield one_link

 
def download(link, dest):

	global OPTS
	
	OPTS['outtmpl'] = dest + '%(title)s.%(ext)s'


	with youtube_dl.YoutubeDL(OPTS) as ydl:
		ydl.download([link])

	print('-'*100)
	
	

if __name__ == '__main__':

	main()
		



