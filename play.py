#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
Searching and playing your favorites musics from command shell

Usage: play <options> <keywords>

Options:
-Z -> Play files randomly forever (default disabled)
-L -> Repeat all (default disabled)
-R -> Repeat current item (default disabled)

Keywords:
--all -> Searches all mp3 files generating a playlist and execute it.
--started-from-file %U -> Execute the last playlist saved

Example:
play -R
play --all
play -R --all
play -Z metallica
play beatles let it be
"""


"""
Author: Laercio Serra (laercio.serra@gmail.com)
Version 1.0 - 03/21/2016 - Coding the first version
Version 1.1 - 03/24/2016 - Added a validation the arguments
Version 1.2 - 03/25/2016 - Cleaning the code
"""

# ------------ module imports ------------
import sys
import os
import fnmatch


# ------------ configuration options ------------
# change this to your mp3 root folder
media = "file://"
root_folder = "/home/lserra/Music"
pattern = "*.mp3"
player = "/usr/bin/vlc"
playlist_filename = "playlist.m3u"


# ------------ functions used ------------
def find_files(root_folder, keylist):
	"""
	Gets a list of files in the directory (and subdirectories)
	with contains all the keywords in 'keylist' at the filename
	"""
	matches = []
	for k in range(len(keylist)):
		if keylist[k] == '--all':
			for root, dirs, files in os.walk(root_folder):
				for filename in files:
					if fnmatch.fnmatch(filename, pattern):
						matches.append(os.path.join(root_folder, filename))
		else:
			for root, dirs, files in os.walk(root_folder):
				for filename in files:
					# for each filename, check if it contains all the keywords
					lowercase = filename.lower()
					if lowercase.endswith(".mp3"):
						for keyword in keylist:
							if keyword not in lowercase:
								break
							else:
								# all keywords were found: add to the result list
								matches.append(os.path.join(root_folder, filename))
	return matches


def make_playlist(file_list):
	"""
	Generates a playlist file for the filenames at fileList
	"""
	playlist = open(playlist_filename, "w")  # create the file
	playlist.write("#EXTM3U\n")  # add the standard header
	for each_file in file_list:
		playlist.write(each_file + "\n")  # add the items
	playlist.close()


def play_it(opt):
	"""
	Execute the playlist.
	"""
	print player, opt, playlist_filename
	command = " ".join([player, opt, playlist_filename, "&"])
	os.popen(command)


def main():
	"""
	Program main function.
	"""
	# if no arguments or keyword was entered, give the user a nice tip...
	print "-" * 60
	if len(sys.argv) < 2:
		print __doc__
		print "-" * 60
	else:
		args = sys.argv
		args.remove('play.py')

		# validating the arguments
		if args[0] != '--all':
			if args[0] in ('-Z', '-L', '-R'):
				opt = args[0]
			else:
				opt = '-Z'
		else:
			opt = '-Z'

		# get the keywords to search for the mp3s
		# if we don't use str.lower the user will never find
		# anything if it puts a uppercase letter in any of the
		# keywords.
		keylist = []
		for x in args:
			if x in ('-Z', '-L', '-R'):
				pass
			elif x not in opt:
				keylist.append(x.lower())

		if len(keylist) == 0 and len(opt) > 0:
			keylist = ['--all']

		print "Searching for mp3 files with the keyword(s): "
		print keylist
		files = find_files(root_folder, keylist)
		if files:
			print "Finished! Found", len(files), "file(s). So, let's play!"
			make_playlist(files)
			play_it(opt)
		else:
			print "Sorry, didn't find anything file :-( Did you misspell it?"

		print "-" * 60

if __name__ == '__main__':
	main()
	sys.exit(0)  # successful termination