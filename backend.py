import os
import sys
import shlex
import shutil
import getpass
import subprocess

import queue

CRYPTO_BASE = 'openssl enc -{crypto_direction} -salt -aes-256-cbc -base64 -in "{inFile}" -out "{outFile}"'

def shall_i(crypto_direction, filePath):
	SPACE = " "
	file_is_encrypted = True
	with open(filePath, mode='rt') as fp:
		for i, aLine in enumerate(fp):
			if SPACE in aLine:
				file_is_encrypted = False
				break
			if i > 99:
				break
	answer = "no"
	if file_is_encrypted and crypto_direction is "decrypt":
		answer = "yes"
	if not file_is_encrypted and crypto_direction is "encrypt":
		answer = "yes"
	return answer

def crypto(filePath, action):
	if action is "encrypt":
		crypt_dirn = "e"
	elif action is "decrypt":
		crypt_dirn = "d"
	else:
		raise ValueError(f'crypto() doesn\'t know how to "{action}" a file')
	if shall_i(action, filePath) is "no":
		raise RuntimeError(f"Cannot {action} already {action}ed file:\n\
		`{filePath}`") from None
	resultFile = filePath + ".temp"
	cmnd = CRYPTO_BASE.format(
		inFile=filePath,
		outFile=resultFile,
		crypto_direction=crypt_dirn
	)
	subprocess.run(shlex.split(cmnd), stdout=subprocess.DEVNULL)
	# if encryption is requested, then overwrite inFile
	# NOTE: at this point, filePath still contains plain text and although
	# copy2 will overwrite it with its encrypted version, we can't risk the
	# scenario where HDD forensics experts are able to retrive previously
	# written data (which was in plain text) due to insufficient overwrites
	# so we write garbage 35 times berfor copying the aes-encrypted-plain-text
	# from resultFile to inFile (i.e. filePath)
	if action is "encrypt":
		overwrite(filePath)
	shutil.copy2(src=resultFile, dst=filePath)
	# SIDE_EFFECT: for git and local_db to do its job
	queue.push("crypto", {"action": action, "subject": filePath})
	# sugar
	if action is "encrypt":
		print(f"Entry for {path2date(filePath)} encrypted successfully")
	else:
		overwrite(resultFile)
		# because in case of decrypt-a-file, resultFile would contian plain
		# text and the fact that resultFile is stored somewhere else on disk,
		# we cannot risk simply deleteing resultFile without first garbling it
		os.start(filePath)
	os.remove(resultFile)
	return "success"

def date2path(date, month_num, full_year):
	return path

def path2date():
	return date

def overwrite(filePath, passes=35):
	""" write random data of size slightly larger than initial size of
	`filePath` in file pointed by `filePath`, `passes` number of times
	"""
	file_size = os.stat(filePath).st_size / 1024
	file_size = math.ceil(file_size)
	target_size = file_size * 1024
	with open(filePath, mode='rb') as fp:
		for _ in range(passes):
			fp.write(os.urandom(target_size))
	return
