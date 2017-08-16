# write path to config file
# walk user through repo setup

# download queue.py

import os
import subprocess

import utils

try:
	with open("queue.py", mode="rb"):	pass
except OSError:
	downloadFile()
else:
	check_purity()

import queue

def reactorSetup():
	# TODO
	onerror = "ignore"
	queue.define_rules("crypto",
		[ queue.PhysicsRule(git_func_path, git_func_name, expectedAns, onerror)
		, queue.PhysicsRule(localDB_func_path, localDB_func_name, expectedAns, onerror)
		])
	return

def envSetup():
	def test_gp(git_path="git"):
		x = subprocess.run(f"{git_path} version", stdout=subprocess.PIPE, stderr=subprocess.PIPE)
	git_path = input("Enter path to git executable")
	openssl_path = 
	return

def directorySetup():
	return

def configFileSetup():
	return

def main():
	reactorSetup()
	envSetup()
	directorySetup()
	configFileSetup()
	return

if __name__ == '__main__':
	main()



def downloadFile():
	import urllib
	req = urllib.request.urlopen(URL)
	data = req.read()
	with open("queue.py", mode="wb") as fp:
		fp.write(data)
	return "success"

def check_purity():
	if utils.calc_hash("queue.py") == "":
		# no need for hmac/secrets.compare_digest()
		pass
	else:
		raise RuntimeError("queue.py is corrupted")
