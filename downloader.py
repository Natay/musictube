

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

	parser = ArgumentParser()
	parser.add_argument("links", type=str, help="file with links")
	parser.add_argument("dest_dir", type=str, help="dir to download to")

	args = parser.parse_args()

	links = urls_from_file(args.links)

	for link in links:

		download(link, args.dest_dir)


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




