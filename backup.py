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
		self.__loadEmailServerConfig()
		self.__TO = self.__cfg['DEFAULT']['TO']
		self.__Subject = self.__cfg['DEFAULT']['SUBJECT']
		self.__backuppath = self.__readBackupPath()
		self.__configpath = self.__configPath()

	def __loadEmailServerConfig(self):
		self.__SERVER = self.__cfg['MAIL']['SERVER']
		self.__FROM = self.__cfg['MAIL']['FROM']
		self.__USER = self.__cfg['MAIL']['USER']
		self.__PASSWD = self.__cfg['MAIL']['PASSWD']
		self.__SUBJECT = self.__cfg['MAIL']['SUBJECT']
		self.__TO = self.__cfg['MAIL']['TO']

	def __sendMSG(self, message):
		msg = MIMEText(message)
		msg['TO'] = self.__TO
		msg['FROM'] = self.__FROM
		msg['SUBJECT'] = self.__SUBJECT
		server = smtplib.SMTP_SSL(self.__SERVER)
		server.login(self.__USER, self.__PASSWD)
		server.sendmail(self.__FROM, [self.__TO], msg.as_string())
		server.quit()

	#def __configPath(self):
	#	if not(os.path.exists(self.cfg
	
	def __readBackupPath(self):
		if not(os.path.exists(self.__cfg['DEFAULT']['BACKUPDIR'])):
			self.__sendMSG('['+time.ctime()+'] No Backup Folder found in System!')
			print('['+time.ctime()+'] No Backup Folder found in System!', file=sys.stderr)
			sys.exit('No Backup Folder found in System!')
		else:
			 return self.__cfg['DEFAULT']['BACKUPDIR']

if __name__ == "__main__":
	a = backup()
	a.maintenance()
	a.backup()
