#!/usr/bin/python3

import configparser
import os.path
import sys
import time

class backup:

	def __init__(self):
		self.cfg = configparser.ConfigParser()
		self.cfg.read('config.ini')
		self.backuppath = self.__readBackupPath()
		self.configpath = self.__configPath()

	def __configPath(self):
		if not(os.path.exists(self.cfg
	
	def __readBackupPath(self):
		if not(os.path.exists(self.cfg['DEFAULT']['BACKUPDIR'])):
			print('['+time.ctime()+'] No Backup Folder found in System!', file=sys.stderr)
			sys.exit('No Backup Folder found in System!')
		else:
			 return self.cfg['DEFAULT']['BACKUPDIR']

if __name__ == "__main__":
	a = backup()
	a.maintenance()
	a.backup()
