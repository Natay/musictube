

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

OPTS = {
'format': 'bestaudio/best',
'postprocessors': [{
		'key': 'FFmpegExtractAudio',
		'preferredcodec': 'mp3',
		'preferredquality': '192'
		}],
'forcefilename': True,
}


def main():

	from argparse import ArgumentParser
	import os
	import time

	parser = ArgumentParser()
	parser.add_argument("links", type=str, help="file with links")
	parser.add_argument("dest_dir", type=str, help="dir to download to")

	args = parser.parse_args()

	links = urls_from_file(args.links)
	
	# Make a new dir, way easier to import into library this way
	now = time.time()
	destpath = os.path.join(args.dest_dir, f"{now}")

	# Add a trailing "/" or "\" if it is there
	destpath = destpath if destpath.endswith(os.sep) else destpath + os.sep

	os.makedirs(destpath, exist_ok=True)


	for link in links:

		download(link, destpath)


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
	OPTS['progress_hooks']= [myhook]


	with youtube_dl.YoutubeDL(OPTS) as ydl:
		ydl.download([link])

	print('-'*100)



if __name__ == '__main__':
	main()




