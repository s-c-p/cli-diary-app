import os
import sys
import shlex
import random
import shutil
import getpass
import subprocess

SPACE = " "
CRYPTO_BASE = 'openssl enc -{crypto_direction} -aes-256-cbc -salt -a -in "{inFile}" -out "{outFile}"'

def shall_i(crypto_direction, filePath):
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
		raise ValueError('crypto() doesn\'t know how to "{}" a file'.format(action))
	if shall_i(action, filePath) is "no":
		raise RuntimeError("Cannot {} already {}ed file".format(action, action))
	tempFile = filePath + ".temp"
	cmnd = CRYPTO_BASE.format(crypto_direction=crypt_dirn, inFile=filePath, outFile=tempFile)
	subprocess.run(shlex.split(cmnd), stdout=subprocess.DEVNULL)
	shutil.copy2(src=tempFile, dst=filePath)
	with...as...:
		my_name = sys._getframe().f_code.co_name # bit.ly/2veIOw3
		app.announce(frm=my_name, info={
			"": ""
		})
	shredFile(tempFile)
	return "success"

def date2path():
	return path

def path2date():
	return date

def shredFile(filePath):
	rand_init = os.urandom(512)
	random.seed(rand_init)
	file_size = os.stat(filePath).st_size / 1024 / 1024
	file_size = math.ceil(file_size)
	fp = open(filePath, mode='')
	with fp:
	return "success"

