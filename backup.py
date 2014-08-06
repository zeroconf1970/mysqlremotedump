#!/usr/bin/python3

import configparser
import os.path
import sys
import time
import smtplib
from email.mime.text import MIMEText
import sendmail

class backup:

	def __init__(self):
		self.__cfg = configparser.ConfigParser()
		self.__cfg.read('config.ini')
		self.__TO = self.__cfg['DEFAULT']['TO']
		self.__SUBJECT = self.__cfg['DEFAULT']['SUBJECT']
		self.__mailer = sendmail.sendMail()
		self.__backuppath = self.__readBackupPath()
		self.__configpath = self.__configPath()

	def __configPath(self):
		if not(os.path.exists(self.__cfg['DEFAULT']['CONFIGDIR'])):
			self.__mailer.sendMail(self.__TO, self.__SUBJECT, ('['+time.ctime()+'] No Config Folder found in System!'))
			print('['+time.ctime()+'] No Config Folder found in System!', file=sys.stderr)
			sys.exit('['+time.ctime()+'] No Config Folder found in System!')
		else:
			return self.__cfg['DEFAULT']['CONFIGDIR']

	def __readBackupPath(self):
		if not(os.path.exists(self.__cfg['DEFAULT']['BACKUPDIR'])):
			self.__mailer.sendMail(self.__TO, self.__SUBJECT, ('['+time.ctime()+'] No Backup Folder found in System!'))
			print('['+time.ctime()+'] No Backup Folder found in System!', file=sys.stderr)
			sys.exit('No Backup Folder found in System!')
		else:
			 return self.__cfg['DEFAULT']['BACKUPDIR']

if __name__ == "__main__":
	a = backup()
	a.load()
	a.maintenance()
	a.backup()
